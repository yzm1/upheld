# Use Upheld with your existing agent

Readers are engineers trying the Upheld guide. Version 0.2.0 is a packaged prototype dated 9 September 2026. It helps an agent work from a software obligation to a recommended defense plan, the defenses that actually exist, the evidence behind them, and the gaps that still need attention.

**Choose a client, export a fresh folder, and invoke the guide explicitly.** Package checks pass locally; actual loading and explicit-only behavior in installed clients remain untested under S14. The guide supplies instructions and references. Your agent's permissions still govern its tools.

The guide now supports both entry paths. You can use it while specifying a new application, before defenses exist, or while auditing an existing codebase. In either case, advice, current implementation, evidence, and human acceptance stay separate.

## Export the package for your client

From an Upheld checkout, use Python 3.11 or later and Git with the pinned method source commit available. Export uses the Python standard library and reads the named commit with Git. A shallow checkout may need that history fetched first. Name the new output folder `upheld`.

```bash
python tools/package_upheld_skill.py --client codex --output /tmp/upheld-codex/upheld
python tools/package_upheld_skill.py --verify /tmp/upheld-codex/upheld
```

Choose `claude` or `copilot` with a fresh output path for those clients. The exporter adds the appropriate invocation controls. It copies the core, local references, license, notices, and a file manifest. It does not install into accounts or change an existing setup.

The verifier requires the known package files and checks their hashes. An empty file map is invalid. It does not authenticate a publisher or prove that the method is current online. The command reports `clean` with exit 0, `violated` with exit 1, or `could_not_look` with exit 2.

Keep the exported folder together; copying the entrypoint alone loses required rules.

## Install the folder only where you want it available

Move the exported folder into one selected location below. Preserve any existing installation until you have reviewed the new package; the exporter leaves existing folders untouched. Restart or reload the client, then inspect which skill it selected. Multiple copies with the same name can affect which version runs.

| Client | Documented project location | Explicit request |
|---|---|---|
| [Codex](https://learn.chatgpt.com/docs/build-skills) | `.agents/skills/upheld` | `$upheld Map these obligations to the best defense plan, current defenses, and gaps.` |
| [Claude Code](https://code.claude.com/docs/en/skills) | `.claude/skills/upheld` | `/upheld Map these obligations to the best defense plan, current defenses, and gaps.` |
| [Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills) | `.github/skills/upheld` | `/upheld Map these obligations to the best defense plan, current defenses, and gaps.` |

These locations come from official documentation checked on 7 September 2026. The exported Codex package includes both its own policy file and the other clients' explicit-only field because some directories are shared. Their actual handling still needs a live check. Do not install the unrendered `skills/upheld` source folder directly.

## Ask for the part of the assurance map you need

Useful explicit requests include:

- specify falsifiable obligations for this feature and propose a defense plan before implementation;
- discover obligations and current defenses in this component;
- recommend a defense portfolio under these latency, runtime, or infrastructure constraints;
- compare the intended plan with the defenses that exist and show the gaps;
- challenge this defense and tell me whether the evidence is strong enough to rely on;
- review this change and identify which recorded grounds or recommendations need another look.

A recommendation is advice, not proof that the mechanism exists. A current defense remains visible even when it differs from the recommendation. A passing test remains unproven until a suitable fault challenge supports it.

The skill can propose schema 0.2 records in prose when the repository schemas are available to the agent. It does not create human bindings or accepted evidence by itself.

## Keep the package tied to reviewed rules

Maintainers edit the source guide and worked example. Generate the method reference from the reviewed method rather than editing the copy:

```bash
python tools/package_upheld_skill.py --refresh-reference
python tools/package_upheld_skill.py --check
python tools/check_docs.py
python -m unittest discover -s tests -p 'test_*.py'
```

A normative method change still requires the existing rule review, a new source commit and digest in the packager, and a package version update. The 0.2.0 guide broadens the product workflow without changing method 1.4's reviewed evidence rules.

Re-export and review the package before replacing an installed copy. If a write fails partway through export, inspect the partial folder and retry into a fresh path.

The [product model](PRODUCT_MODEL.md) explains the full obligation-to-defense map. The [schema](SCHEMA.md) defines the 0.2 record split. The [self-audit](SELF_AUDIT.md) records earlier source-pin and verifier defects; the newer self-assurance example applies the broader model to Upheld itself.
