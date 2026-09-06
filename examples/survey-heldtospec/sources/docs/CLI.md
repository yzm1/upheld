# Quivra CLI Reference

Quivra provides a robust command-line interface (CLI) to run validation pipelines, manage data contracts, and analyze data quality.

## Usage

```bash
quivra [command] [options]
```

## Global Options

These options apply to the default pipeline execution mode. Subcommands define
their own options; use `quivra <command> --help` for those.

### Execution Control

| Option | Description |
|--------|-------------|
| `-c, --config <file>` | Path to a YAML config. Repeat the option to merge configs in order. |
| `--out <path>` | Output file path; output goes to stdout when omitted. |
| `--stream <path>` | Stream execution results to a Parquet file. |
| `--format <fmt>` | `table` (default), `markdown`, `json`, `csv`, `parquet`, `yaml`, or `junit`. Parquet requires `--out`. |
| `--validate`, `--dry-run` | Validate the resolved config and its data references without executing metrics. |
| `--validate-config` | Validate syntax and schema only, without loading data. |
| `--show-resolved` | Print the merged config after inheritance/includes and exit. |
| `--plan` | Build and print an execution plan without running analysis. |
| `--no-cache` | Disable file caching for this process. |
| `--timeout <sec>` | Global pipeline timeout in seconds. Cooperative: checked between tasks, slices and columns, so a run can overshoot by the duration of one such unit. Exits `8`. |
| `--profile-execution` | Record Python `cProfile` data for the run. |
| `--schema-cache-path <dir>` | Use a specific directory for inferred-schema caching. |
| `--parallel` | Enable process-based parallel analysis work. |
| `-j, --workers <n>` | Worker count; defaults to 1. |
| `--degradation-mode <mode>` | `strict` or `allow_partial`; overrides the config policy. |
| `--retry-attempts <n>` | Enable remote-source retries with this many attempts. |
| `--retry-delay <sec>` | Enable retries with this initial delay. |
| `--health-port <port>` | Start the health server on this port. |
| `--explain` | Print each source's logical Polars plan. |
| `--explain-optimized` | Print each source's optimized Polars plan. |
| `--polars-threads <n>` | Set `POLARS_MAX_THREADS` before execution. |
| `--streaming` | Request Polars streaming execution where supported. Results can differ from in-memory execution in the last bits of a float; see PERFORMANCE.md. |
| `--profile-timing` | Include task and source timing details. |
| `--progress` | Display slice-evaluation progress on stderr. Suppressed by `--quiet`. |
| `--no-batch-metrics` | Disable metric batching/vertical fusion. |

### Data Sampling

| Option | Description |
|--------|-------------|
| `--sample` | Enable sampling. |
| `--sample-strategy <strategy>` | `head` (default), `tail`, `random`, `stratified`, or `auto`. |
| `--sample-size <n>` | Rows to sample; defaults to 1000. |
| `--sample-seed <n>` | Random seed; defaults to 42. |

### Logging

| Option | Description |
|--------|-------------|
| `-v`, `--verbose` | Increase verbosity; repeat up to `-vvv`. |
| `-q`, `--quiet` | Suppress non-error console output. |
| `--log-level <level>` | `DEBUG`, `INFO`, `WARNING`, `ERROR`, or `CRITICAL`. |
| `--log-format <format>` | `text` or structured `json`. |
| `--redact-secrets` / `--no-redact-secrets` | Enable or disable log redaction; enabled by default. |

### History and Trends

| Option | Description |
|--------|-------------|
| `--store-results` | Store this run in the local history database. |
| `--db-path <path>` | Override the history database path. |
| `--compare-to-baseline` | Report values against previous runs. |
| `--baseline-runs <n>` | Number of previous runs in the baseline. |
| `--baseline-tolerance <pct>` | Fail when deviation exceeds this percentage. |

## Utility Options

| Option | Description |
|--------|-------------|
| `--list-metrics` | List all built-in and registered metrics, including parameters, input shape, and capabilities. |
| `--build-config [path]` | Launch the interactive config builder. |
| `--migrate-config <path>` | Legacy spelling for `quivra migrate config <path>`. |
| `--version` | Print the installed version. |
| `--install-completion` | Install completion for the selected/current shell. |
| `--show-completion` | Print a completion script. |
| `--completion-shell <shell>` | Select `bash`, `zsh`, or `fish`. |

## Subcommands

| Command | Purpose | Representative usage |
|---------|---------|----------------------|
| `init` | Create a config interactively or from a template. | `quivra init --non-interactive --template basic -o quivra.yaml` |
| `contract` | Lint, initialize, verify, or document data contracts. | `quivra contract verify contract.yaml data.parquet` |
| `watch` | Learn baselines, inspect status, or detect anomalies. | `quivra watch learn --history-dir .quivra/runs` |
| `lineage` | Render lineage, calculate impact/dependencies, or validate the graph. | `quivra lineage show -c config.yaml --format mermaid` |
| `generate` | Generate synthetic data from one or more configs. | `quivra generate -c config.yaml --rows 1000` |
| `diff` | Compare schema and aggregate statistics. With `--exit-code`: `0` identical, `1` differences found, `2` a dataset could not be read. | `quivra diff old.parquet new.parquet --exit-code` |
| `profile` | Profile a dataset. | `quivra profile data.parquet --format json` |
| `infer` | Infer a validation config from a dataset. | `quivra infer data.csv -o config.yaml` |
| `migrate` | Upgrade Quivra configs or convert Great Expectations suites. | `quivra migrate config old.yaml --dry-run` |
| `plugins` | List loaded plugins or raw entry points. | `quivra plugins list` |
| `create-plugin` | Scaffold an external plugin project. | `quivra create-plugin quivra-example` |
| `export-dbt` | Convert Quivra checks to dbt `schema.yml`. | `quivra export-dbt -c config.yaml -o schema.yml` |
| `doctor` | Diagnose the environment and optionally a config. | `quivra doctor -c config.yaml` |

The `contract` command provides `lint`, `init`, `verify`, and `docs`; `watch`
provides `learn`, `status`, and `run`; `lineage` provides `show`, `impact`,
`deps`, and `validate`; and `migrate` provides `config` and `gx`.

## Output Formats

- **Table** (default): Rich terminal table.
- **Markdown**: GitHub-flavored Markdown table.
- **JSON, CSV, and Parquet**: Machine-readable tabular results.
- **YAML**: Structured validation report.
- **JUnit**: XML for CI test-report consumers.

### Example: CI Integration

To generate a JUnit report for your CI pipeline:

```bash
quivra -c config.yaml --format junit --out test-results.xml
```

## Exit Codes

| Code | Meaning |
|---:|---|
| `0` | All checks passed. |
| `1` | Configuration error. |
| `2` | Data loading error — **or** an argument-parsing error (see below). |
| `3` | Quality threshold or enforced baseline-tolerance violation. |
| `4` | Metric execution error. |
| `5` | Unexpected internal error. |
| `6` | Partial success under degradation mode. |
| `7` | Plugin loading or registration error. |
| `8` | Timeout. |
| `9` | Cancellation by the user or a signal. |

Treat every nonzero value as a failed quality gate unless a caller explicitly
handles partial success (`6`).

**`2` is not unambiguous.** `argparse` exits `2` for an invalid invocation, which
is the long-standing convention for a usage error, so an unknown flag, an unknown
subcommand or a bad flag value all exit `2` — the same code as a data-loading
failure:

| Invocation | Exit | Why |
|---|---:|---|
| `quivra --no-such-flag` | `2` | usage — unknown flag |
| `quivra --timeout notanumber` | `2` | usage — bad flag value |
| `quivra -c config.yaml` with a missing source file | `2` | data loading |

A caller that routes `2` to whoever owns the data will misattribute a typo in the
command line. The two are distinguishable on stderr: a usage error is a single
`quivra: error: ...` line from the argument parser and produces no run log,
while a data error is logged and reported through the normal result path. A
pipeline that needs to tell them apart reliably should validate its own
invocation before calling `quivra`.

Quivra keeps `2` for usage errors rather than remapping them onto
`1` (Configuration error), because deviating from the convention would surprise
every caller that already relies on it. Remapping is a defensible alternative and
is recorded as a maintainer decision in the audit log rather than taken here.

The result also preserves the pre-action decision as `validation_exit_code`.
For example, checks may pass with `validation_exit_code == 0` while a failed
configured output marked `required: true` makes the overall process exit with
plugin error (`7`). Optional output failures are recorded without changing the
overall exit.

---

## Environment Variable Integration

Some CLI flags set process-wide execution controls. See
[ENV_REFERENCE.md](ENV_REFERENCE.md) for the environment variables that can
also be configured before startup.

| CLI Flag | Environment Variable | Effect |
|----------|---------------------|--------|
| `--no-cache` | Runtime flag and `QUIVRA_FILE_CACHE_SIZE=0` | Clears and bypasses caches in this process; child processes inherit the zero cache size |
| `--polars-threads <n>` | `POLARS_MAX_THREADS=<n>` | Limits Polars thread pool |
| `--streaming` | (internal) | Enables streaming execution mode |

### Setting Variables via CLI

For environment variables without dedicated CLI flags, use shell syntax:

```bash
# Set streaming batch size for this run only
QUIVRA_JSON_STREAMING_BATCH_SIZE=50000 quivra -c config.yaml

# Or export for the session
export QUIVRA_FILE_CACHE_SIZE=0
quivra -c config.yaml
```

---

## Shell Completion

Quivra provides command-line completion for bash, zsh, and fish shells to speed up your workflow.

### Installation

**Automatic (Recommended):**
```bash
quivra --install-completion
```

This will:
- Detect your current shell (bash, zsh, or fish)
- Install the completion script to the appropriate location
- Provide instructions for activating completion

**Manual Installation:**

1. Generate the completion script for your shell:
   ```bash
   quivra --show-completion
   ```

2. Save it to the appropriate location:

   **Bash:**
   ```bash
   quivra --show-completion > ~/.local/share/bash-completion/completions/quivra
   source ~/.local/share/bash-completion/completions/quivra
   ```
   
   **Zsh:**
   ```bash
   quivra --show-completion > ~/.zsh/completions/_quivra
   # Add to ~/.zshrc:
   fpath=(~/.zsh/completions $fpath)
   autoload -Uz compinit && compinit
   ```
   
   **Fish:**
   ```bash
   quivra --show-completion > ~/.config/fish/completions/quivra.fish
   ```

3. Restart your shell or source your configuration file.

### Features

Once enabled, shell completion provides:

- **Command completion**: Press `Tab` after `quivra ` to see available commands
  ```bash
  quivra <Tab>
  # Suggests: init, contract, watch, lineage, generate, diff, profile, ...
  ```

- **Option completion**: Press `Tab` after `--` to see available flags
  ```bash
  quivra --<Tab>
  # Suggests: --config, --format, --out, --verbose, --help, ...
  ```

- **Subcommand completion**: Works with all subcommands
  ```bash
  quivra contract <Tab>
  # Suggests: docs, init, lint, verify
  ```

### Troubleshooting

**Completion not working after installation:**

1. Make sure you've restarted your shell or sourced your rc file:
   ```bash
   # Bash
   source ~/.bashrc
   
   # Zsh
   source ~/.zshrc
   
   # Fish (automatic)
   ```

2. Verify the completion script was installed:
   ```bash
   # Bash
   ls ~/.local/share/bash-completion/completions/quivra
   
   # Zsh
   ls ~/.zsh/completions/_quivra
   
   # Fish
   ls ~/.config/fish/completions/quivra.fish
   ```

3. For zsh, ensure completion is enabled in your `~/.zshrc`:
   ```bash
   autoload -Uz compinit && compinit
   ```

**Permission errors during installation:**

If `--install-completion` fails due to permission errors, use manual installation or create the directory first:
```bash
mkdir -p ~/.local/share/bash-completion/completions  # Bash
mkdir -p ~/.zsh/completions                           # Zsh
mkdir -p ~/.config/fish/completions                   # Fish
```

---

## See Also

- [Environment Variables Reference](ENV_REFERENCE.md) - All environment variables
- [Configuration Reference](CONFIG_REFERENCE.md) - YAML configuration options
- [Performance Guide](PERFORMANCE.md) - Performance tuning tips
