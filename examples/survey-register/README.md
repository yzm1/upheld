# The source review now has a canonical register

This example converts the saved heldtospec source review into Upheld schema 0.1. **It contains twelve suspected promises and no defenses.** It reuses prior judgments and supplies no new evidence.

The [register](obligations.register.json) retains each claim's source, limits, uncertainty, and next question. Its metadata records missing or excluded inputs and submitted reading notes. The [source review](../survey-heldtospec/README.md) describes the original scope.

Generate a new copy from the repository root:

```bash
python tools/survey.py register \
  --run examples/survey-heldtospec/run \
  --out /tmp/heldtospec-proposed.register.json
```

Install `requirements-docs.txt` first. Use a fresh output filename. An existing output file causes an error. [The guide](../../docs/SURVEY_REGISTER.md) explains its fields and remaining work.

The source quotations retain historical spellings. Current prose uses heldtospec. The exporter preserves quotations as evidence input.
