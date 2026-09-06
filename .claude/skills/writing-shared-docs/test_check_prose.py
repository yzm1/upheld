#!/usr/bin/env python3
"""Tests for the writing-shared-docs prose gate.

The gate is ten regexes and a few thresholds. Its whole value is whether those
regexes fire on the right lines, so each one is pinned here from both sides:
what it must catch, and what it must leave alone.

    python3 -m pytest test_check_prose.py -q
    python3 test_check_prose.py            # same tests, no pytest needed
"""
import contextlib
import importlib.util
import io
import os
import re
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location(
    "check_prose", os.path.join(HERE, "check_prose.py"))
cp = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(cp)

# A `.tmp` directory at the repository root is used for temporary files when
# it exists; otherwise the system default. Either way every file is unlinked.
_TMP = os.path.join(HERE, "..", "..", "..", ".tmp")
TMPDIR = os.path.abspath(_TMP) if os.path.isdir(_TMP) else None

ROW = re.compile(r"^\s+(ok|FAIL)\s+(.+?)\s{2,}(\S+)\s+target", re.M)


def run(body, suffix=".md", owns=frozenset()):
    """Run the gate over `body` and return {check name: (value, passed)}."""
    fd, path = tempfile.mkstemp(suffix=suffix, dir=TMPDIR)
    with os.fdopen(fd, "w", encoding="utf-8") as fh:
        fh.write(body)
    saved, cp.OWNS = cp.OWNS, set(owns)
    out = io.StringIO()
    try:
        with contextlib.redirect_stdout(out):
            cp.report(path)
    finally:
        cp.OWNS = saved
        os.unlink(path)
    text = out.getvalue()
    rows = {name.strip(): (value, verdict == "ok")
            for verdict, name, value in ROW.findall(text)}
    rows["_raw"] = text
    return rows


def passed(rows, check):
    return rows[check][1]


# --- defect 1: an adjective that ends like a participle is not passive voice ---

REAL_PASSIVES = [
    "The run was cancelled by the scheduler.",
    "Records are written by the worker.",
    "The job is scheduled every hour.",
    "The file was sent to the queue.",
    "The lock is held by the leader.",
    "The answer was told to nobody.",
    "The image is built from source.",
    "The change is thought to be safe.",
    "The claim is made without evidence.",
    "The budget was spent in August.",
]

NOT_PASSIVES = [
    "The traversal is deterministic.",
    "The result is different from before.",
    "The value is present in the table.",
    "The schema is consistent everywhere.",
    "The port is open on every host.",
    "The branch is old but it still builds.",
    "The warning is urgent and nobody read it.",
    "The two runs are equivalent.",
]


def test_passive_still_catches_real_passives():
    for s in REAL_PASSIVES:
        assert cp.is_passive(s), f"missed a real passive: {s}"


def test_passive_ignores_participle_shaped_adjectives():
    for s in NOT_PASSIVES:
        assert not cp.is_passive(s), f"false positive: {s}"


def test_passive_rate_reported_from_the_filtered_count():
    rows = run(" ".join(NOT_PASSIVES))
    assert passed(rows, "passive voice"), rows["_raw"]


# --- defect 2: a declared word is exempt from the banned list too ---

def test_banned_words_flagged_when_undeclared():
    rows = run("The admin portal is a robust and seamless piece of work here.")
    assert not passed(rows, "banned words")


def test_declared_words_are_not_banned_words():
    rows = run("The admin portal shows the number to every reader.",
               owns={"portal"})
    assert passed(rows, "banned words"), rows["_raw"]


def test_declaring_one_word_does_not_excuse_the_others():
    rows = run("The admin portal is a robust piece of work here.",
               owns={"portal"})
    assert not passed(rows, "banned words")
    assert "robust" in rows["_raw"] and "portal" not in rows["_raw"].split("banned:")[1]


def test_reader_vocabulary_is_loaded_by_default():
    owns, rest = cp.load_vocabulary(["some-file.md"])
    assert "ci" in owns and "yaml" in owns and "must" in owns
    assert rest == ["some-file.md"]


def test_owns_flag_is_parsed_and_stripped():
    owns, rest = cp.load_vocabulary(["--owns", "widget,Gadget", "f.md"])
    assert {"widget", "gadget"} <= owns
    assert rest == ["f.md"]


# --- defect 3: capitals in a heading are formatting, not an identifier ---

IDENTIFIERS = ["run_summary", "permissions.py", "requireAuth", "MAX_RETRIES", "ZZQ"]
CAPITALISED_ENGLISH = ["PLAN", "MODEL", "CONFIRMED", "PART", "NOT", "BEFORE", "AFTER"]


def test_identifiers_are_flagged():
    for w in IDENTIFIERS:
        assert cp.JARGON_RE.search(w) and cp.is_jargon(w), f"missed: {w}"


def test_ordinary_words_in_capitals_are_not_identifiers():
    for w in CAPITALISED_ENGLISH:
        assert not cp.is_jargon(w), f"false positive: {w}"


def test_declared_acronyms_are_not_identifiers():
    saved, cp.OWNS = cp.OWNS, {"dlq"}
    try:
        assert not cp.is_jargon("DLQ")
        assert cp.is_jargon("ZZQ")
    finally:
        cp.OWNS = saved


def test_insider_check_passes_on_capitalised_english():
    rows = run("## PLAN\n\nThe PART marked CONFIRMED is ready for the reader now.\n")
    assert passed(rows, "insider terms"), rows["_raw"]


# --- defect 4: a list marker is not an em dash ---

def test_nested_list_markers_do_not_count_as_dashes():
    body = ("Some prose that carries a fact for the reader.\n\n"
            "- top level item here\n"
            "  - nested item one\n"
            "  - nested item two\n"
            "  - nested item three\n"
            "  - nested item four\n")
    assert passed(run(body), "em dashes")


def test_real_em_dashes_still_count():
    body = "\n\n".join(
        f"Prose — with a dash — in it, number {i}." for i in range(8))
    assert not passed(run(body), "em dashes")


def test_hyphen_between_words_counts_as_a_dash():
    body = "\n\n".join(f"A hyphen - used as punctuation here, {i}." for i in range(8))
    assert not passed(run(body), "em dashes")


def test_double_hyphen_between_words_counts_as_a_dash():
    """Markdown writers type " -- " for an em dash. Counting only the real
    character passed a document carrying fifteen per thousand words."""
    body = "\n\n".join(f"A dash -- typed as two hyphens, number {i}." for i in range(8))
    assert not passed(run(body), "em dashes")


def test_hyphenated_words_do_not_count():
    body = "\n\n".join(f"A well-known state-of-the-art result, number {i}." for i in range(8))
    assert passed(run(body), "em dashes")


def test_underscores_inside_a_name_survive_emphasis_stripping():
    """`OBLIGATION_SURVEY.md` is one name. Stripping its underscore as if it
    were an emphasis marker produced a mangled name that the jargon check then
    flagged, so the gate reported a defect the document did not have."""
    assert "OBLIGATION_SURVEY.md" in cp.to_text("see OBLIGATION_SURVEY.md now", True)
    assert cp.to_text("**bold** and _italic_ words", True) == "bold and italic words"


def test_numbered_and_wrapped_list_items_are_not_measured_for_length():
    """A reading list of eight numbered items measured as one 118-word
    sentence, because only `-` and `*` markers were recognised and only their
    first line was dropped."""
    body = ("A short sentence of prose that carries a fact.\n\n"
            "1. `docs/METHOD.md`. The method, normative, and a long enough item that\n"
            "   its continuation line wraps onto a second line of the file here.\n"
            "2. `docs/CHECKER.md`. The checker, with the same wrapping behaviour and\n"
            "   the same continuation line that must not be read as prose.\n"
            "- A bulleted item that also wraps across two lines and would otherwise\n"
            "  be merged into whatever sentence fragment came before it.\n")
    rows = run(body)
    assert passed(rows, "over 25 words"), rows["_raw"]
    assert passed(rows, "mean sentence"), rows["_raw"]


def test_html_comments_are_invisible_to_the_gate():
    """A reader of the rendered page never sees a comment, so the gate does not
    grade it. The prose-gate:ignore fence is one case of this."""
    rows = run("<!-- The robust seamless ecosystem will drive the deep dive. -->\n\n"
               "A plain sentence carries the fact for the reader.\n")
    assert passed(rows, "banned words"), rows["_raw"]


def test_a_sentence_ending_inside_a_quotation_still_splits():
    """`components." It runs` is two sentences. The splitter looked for the
    full stop immediately before the space, so the closing quote hid the
    boundary and a two-sentence line measured as one long one."""
    assert len(cp.sentences('The README calls it "a lockfile for contracts." It runs on Python.')) == 2
    assert len(cp.sentences("The README calls it a lockfile for contracts. It runs on Python.")) == 2


def test_each_list_item_is_its_own_sentence_for_the_voice_rate():
    """Three items, one of them passive, is a one-in-three rate. With the
    markers left in the text the three items read as one sentence and the
    rate was reported as one in one."""
    body = ("- The worker writes the record.\n"
            "- The record was written by the worker.\n"
            "- The reader checks the record.\n")
    text = cp.to_text(cp.drop_quoted(body, True), True)
    assert len(cp.sentences(text)) == 3


# --- the other detectors, pinned so a later edit cannot quietly drop one ---

def test_machine_tells_are_caught():
    for snippet in ["This isn't a bug, it's a feature.",
                    "Let's dive in and see what happened.",
                    "The finding truly underscores the pivotal risk.",
                    "I found no production release anywhere."]:
        rows = run(snippet + " The rest of the line carries a plain fact.")
        assert not passed(rows, "machine tells"), snippet


def test_figurative_language_is_caught():
    rows = run("The run speaks for the technology and the service cares about order.")
    assert not passed(rows, "figurative")


def test_abstraction_density_is_caught():
    rows = run("The classification, verification and implementation of the "
               "orchestration is a function of the configuration.")
    assert not passed(rows, "abstraction")


def test_plain_prose_passes_every_check():
    body = ("The gate reads a file and prints nine rows.\n\n"
            "Each row names a rule, the number it found and the target.\n\n"
            "A run that fails any row exits with status one.\n")
    rows = run(body)
    for name, row in rows.items():
        if name != "_raw":
            assert row[1], f"{name} failed on plain prose:\n{rows['_raw']}"


# --- exemptions: the gate cannot tell use from mention, so it skips both ---

def test_ignore_block_is_skipped():
    banned = "The robust and seamless ecosystem will drive the deep dive."
    assert not passed(run(banned), "banned words")
    fenced = f"<!-- prose-gate:ignore -->\n{banned}\n<!-- /prose-gate:ignore -->\n"
    rows = run(fenced + "\nA plain sentence carries the fact for the reader.\n")
    assert passed(rows, "banned words"), rows["_raw"]


def test_code_and_tables_are_skipped():
    body = ("A plain sentence carries the fact for the reader here.\n\n"
            "```\nrobust seamless ecosystem\n```\n\n"
            "| name | note |\n| --- | --- |\n| drive | leverage |\n\n"
            "Inline `robust` code is a mention as well.\n")
    assert passed(run(body), "banned words")


# --- the HTML path, used before publishing an artifact ---

def test_html_prose_is_measured():
    rows = run("<h2>A heading that makes a claim</h2>"
               "<p>The scheduler retries once and then stops.</p>"
               "<p>Every failure names the line that caused it.</p>", suffix=".html")
    assert passed(rows, "banned words") and passed(rows, "mean sentence")


def test_html_banned_words_are_caught():
    rows = run("<p>Our robust and seamless ecosystem will drive the result.</p>",
               suffix=".html")
    assert not passed(rows, "banned words")


# --- the skill dogfoods its own gate ---

def test_skill_md_passes_its_own_gate():
    owns, _ = cp.load_vocabulary([])
    saved, cp.OWNS = cp.OWNS, owns
    out = io.StringIO()
    try:
        with contextlib.redirect_stdout(out):
            ok = cp.report(os.path.join(HERE, "SKILL.md"))
    finally:
        cp.OWNS = saved
    assert ok, out.getvalue()


if __name__ == "__main__":
    tests = [(n, f) for n, f in sorted(globals().items())
             if n.startswith("test_") and callable(f)]
    failed = 0
    for name, fn in tests:
        try:
            fn()
            print(f"  ok    {name}")
        except AssertionError as exc:
            failed += 1
            print(f"  FAIL  {name}\n        {exc}")
    print(f"\n{len(tests) - failed}/{len(tests)} passed")
    raise SystemExit(1 if failed else 0)
