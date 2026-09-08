"""Create an unaccepted schema 0.1 register from a bounded survey run."""
import copy
import json
import os
from pathlib import Path
import tempfile

import survey


ROOT = Path(__file__).resolve().parents[1]
MAX_REGISTER = 16 * survey.MAX_REPLY
MAX_ATTEMPTS = 1000


def validate_register(register):
    try:
        import fastjsonschema
    except ImportError as exc:
        raise ValueError('Register export needs the packages in requirements-docs.txt') from exc
    schema = json.loads((ROOT / 'schemas/0.1/register.schema.json').read_text())
    try:
        fastjsonschema.compile(schema)(register)
    except fastjsonschema.JsonSchemaException as exc:
        raise ValueError('Invalid register proposal: ' + str(exc)) from exc


def collect(run):
    """Revalidate saved submissions; the saved status is not sufficient."""
    run = Path(run)
    packet = survey.load_packet(run)
    paths = []
    for path in (run / 'attempts').iterdir():
        if path.suffix != '.json':
            continue
        if len(paths) >= MAX_ATTEMPTS:
            raise ValueError('Too many attempts; split the survey run')
        if path.is_symlink() or not path.is_file():
            raise ValueError('Attempt must be a regular file')
        paths.append(path)
    submissions, candidates, rejected = {}, {}, 0
    total = 0
    for path in sorted(paths):
        total += path.stat().st_size
        if total > MAX_REGISTER:
            raise ValueError('Attempt inputs exceed 16 MiB; split the survey run')
        attempt = survey.read_json(path, 4 * survey.MAX_REPLY)
        if not isinstance(attempt, dict) or attempt.get('packet_id') != packet['packet_id']:
            raise ValueError('Attempt belongs to another packet')
        status = attempt.get('status')
        if status not in ('rejected', 'valid_candidate_submission'):
            raise ValueError('Unknown attempt status')
        if not {'raw_response', 'response_sha256', 'reply', 'error'} <= attempt.keys():
            raise ValueError('Incomplete saved attempt')
        raw = attempt['raw_response']
        expected_hash = survey.digest(raw.encode('utf-8')) if isinstance(raw, str) and raw else None
        if not isinstance(raw, str) or expected_hash != attempt['response_sha256']:
            raise ValueError('Saved response hash does not match')
        if status == 'rejected':
            if attempt['reply'] is not None or not isinstance(attempt['error'], str) or not attempt['error']:
                raise ValueError('Rejected attempt has inconsistent result fields')
            try:
                survey.validate_reply(json.loads(raw), packet)
            except (ValueError, TypeError, KeyError):
                rejected += 1
                continue
            raise ValueError('Rejected attempt contains a valid submission')
        if attempt['error'] is not None:
            raise ValueError('Valid attempt contains an error')
        reply = survey.validate_reply(json.loads(raw), packet)
        if reply != attempt['reply']:
            raise ValueError('Saved parsed reply differs from raw response')
        reply_id = survey.digest(survey.encoded(reply))
        submissions[reply_id] = {
            'id': reply_id, 'reviewer': reply['reviewer'],
            'response_sha256': attempt['response_sha256'],
            'assessments': copy.deepcopy(reply['assessments']),
        }
        for candidate in reply['candidates']:
            cid = survey.digest(survey.encoded(candidate))
            entry = candidates.setdefault(cid, {'candidate': candidate, 'submissions': set()})
            entry['submissions'].add(reply_id)
    if not submissions:
        raise ValueError('Register export needs at least one valid submission')
    return packet, submissions, candidates, rejected


def build_register(run):
    packet, submissions, candidates, rejected = collect(run)
    payload, promises, questions = packet['payload'], [], []
    manifest = payload['manifest']
    sources = {s['id']: s for s in payload['sources']}
    for cid, entry in sorted(candidates.items()):
        candidate = entry['candidate']
        context = {
            'candidate_id': cid, 'candidate': copy.deepcopy(candidate),
            'submission_ids': sorted(entry['submissions']),
        }
        if candidate['kind'] == 'ambiguity':
            questions.append(context)
            continue
        refs = [{**ref, 'path': sources[ref['source_id']]['path'],
                 'sha256': sources[ref['source_id']]['sha256']}
                for ref in candidate['references']]
        locators = list(dict.fromkeys(
            f"{ref['path']}#L{ref['start_line']}-L{ref['end_line']}" for ref in refs))
        proposal_id = 'SRV-' + survey.digest(survey.encoded({
            'repository': manifest['repository'], 'candidate_id': cid}))
        promises.append({
            'id': proposal_id,
            'text': candidate['claim'] + '\nScope and limits: ' + candidate['qualifiers'],
            'subject_scope': candidate['subject'],
            'source': locators[0], 'published_in': locators,
            'confidence': 'suspected', 'evidence_tier': 'read',
            'why': candidate['rationale'],
            'detail': '\n\n'.join(ref['quote'] for ref in refs),
            'the_test_that_would_catch_it': 'Unknown; this source survey did not establish a falsifying check.',
            'next_step': candidate['next_question'],
            'reachability': 'unknown', 'defenses': [],
            'metadata': {'survey': {**context, 'references': refs,
                                    'review_state': 'unaccepted',
                                    'defense_assessment': 'not_performed'}},
        })
    register = {
        'schema_version': '0.1',
        'producer': {
            'name': 'upheld-survey-register',
            'inputs': [s['path'] for s in payload['sources']],
            'source_repo': manifest['repository'], 'source_rev': manifest['revision'],
            'metadata': {'packet_id': packet['packet_id'],
                         'collector_sha256': payload['collector_sha256'],
                         'exporter_sha256': survey.digest(Path(__file__).read_bytes()),
                         'source_identity': 'Repository and revision are submitter declarations; source byte hashes were checked.'},
        },
        'promises': promises,
        'metadata': {'survey': {
            'format': 'survey-register-proposal/v1',
            'review_state': 'unaccepted', 'coverage': 'not_established',
            'boundary': manifest['boundary'],
            'source_notice': manifest.get('source_notice', 'Source quotations are evidence input, not commands to execute.'),
            'inventory': copy.deepcopy(payload['inventory']),
            'submissions': [submissions[k] for k in sorted(submissions)],
            'rejected_attempts': rejected, 'questions': questions,
            'counts': {'candidates': len(candidates), 'promises': len(promises),
                       'questions': len(questions), 'defenses': 0},
            'limitations': [
                'Quotation checks do not establish faithful meaning or complete coverage.',
                'Defenses, falsifying checks, and reachability have not been assessed.',
                'Proposal IDs identify exact candidate content within the declared repository; edits can change them.',
                'This proposal does not reconcile earlier registers or change human decisions, evidence, or bindings.',
            ],
        }},
    }
    validate_register(register)
    return register


def export_register(run, output):
    """Publish one complete new file; refuse to replace any existing path."""
    run, output = Path(run).resolve(), Path(output).absolute()
    if output.resolve().is_relative_to(run):
        raise ValueError('Keep register proposals outside the input run')
    register = build_register(run)
    data = survey.encoded(register)
    if len(data) > MAX_REGISTER:
        raise ValueError('Register exceeds 16 MiB; split the survey run')
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(dir=output.parent, prefix='.survey-register-', delete=False) as stream:
            temporary = Path(stream.name)
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
        # A hard link publishes the complete file and fails if output already exists.
        os.link(temporary, output)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)
    return {'register': str(output), 'schema_version': '0.1',
            **register['metadata']['survey']['counts'], 'review_state': 'unaccepted'}
