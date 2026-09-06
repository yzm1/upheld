"""Write a review copy. Preserve the historical input and never create evidence."""
import argparse
import copy
import json
from pathlib import Path


def convert(source):
    result = copy.deepcopy(source)
    result['schema_version'] = '0.1'
    old = result['producer']
    result['producer'] = {
        'name': 'tools/prepare_probe_review.py',
        'inputs': ['examples/heldtospec-contracts/obligations.register.json',
                   'tools/prepare_probe_review.py'],
        'source_repo': old['source_repo'], 'source_rev': old['source_rev'],
        'surveyed_on': old['surveyed_on'], 'metadata': {'original_producer': old}}
    result['metadata'] = {'source_format': '0.1-probe', 'review_state': 'unaccepted',
                          'original_summary': result.pop('summary')}
    for promise in result['promises']:
        promise['evidence_tier'] = 'unknown'
        promise['reachability'] = 'unknown'
        for defense in promise['defenses']:
            defense['needs_environment'] = []
            defense['last_actually_ran'] = None
            defense['metadata'] = {'environment_needs': 'not recorded',
                                   'execution_link': 'no defense-level run record'}
    return result


def diagnostics(source):
    return [{'code': 'promise_without_defense_or_gap', 'subject': p['id'],
             'message': 'Choose a defense or record an authorized gap decision.'}
            for p in source['promises'] if not p['defenses'] and 'gap' not in p]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source', type=Path)
    parser.add_argument('output', type=Path)
    args = parser.parse_args()
    if args.source.resolve() == args.output.resolve() or args.output.exists():
        parser.error('Output must be a new path; original records remain unchanged.')
    converted = convert(json.loads(args.source.read_text()))
    args.output.write_text(json.dumps(converted, indent=2, ensure_ascii=False) + '\n')
    print(json.dumps({'review_only': True, 'diagnostics': diagnostics(converted)}, indent=2))
