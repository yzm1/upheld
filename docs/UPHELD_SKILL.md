# Use Upheld with your existing agent

Readers are engineers trying the Upheld guide. Version 0.1.1 is a packaged prototype dated 7 September 2026. It helps an agent review promises and evidence within a chosen scope. It uses your existing account and tools.

**Choose a client, export a fresh folder, and invoke the guide explicitly.** Package checks pass locally; actual loading and explicit-only behavior in installed clients remain untested under S14. The guide supplies instructions and references. Your agent's permissions still govern its tools.

## Export the package for your client

From an Upheld checkout, use Python 3.11 or later and Git with the pinned source commit available. Export uses the Python standard library and reads the named commit with Git. A shallow checkout may need that history fetched first. Name the new output folder `upheld`.

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
| [Codex](https://learn.chatgpt.com/docs/build-skills) | `.agents/skills/upheld` | `$upheld Review this change against the promises it affects.` |
| [Claude Code](https://code.claude.com/docs/en/skills) | `.claude/skills/upheld` | `/upheld Review this change against the promises it affects.` |
| [Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills) | `.github/skills/upheld` | `/upheld Review this change against the promises it affects.` |

These locations come from official documentation checked on 7 September 2026. The exported Codex package includes both its own policy file and the other clients' explicit-only field because some directories are shared. Their actual handling still needs a live check. Do not install the unrendered `skills/upheld` source folder directly.

A normal review returns source-backed findings, their limits, and useful next checks. It may find no issue within the inspected scope. Missing tools remain visible. The guide can propose records in prose; it does not ship a formal exporter or create accepted evidence.

## Keep the package tied to reviewed rules

Maintainers edit the source guide and worked example. Generate the method reference from the reviewed method rather than editing the copy:

```bash
python tools/package_upheld_skill.py --refresh-reference
python tools/package_upheld_skill.py --check
python tools/check_docs.py
python -m unittest discover -s tests -p 'test_*.py'
```

A method change also requires the existing rule review, a new source commit and digest in the packager, and a package version update. Do not change pins merely to pass a failing check. Re-export and review the package before replacing an installed copy. If a write fails partway through export, inspect the partial folder and retry into a fresh path.

The [implementation record](S12_IMPLEMENTATION.md) records the checks. The [research and design](S12_DESIGN.md) and [red-team review](S12_RED_TEAM.md) explain the choices and remaining trial work.

The [self-audit](SELF_AUDIT.md) records the source-pin and verifier defects fixed in 0.1.1. Existing 0.1.0 manifests remain readable when their required files and hashes are valid.
