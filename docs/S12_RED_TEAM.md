# The guide must survive copying, missing rules, and misleading evidence

Readers are engineers reviewing the S12 design. This author-led challenge took place on 7 September 2026, before we wrote the skill and packager. This reviews the design. It reports no independent agent trial or live client result.

**The initial design needed stronger controls for copied references, invocation differences, and scope loss.** The revised [design](S12_DESIGN.md) addresses these before coding. The scenarios below are deliberate review challenges, not reported incidents or scored agent runs.

| Challenge | Failure in a naive design | Required repair and check |
|---|---|---|
| Copy only the skill folder into another repository | Relative links escape into files that no longer exist. | Bundle required rules and worked notes. Build in a fresh directory and resolve every local reference inside it. |
| Change a method rule after the bundle was created | The skill keeps teaching old rules without notice. | Compare the generated reference with current source before export; seed a changed rule and require refusal. |
| Use Claude controls in Codex, or the reverse | The skill may activate automatically despite the agreed mode. | Generate client-specific controls and inspect them in tests. Keep live enforcement unverified until S14. |
| Follow-up during coding: place a Codex package in a directory also read by Copilot | Copilot ignores the Codex-only policy and may invoke the guide automatically. | Add the Claude/Copilot explicit-only field to every exported package, including Codex. Test both controls in the Codex output; live parsing remains S14 work. |
| Mark tools as allowed to make the skill read-only | A permission grant can broaden tool access. | Ship no tool grants, hooks, or runtime command wrappers. Existing host permissions govern every probe. |
| Source text asks the agent to fabricate a successful run | A quotation becomes an instruction or invented evidence. | Keep the data/instruction boundary and actual-run requirement in the core, before optional references. Challenge this in S14. |
| Full rules cannot be read | A short summary silently weakens a binding rule. | Make defense grading and formal records depend on the bundled rules. Report provisional findings if those rules are unavailable. |
| Local helper tests pass | The guide claims the production path is defended. | Ask for caller connections and assumptions. Teach the narrower Repo C lesson, retaining its untested paths. |
| A smaller task becomes a full audit | Method compliance replaces the user's deliverable. | Work within the requested scope and budget; stop at useful findings and next checks. Preserve required features and intended behavior. |
| A no-fault case gets forced into the finding template | More findings look like better performance. | Permit a bounded no-issue result, with unread portions visible. Count unnecessary follow-up work in the later trial. |
| A known example becomes the benchmark | The skill repeats the answer it was taught. | Keep Repo C and heldtospec in development; S13 supplies unseen sources and independent labels. |
| Packaging overwrites an existing install | The user loses local changes or policy. | Require a new output directory; fail before writing if it already exists. Test sentinel files remain unchanged. |
| A package hash is called verified evidence | File integrity becomes a behavior or authenticity claim. | Name the manifest's limited purpose. It checks exported bytes only. |

The prototype guide also retains a stale S11 status sentence flagged on PR #5. Correct it in this work and search current documents for other S11 status conflicts. This is a documentation finding from the actual review, separate from the design challenges above.

Proceed with these repairs. Agents may still skip rules, clients may differ, and unseen source traps may add review work. Structural tests cannot settle them; S13, E01, and S14 remain open. The [implementation record](S12_IMPLEMENTATION.md) will distinguish checks actually run from these proposed behavioral challenges.
