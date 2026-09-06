# Data Contracts

A Quivra contract records dataset ownership, consumers, schema declarations,
column constraints, and selected service-level checks in a standalone YAML
file.

## Create a contract

Generate a starting contract from a local dataset:

```bash
quivra contract init data/orders.parquet \
  --name orders \
  --output contracts/orders.yaml
```

The generated schema is a starting point; review nullability, uniqueness,
constraints, ownership, and SLAs before publishing it.

## Contract structure

```yaml
contract:
  name: orders
  version: 1.0.0
  owner:
    team: checkout
    slack: "#checkout-data"
  consumers:
    - team: finance
      use_case: revenue reporting
  schema:
    columns:
      - name: order_id
        type: Int64
        nullable: false
        unique: true
      - name: amount
        type: Float64
        nullable: false
        constraints:
          min: 0
      - name: status
        type: String
        allowed_values: [pending, paid, failed]
  sla:
    freshness:
      max_age: 24h
      timestamp_column: created_at
    completeness:
      min_rows: 100
      max_null_percentage: 0.01
  checks:
    - name: nonnegative_amount
      expr: amount >= 0
```

`max_null_percentage` is a fraction: `0.01` means one percent. Duration units
for `max_age` are `s`, `m`, `h`, and `d`.

## Validate contract syntax

```bash
quivra contract lint contracts/orders.yaml
```

Linting validates the contract model and rejects unknown or misspelled keys.
It does not load the dataset.

## Verify a dataset

```bash
quivra contract verify contracts/orders.yaml data/orders.parquet
```

Verification maps the following declarations to executable Quivra checks:

| Declaration | Enforced check |
|---|---|
| `schema.columns[].name` / `.type` | Every declared column must exist with the declared Polars dtype. |
| `nullable: false` | Null percentage must be zero for that column. |
| `unique: true` | Uniqueness percentage must be 100 for that column. |
| `allowed_values` | Count outside the allowed set must be zero. |
| `constraints.min` / `.max` | Count outside the numeric range must be zero. |
| `constraints.regex` | Regex-match percentage must be 100. |
| `sla.freshness` | `freshness_check` must pass for the timestamp column. |
| `sla.completeness.min_rows` | Row count must meet the minimum. |
| `sla.completeness.max_null_percentage` | Every declared column must meet the null limit. |
| `checks[].expr` | The expression must be true for every row. |

Ownership, consumers, descriptions, and foreign-key `references` are contract
metadata in the current verifier. A bare
`checks[].metric` also has no pass condition; use `expr` or a concrete column
constraint for a check that must gate the run.

The verification command returns the underlying pipeline exit code, including
code 3 for a constraint violation. It fails rather than reporting success if
the contract produces no executable checks.

## Generate documentation

Render a contract for a catalog or wiki:

```bash
quivra contract docs contracts/orders.yaml --output orders-contract.md
```

Omit `--output` to write Markdown to stdout.

## See also

- [CLI Reference](CLI.md#subcommands)
- [Configuration Reference](CONFIG_REFERENCE.md)
