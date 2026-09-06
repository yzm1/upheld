#!/usr/bin/env python3
"""Measure the sentence rules in writing-shared-docs/SKILL.md.

Usage: python3 check_prose.py FILE [FILE ...]

Reports passive rate, mean sentence length, long-sentence share, abstraction
density and banned words, and flags the offending lines.

Two known limits, stated rather than hidden:

  * Passive detection over-counts. It matches a "to be" form followed by a past
    participle, so an adjective sharing a participle ending - "the result is
    different" - reads as passive. NOT_PARTICIPLE excludes the common ones; the
    list is not exhaustive. Read the flagged lines; do not rewrite on the number.
  * Terms your readers already own are declared with --owns or in
    reader-vocabulary.txt. Declaring one is a claim about your audience.
  * The insider-term check finds identifier-shaped words only. It cannot see
    plain-English jargon - "run selection", "the panel", "the engine" - so read
    the headings aloud to someone outside the project as well. Acronyms in
    capitals are flagged unless declared; ALLCAPS_COMMON exempts ordinary
    English words that appear capitalised as formatting.
  * It cannot tell use from mention. Quoted material, code and tables are
    exempt, and anything between <!-- prose-gate:ignore --> and
    <!-- /prose-gate:ignore --> is skipped.

Sentence-length rules apply to prose only. Headings, table cells and list items
(bulleted or numbered, including wrapped continuation lines) are measured for
voice and vocabulary but not for length. HTML comments are skipped entirely: a
reader never sees them.

  * The sentence splitter needs a capital letter after a full stop, with at
    most a closing quotation mark between them. A sentence that opens with an
    inline code term, which the gate strips, merges into the one before it,
    so code-dense prose reads longer than it is.
"""
import os
import re
import sys
from collections import Counter

PASSIVE_MAX = 10.0
MEAN_LEN_MAX = 20.0
LONG_SENTENCE_WORDS = 25
LONG_SENTENCE_MAX = 15.0
ABSTRACTION_MAX = 45.0

BE = r"(?:is|are|was|were|be|been|being|isn't|aren't|wasn't|weren't)"
ADV = r"(?:not|also|already|never|still|therefore|then|now)\s+"
PARTICIPLE = r"[a-z]+(?:ed|en|own|ought|uilt|eld|ent|ade|old)"
PASSIVE_RE = re.compile(rf"\b{BE}\s+(?:{ADV})?({PARTICIPLE})\b", re.I)

# Adjectives that end like a participle. "is different" is not passive voice.
NOT_PARTICIPLE = {
    "different", "present", "consistent", "inconsistent", "persistent",
    "dependent", "independent", "evident", "apparent", "current", "silent",
    "urgent", "absent", "competent", "excellent", "frequent", "permanent",
    "prominent", "recent", "equivalent", "transparent", "intelligent",
    "convenient", "adjacent", "coherent", "concurrent", "inherent", "latent",
    "sufficient", "insufficient", "efficient", "deficient", "ancient",
    "patient", "content", "potent", "open", "red", "old", "bold", "cold",
    "gold", "brown",
}


def is_passive(sentence):
    """True if any to-be + participle match is not an adjective in disguise."""
    return any(m.group(1).lower() not in NOT_PARTICIPLE
               for m in PASSIVE_RE.finditer(sentence))
ABSTRACT_RE = re.compile(r"\b[a-z]{4,}(?:tion|sion|ment|ance|ence|ity|ness)s?\b", re.I)

BANNED = [
    "drive", "unlock", "deep dive", "robust", "hub", "portal", "landscape",
    "ecosystem", "going forward", "leverage", "seamless", "comprehensive",
    "holistic", "utilise", "utilize", "it is worth noting", "importantly",
    "it should be said", "as mentioned above",
]
BANNED_RE = re.compile(r"\b(" + "|".join(re.escape(w) for w in BANNED) + r")\b", re.I)

# Abstract nouns that name the thing rather than dress it up.
EXEMPT = {"section", "question", "position", "version", "condition", "mention",
          "information", "attention", "documentation", "definition", "evidence", "sentence",
          "audience", "instance", "science", "reference"}

# Identifier-shaped words: a reader outside the project does not own these.
JARGON_RE = re.compile(
    r"\b(?:[a-z][a-z0-9]*_[a-z0-9_]+"          # snake_case
    r"|[a-z]+[A-Z][a-zA-Z]+"                    # camelCase
    r"|[A-Za-z_][\w-]*\.(?:py|sql|ya?ml|json|tsx?|jsx?|md|sh)"  # filenames
    r"|[A-Z]{3,}(?:_[A-Z]+)*(?!\.[A-Z])"        # SHOUTING_CONSTANTS
    r")\b")
# Ordinary English words that appear in capitals in headings, table cells and
# emphasis. Capitals are formatting there, not an identifier.
ALLCAPS_COMMON = {
    "NOT", "AND", "THE", "FOR", "ALL", "ANY", "NEW", "OLD", "YES", "NONE",
    "PLAN", "PLANS", "MODEL", "MODELS", "PART", "PARTS", "PROJECT", "DIAGRAM",
    "CONFIRMED", "FIXED", "OPEN", "CLOSED", "DONE", "TODO", "WARNING", "NOTE",
    "NOTES", "IMPORTANT", "SUMMARY", "STATUS", "RESULT", "RESULTS", "BEFORE",
    "AFTER", "TOTAL", "ROOT", "CAUSE", "RISK", "IMPACT", "SCOPE", "GOAL",
    "GOALS", "NEXT", "STEPS", "WHY", "HOW", "WHAT", "WHO", "WHEN", "WHERE",
    "PRO", "PROS", "CON", "CONS", "HIGH", "LOW", "MEDIUM", "CRITICAL", "MAJOR",
    "MINOR", "PASS", "FAIL", "PASSED", "FAILED", "ERROR", "TRUE", "FALSE",
}


def is_jargon(word):
    """Identifier-shaped, and not a word this document's readers already own."""
    return word.lower() not in OWNS and word not in ALLCAPS_COMMON


# Constructions that mark generated prose. Each one substitutes rhythm for a fact.
TELLS = [
    (r"\b(?:is|are|was|were|it's|that's)\s+not\s+(?:just|only|merely|simply)\b", "not just X but Y"),
    (r"\bnot\s+(?:just|only|merely|simply)\s+\w+[,;-]?\s+but\b", "not merely X but Y"),
    (r",\s+not\s+(?:a|an|the|its|his|her|their|your|our)\b", "X, not Y"),
    (r"\bthis\s+(?:isn't|is not)\b[^.]{0,60}\bit(?:'s| is)\b", "this isn't X, it's Y"),
    (r"\b(?:let's dive|here's the thing|at its core|in essence|the result\?|what this means:)", "opener tic"),
    (r"\b(?:delve|tapestry|testament to|underscore[sd]?|pivotal|realm|crucial|multifaceted)\b", "tic word"),
    (r"\b(?:truly|genuinely|remarkably|incredibly|undeniably|arguably)\b", "hedged intensifier"),
    (r"\bnot\s+only\b[^.]{0,60}\bbut\s+also\b", "not only / but also"),
    (r"\bI\s+(?:found|could not find|couldn't find|was unable|did not see|didn't see)\b", "search report, not a fact"),
    (r"\b(?:appears? to be|seems? to|would appear)\b", "hedge"),
]
TELL_RES = [(re.compile(p, re.I), name) for p, name in TELLS]

FIGURATIVE = re.compile(
    r"\b(?:speak(?:s|ing)?\s+for|wants?\s+to|believes?|cares?\s+about"
    r"|insists?|refuses?\s+to|remembers?|forgets?|thinks?\s+that|is\s+happy"
    r"|deserves?|suffers?|pretends?|hopes?\s+to|knows?\s+best|lives?\s+in)\b", re.I)
DASH_MAX = 5.0   # em dashes per 1,000 words

HEADING_RE = re.compile(r"<h[1-4]\b[^>]*>(.*?)</h[1-4]>|^#{1,4}\s+(.*)$", re.S | re.I | re.M)

IGNORE_RE = re.compile(r"<!--\s*prose-gate:ignore\s*-->.*?<!--\s*/prose-gate:ignore\s*-->", re.S | re.I)
HTML_PROSE = re.compile(r"<(p|li|blockquote)\b[^>]*>(.*?)</\1>", re.S | re.I)
BLOCK_END = re.compile(r"</(p|li|td|th|h[1-6]|div|blockquote|cite|span|caption|tr)>", re.I)


def drop_quoted(text, is_md):
    """Quoted material, code and reference tables are mentions, not usage."""
    text = IGNORE_RE.sub(" ", text)
    text = re.sub(r"<(script|style|pre|code)\b.*?</\1>", " ", text, flags=re.S | re.I)
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    text = re.sub(r"`[^`]*`", " ", text)
    if is_md:
        text = re.sub(r"<!--.*?-->", " ", text, flags=re.S)           # comments: invisible to readers
        text = re.sub(r"^---\n.*?\n---\n", " ", text, flags=re.S)     # frontmatter
        text = re.sub(r"^\s*>.*$", " ", text, flags=re.M)             # blockquotes
        text = re.sub(r"^\s*\|.*$", " ", text, flags=re.M)            # tables
    else:
        text = re.sub(r"<blockquote\b.*?</blockquote>", " ", text, flags=re.S | re.I)
        text = re.sub(r"<table\b.*?</table>", " ", text, flags=re.S | re.I)
    return text


def to_text(markup, is_md):
    if not is_md:
        markup = BLOCK_END.sub(". ", markup)
        markup = re.sub(r"<[^>]+>", " ", markup)
        markup = re.sub(r"&[a-z]+;|&#\d+;", " ", markup)
    else:
        markup = re.sub(r"^#{1,6}\s+.*$", " ", markup, flags=re.M)    # headings
        # A list marker is not part of the item's first sentence. Left in place
        # it sits between one item's full stop and the next item's capital, so
        # a whole list read as one sentence and a single passive item counted
        # as a quarter of the page.
        markup = re.sub(r"^[ \t]*(?:[-*]|\d+\.)[ \t]+", "", markup, flags=re.M)
        markup = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", markup)
        # Emphasis markers sit at a word's edge. An underscore inside a word is
        # part of it: stripping it turned OBLIGATION_SURVEY.md into a name that
        # the jargon check then flagged.
        markup = re.sub(r"(?<!\w)[*_]{1,2}|[*_]{1,2}(?!\w)", "", markup)
    return markup


def prose_blocks(markup, is_md):
    """Paragraph text only - what the sentence-length rules apply to."""
    if is_md:
        # A list item is its marker line plus any indented continuation lines.
        # Dropping only the first line left the wrapped remainder to be read as
        # a sentence fragment and merged into its neighbours, which is how a
        # numbered reading list measured as one 118-word sentence.
        body = re.sub(r"^[ \t]*(?:[-*]|\d+\.)[ \t]+.*(?:\n[ \t]+\S.*)*", " ",
                      markup, flags=re.M)
        return to_text(body, True)
    blocks = [m.group(2) for m in HTML_PROSE.finditer(markup)]
    return to_text(" ".join(blocks), False) if blocks else None


def sentences(text):
    text = re.sub(r"\s+", " ", text or "")
    # A closing quotation mark may sit between the full stop and the space.
    # Without allowing for it, a sentence ending inside a quote merged with
    # the next one and a two-sentence line measured as forty-four words.
    parts = re.split(r"(?<=[.!?:])[\"”’]?\s+(?=[A-Z“\"])", text)
    return [p.strip() for p in parts if len(p.split()) >= 4]


OWNS = set()


def report(path):
    with open(path, encoding="utf-8") as fh:
        raw = fh.read()
    is_md = path.lower().endswith((".md", ".markdown"))
    cleaned = drop_quoted(raw, is_md)

    text = to_text(cleaned, is_md)
    sents = sentences(text)
    len_sents = sentences(prose_blocks(cleaned, is_md)) or sents
    if not sents:
        print(f"{path}: no prose found")
        return True

    n_words = len(text.split())
    passive = [s for s in sents if is_passive(s)]
    long_s = [s for s in len_sents if len(s.split()) > LONG_SENTENCE_WORDS]
    mean_len = sum(len(s.split()) for s in len_sents) / len(len_sents)
    abstract = [m.group(0).lower() for m in ABSTRACT_RE.finditer(text)
                if m.group(0).lower().rstrip("s") not in EXEMPT]
    banned = [m.group(0) for m in BANNED_RE.finditer(text)
              if m.group(0).lower() not in OWNS]
    jargon = sorted({m.group(0) for m in JARGON_RE.finditer(text)
                     if is_jargon(m.group(0))})
    tells = [(name, m.group(0).strip())
             for rx, name in TELL_RES for m in rx.finditer(text)]
    # " - " and " -- " count only between words; at a line start either is a
    # list marker. Markdown writers type " -- " for an em dash, and a gate that
    # counted only the real character passed documents carrying fifteen per
    # thousand words.
    dashes = text.count("\u2014") + len(re.findall(r"(?<=\S) --? (?=\S)", text))
    figurative = [m.group(0).strip() for m in FIGURATIVE.finditer(text)]
    headings = [to_text(m.group(1) or m.group(2) or "", is_md).strip()
                for m in HEADING_RE.finditer(cleaned)]
    heading_jargon = sorted({w for h in headings for w in JARGON_RE.findall(h)
                             if is_jargon(w)})

    passive_pct = len(passive) / len(sents) * 100
    long_pct = len(long_s) / len(len_sents) * 100
    density = len(abstract) / n_words * 1000

    checks = [
        ("passive voice", f"{passive_pct:.0f}%", f"<={PASSIVE_MAX:.0f}%", passive_pct <= PASSIVE_MAX),
        ("mean sentence", f"{mean_len:.1f}w", f"<={MEAN_LEN_MAX:.0f}w", mean_len <= MEAN_LEN_MAX),
        ("over 25 words", f"{long_pct:.0f}%", f"<={LONG_SENTENCE_MAX:.0f}%", long_pct <= LONG_SENTENCE_MAX),
        ("abstraction", f"{density:.1f}/1k", f"<={ABSTRACTION_MAX:.0f}", density <= ABSTRACTION_MAX),
        ("banned words", str(len(banned)), "0", not banned),
        ("insider terms", str(len(jargon)), "0", not jargon),
        ("machine tells", str(len(tells)), "0", not tells),
        ("figurative", str(len(figurative)), "0", not figurative),
        ("em dashes", f"{dashes / n_words * 1000:.1f}/1k", f"<={DASH_MAX:.0f}", dashes / n_words * 1000 <= DASH_MAX),
    ]

    print(f"\n{path}\n{len(sents)} sentences ({len(len_sents)} in prose), {n_words} words")
    print("-" * 58)
    for name, got, want, ok in checks:
        print(f"  {'ok  ' if ok else 'FAIL'}  {name:<15} {got:>9}   target {want}")

    if passive:
        print(f"\n  passive ({len(passive)}) - over-counts, verify by hand:")
        for s in passive[:6]:
            print(f"    - {s[:94]}")
    if long_s:
        print(f"\n  over {LONG_SENTENCE_WORDS} words ({len(long_s)}):")
        for s in sorted(long_s, key=lambda x: -len(x.split()))[:6]:
            print(f"    - {len(s.split()):>2}w  {s[:88]}")
    if banned:
        print(f"\n  banned: {', '.join(sorted({w.lower() for w in banned}))}")
    if tells:
        print(f"\n  machine tells ({len(tells)}) - say the fact instead:")
        for name, snip in tells[:10]:
            print(f"    - [{name}] {snip[:80]}")
    if figurative:
        print(f"\n  figurative ({len(figurative)}) - systems do not have intentions:")
        print("    " + ", ".join(sorted(set(figurative))))
    if jargon:
        print(f"\n  insider terms ({len(jargon)}) - replace, define in six words, or cut:")
        print("    " + ", ".join(jargon[:20]))
    if heading_jargon:
        print(f"\n  IN HEADINGS - a heading is the one line everyone reads:")
        print("    " + ", ".join(heading_jargon))
    if density > ABSTRACTION_MAX:
        top = Counter(abstract).most_common(8)
        print(f"\n  commonest abstract nouns: {', '.join(f'{w} x{n}' for w, n in top)}")

    return all(ok for *_, ok in checks)


def load_vocabulary(argv):
    """Terms this document's readers already own, so the gate stops flagging them.

    Declared with --owns TERM,TERM or in reader-vocabulary.txt beside this script.
    Declaring one is a claim about your audience. Make it deliberately.
    """
    owns = set()
    default = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           "reader-vocabulary.txt")
    if os.path.exists(default):
        with open(default, encoding="utf-8") as fh:
            owns |= {ln.split("#")[0].strip().lower()
                     for ln in fh if ln.split("#")[0].strip()}
    rest = []
    it = iter(argv)
    for a in it:
        if a == "--owns":
            owns |= {t.strip().lower() for t in next(it, "").split(",") if t.strip()}
        else:
            rest.append(a)
    return owns, rest


if __name__ == "__main__":
    OWNS, files = load_vocabulary(sys.argv[1:])
    if not files:
        sys.exit(__doc__)
    sys.exit(0 if all(report(p) for p in files) else 1)
