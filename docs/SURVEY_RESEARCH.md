# Build the survey around claim discovery and evidence review

Readers are engineers deciding how Upheld should discover promises worth checking. They know Git and tests; the research methods below need no specialist background.

**Use a hybrid workflow: fixed rules preserve sources and run checks; an optional generative language model interprets prose and proposes questions.** Let users configure their existing agent CLI before the first model-assisted survey. Keep a useful local mode that requires no generative model. “Non-generative” below means the model does not compose or rewrite claims.

This research supports S01's design, as of 6 September 2026. It does not establish a winning product through a common benchmark. Published studies test different tasks and corpora; vendor documentation establishes advertised behavior. No comparative survey trial or provider integration ran during this work. At this research stage the scanner remained unbuilt. The later [S02 prototype](SURVEY_PROTOTYPE.md) now supports bounded source review; comparative quality trials remain open.

## Literature review supplies the main comparison

A survey must discover claims the reader did not know to ask about. It must then preserve their meaning and find evidence that could change a decision. Those needs also occur in scientific literature review, public fact-checking, and qualitative research.

The search covered claim mining, scientific evidence retrieval, systematic review, interview analysis, and software checks. Primary papers and official product documentation below supply the evidence. This technical review selected methods by relevance. It has no registered search protocol or screened-paper denominator, so it cannot establish exhaustive coverage.

The comparison favors methods with inspectable evidence, explicit uncertainty, and a way to measure omissions. Product popularity and cross-paper leaderboard scores do not determine the recommendation. Each “borrow” below proposes a transfer to Upheld. These transfers remain untested.

## Discovering a claim and checking it need different methods

| Need | Primary source and evidence type | Method | Borrow | Transfer limit |
|---|---|---|---|---|
| Identify statements worth review | [ClaimBuster, KDD 2017](https://www.kdd.org/kdd2017/papers/view/toward-automated-fact-checking-detecting-check-worthy-factual-claims-by-cla), research | Supervised language features and claim ranking | Rank review candidates using explicit relevance criteria | Political check-worthiness labels do not define consequential software promises; ranking does not establish truth |
| Extract faithful standalone claims | [Claimify, ACL 2025](https://aclanthology.org/2025.acl-long.348/), research | language model selection, ambiguity handling, and decomposition | Check source meaning, omitted content, and whether each claim can stand alone | Its factual-content filter could discard requirements and unresolved choices; Upheld must retain those separately |
| Preserve qualifications and relationships | [SciClaim, EMNLP 2021](https://aclanthology.org/2021.emnlp-main.381/), dataset and learned extractor | Transformer models identify entities, relations, and modifying attributes | Keep conditions, comparison groups, strength, and evidence with the claim | A trained scientific extractor needs new labels and evaluation for another domain |
| Resolve references without changing meaning | [Decontextualization, TACL 2021](https://aclanthology.org/2021.tacl-1.27/), research | Rewrite a sentence using its surrounding context | Store the original span beside a proposed standalone version | Missing context must produce an unresolved reference, not a guess |
| Retrieve support and refutation | [SciFact, EMNLP 2020](https://aclanthology.org/2020.emnlp-main.609/), dataset and models | Retrieve abstracts, classify evidence, select rationale spans | Separate evidence retrieval from the verdict; retain supporting spans | The benchmark starts with claims supplied by experts; it cannot establish discovery coverage |
| Check claims against a larger evidence pool | [SciFact-Open, Findings 2022](https://aclanthology.org/2022.findings-emnlp.347/), research | Pool retrieval systems and review retrieved evidence | Preserve partial support and the scope of each result | The study reports degradation on a larger corpus and difficult special-case support; absent retrieval is weak evidence of absence |
| Break verification into answerable questions | [AVeriTeC, NeurIPS 2023](https://papers.nips.cc/paper_files/paper/2023/hash/cd86a30526cd1aff61d6f89f107634e4-Abstract-Datasets_and_Benchmarks.html), benchmark | Web evidence expressed through questions, answers, and justifications | Attach a next question and dated evidence to each claim | Real-world fact-checking still assumes a supplied claim; control evidence dates to avoid hindsight |

Claimify is the closest starting point for extracting claims from prose. Its ambiguity handling matters because a fluent rewrite can silently strengthen the source. Its evaluation also separates faithfulness from coverage. Upheld should preserve ambiguous passages in the review queue, even when the model cannot extract a claim safely.

SciClaim broadens the unit of review beyond a sentence. A claim includes relationships and qualifications. For Upheld, the corresponding fields include subject, version, conditions, quantifiers, exceptions, and whether the source describes behavior or requires it. This design inference from scientific extraction needs a cross-domain trial.

## Evidence search should challenge the claim and preserve its context

| Need | Primary source and evidence type | Method | Borrow | Transfer limit |
|---|---|---|---|---|
| Search and synthesize across papers | [OpenScholar, Nature 2026](https://www.nature.com/articles/s41586-025-10072-4), peer-reviewed system | Retrieval, reranking, language model drafting, further retrieval, and citation checks | Search in several ways, inspect missing evidence, verify citations against retrieved text | Its paper corpus and question-answer benchmark do not demonstrate complete claim discovery |
| Ask questions of a document collection | [PaperQA2 repository](https://github.com/future-house/paper-qa), implementation; [2024 paper](https://arxiv.org/abs/2409.13740), preprint | Retrieval plus language model evidence synthesis; a contradiction-search setting | Make contradiction search an explicit operation over a bounded collection | Agent results require review; its literature benchmarks do not establish promise correctness |
| Inspect the role of citations | [scite Smart Citations](https://scite.ai/blog/smart-citations-rankings), product documentation | Classify citing statements as supporting, contrasting, or mentioning | Keep the evidence relationship alongside the source | Citation role and citation count do not establish truth or independent replication |
| Check factual support at small units | [FActScore, EMNLP 2023](https://aclanthology.org/2023.emnlp-main.741/), research | Split generated prose into atomic facts and assess support | Audit unsupported additions in a model's output | Factual precision does not measure missed claims; splitting claims can inflate counts |
| Handle mixtures of factual and other content | [VeriScore, Findings 2024](https://aclanthology.org/2024.findings-emnlp.552/), research | Extract verifiable claims, then retrieve evidence | Distinguish factual assertions from content requiring another review route | Unverifiable content can still contain an important requirement or decision |
| Detect errors introduced by combining true facts | [Merging Facts, Crafting Fallacies, Findings ACL 2024](https://aclanthology.org/2024.findings-acl.160/), research | Evaluate contradictions hidden by separately scored atomic claims | Keep parent claims, entity identity, and relationships between extracted parts | Individually supported fragments cannot automatically confirm the combined assertion |

OpenScholar provides evidence that retrieval and citation checks can improve a language-model workflow on its tested literature tasks. Borrow that workflow before considering a custom trained model or a large hosted corpus. Start with the user's bounded set of sources and explicit external searches.

Search for both supporting and conflicting evidence. Keep “partial support,” “mentions,” “unresolved,” and “no evidence retrieved” distinct. A result may concern another version, population, condition, or meaning of the same term. Related vocabulary alone cannot resolve that mismatch.

Record evidence dependencies when known. Repeated quotations of one source are not independent observations. A source can report a claim accurately while the underlying claim remains uncertain. For Upheld, a document proves that someone stated a promise; an execution may test its behavior; a maintainer decides whether to adopt it.

For a set of papers, start with the claim's entities, relation, conditions, and alternate terms. Search those combinations and explicit counterclaims. Follow relevant citations, deduplicate versions, and inspect the full passage with its surrounding methods and limits. Preserve abstract-only or unavailable full text as a limit. Distinguish reported measurements from what the authors infer.

For a repository, the same process follows source links, symbols, and relevant history instead of paper citations. Running code adds another evidence route. This transfer keeps the claim-and-evidence workflow general while leaving each source adapter responsible for its own limits.

## Review tools explain how to spend human attention

| Need | Primary source and evidence type | Method | Borrow | Transfer limit |
|---|---|---|---|---|
| Screen and extract consistently | [Elicit systematic-review workflow](https://elicit.com/blog/systematic-review/), product documentation | Criteria, screening, extraction fields, and AI assistance | Define the review question and fields before accepting outputs | Product workflow is not evidence of Upheld accuracy; automated decisions need an audit sample |
| Resolve reviewer disagreement | [Covidence screening conflicts](https://support.covidence.org/help/resolving-conflicts-at-screening-stage), product documentation | Independent human decisions and conflict resolution | Retain decisions, disagreement, exclusion reasons, and the final reviewer | Consensus can still be wrong; source evidence remains necessary |
| Prioritize a large queue without a generative language model | [ASReview models](https://asreview.readthedocs.io/en/latest/lab/models.html), implementation documentation | Text features and classifiers such as TF-IDF with Naive Bayes or SVM; active learning | Learn relevance from reviewer labels and mix priority review with random sampling | It ranks records; it does not extract every claim or verify its meaning |
| Decide when to stop screening | [SAFE procedure, Systematic Reviews 2024](https://link.springer.com/article/10.1186/s13643-024-02502-7), research | Staged active learning and quality checks | Audit the unreviewed remainder and state why the review stopped | A stopping heuristic does not certify completeness on an unfamiliar corpus |
| Connect interview or survey themes to observations | [Dovetail overview](https://docs.dovetail.com/help/what-is-dovetail), product documentation | Source highlights, tags, themes, and shared findings with AI assistance | Let readers inspect the passage behind a finding | A theme summarizes responses; frequency does not establish truth or importance |

ASReview answers part of the non-generative question: classic text features and reviewer feedback can improve queue order. This does not solve open-ended interpretation. A useful non-generative survey can still preserve exact passages, expose explicit declarations, group duplicates, search terms, and guide human review.

The queue needs deliberate exploration. If it only follows the model's highest scores, it cannot reveal what that model systematically misses. Reserve review time for randomly sampled lower-ranked material and for source types that contributed few candidates. Record sampling rules before claiming a miss rate.

## Software tools add evidence mechanisms after discovery

| Mechanism | Primary source | Model dependence | Appropriate role and limit |
|---|---|---|---|
| Source rules and data flow | [CodeQL](https://codeql.github.com/docs/writing-codeql-queries/about-data-flow-analysis/) | Fixed queries | Check modeled behaviors in supported languages; silence says little about unmodeled promises |
| Language models plus static analysis | [IRIS, ICLR 2025](https://proceedings.iclr.cc/paper_files/paper/2025/hash/582d4e27fa24168f3af1f4582655034b-Abstract-Conference.html) | language model-assisted analysis | Shows a hybrid method for security analysis; its Java vulnerability study does not establish survey yield |
| Requirement traceability | [StrictDoc](https://strictdoc.readthedocs.io/en/stable/stable/docs/strictdoc_01_user_guide-TRACE.html) | No generative model required | Keep stable relationships between requirements and source; a link does not prove behavior |
| Observed invariants | [Daikon](https://plse.cs.washington.edu/daikon/) | Dynamic inference | Propose patterns from executions; likely invariants need review before becoming obligations |
| Schema-derived API tests | [Schemathesis](https://schemathesis.readthedocs.io/en/latest/explanations/data-generation/) | Test generation from schemas | Exercise declared API properties; undocumented intent remains outside the schema |
| Symbolic counterexamples | [CrossHair limitations](https://crosshair.readthedocs.io/en/latest/limitations.html) | Symbolic execution | Challenge supported contracts within limits; no counterexample does not guarantee correctness |
| Mutation testing | [Stryker FAQ](https://stryker-mutator.io/docs/General/faq/) | Seeded changes | Investigate whether a defense notices faults; translate result semantics carefully |

Stryker's timeout treatment illustrates why an adapter cannot copy an external score into Upheld's evidence grade. Upheld's [method](METHOD.md) requires its own distinctions between detection and inconclusive execution. A useful probe can resolve a survey question without grading a defense.

## Keep a generic claim record before creating Upheld records

The candidate inbox below is a proposed survey design. It does not change the accepted record schema. Only reviewed choices enter the existing register.

| Candidate information | Why it must survive review |
|---|---|
| Source identity, version, exact span, nearby context, and extraction method | A reader must recover what the source actually said |
| Original passage and proposed standalone claim | Rewriting must not hide added certainty or lost exceptions |
| Subject, conditions, negation, quantities, time, and modality | A factual statement, obligation, prediction, and open choice need different treatment |
| Parent claim and links between extracted parts | Splitting must not change relationships or multiply outcome credit |
| Evidence spans, relationship, scope mismatch, and known dependencies | A citation alone cannot establish support |
| Uncertainty, next question, candidate probe, and reviewer decision | The queue must remain useful when evidence is missing |
| Source coverage and explicit omissions | Unsupported formats and unprocessed passages must remain visible |

Tables and figures need explicit treatment. Research on [claims in heterogeneous scientific tables](https://www.vldb.org/2025/Workshops/VLDB-Workshops-2025/TaDA/TaDA25_16.pdf) shows why text alone can lose essential context. Initially record unsupported material and provide a manual route. Do not silently treat a document as fully surveyed when its tables or images were skipped.

## Compare approaches before paying for more machinery

The proposed design remains provisional. E01 must register the actual targets, budgets, sampling, and decision rules before experiments. The existing two-project milestone establishes feasibility; it cannot rank all providers or establish broad recall.

| Comparison | What it can establish |
|---|---|
| Human review with ordinary search | The baseline cost and findings from the same available sources |
| Structured extraction and review without a generative model | Value from source inventory, explicit rules, and queue design |
| User's agent CLI with a direct survey prompt | What the existing agent can already achieve |
| Hybrid workflow using the same agent and model | Added value from source accounting, faithful extraction, evidence search, and review controls |

Use fresh, comparable components or independent reviewers to avoid learning the answers from another arm. Keep source access and human budgets matched. Have outcome reviewers judge evidence without knowing which method produced it where feasible. Record model, agent version, instructions, costs, failures, and available tools. Mark an unavailable provider as unsupported and exclude it from score comparisons.

Evaluate the parts separately. For extraction, measure source faithfulness, preserved qualifications, and missed claims on independently annotated passages. Include non-software literature passages so the test does not reward software vocabulary alone. Inspect dataset licenses before redistributing examples.

For retrieval, measure whether cited spans support the exact claim and whether the system found known counterevidence. For the end-to-end survey, use the [outcome and attention measures](SURVEY_TOOL.md). Sample the unreviewed remainder; do not infer global recall from accepted candidates.

Advance a language model stage only when its added useful findings or saved review time justify its error and operating costs. Keep the non-generative path if the model fails that comparison. The [backend proposal](SURVEY_BACKENDS.md) makes this choice testable without requiring an Upheld model account.

## S01 completes the design; the trials remain open

S01 now defines the survey objective, outcome categories, attention measures, and omission checks. The milestone uses those definitions. E01 must still register concrete experiments, and the [S02 prototype](SURVEY_PROTOTYPE.md) still needs independent quality trials.

On 6 September 2026, `python tools/check_docs.py` passed the prose, schema, task, and local-link checks for this change. It also passed the supplied prose-check tests. These checks assess the written artifacts; they do not demonstrate survey quality or working backend adapters.
