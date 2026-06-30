# vector-index-sizer

**Tool Manual.** Estimate vector index footprint and flag capacity risks from planning notes.

## Synopsis

Vector store cost and memory can surprise teams. This CLI checks sizing plans for missing dimensions and large footprints.

## Description

`vector-index-sizer` accepts vector index sizing notes or config in text, JSON, JSONL, or CSV form.

## Examples

```bash
python -m pip install -e ".[dev]"
vector-index-sizer examples/sample.txt
vector-index-sizer examples/sample.txt --json --fail-on medium
```

## Rules

| Rule | Severity | Meaning |
|---|---:|---|
| `huge-document-count` | high | document count is very large |
| `large-dimensions` | medium | embedding dimension is large |
| `no-compression` | low | compression is not configured |

## Exit Status

```bash
ruff check .
pytest
python -m vector_index_sizer --help
```

License: MIT

### Example Input

```text
documents 10000000 dimensions 3072 replicas 3 compression none
```

### Architecture

`cli.py` reads files, `core.py` evaluates records, and `rules.py` keeps the vector-index-sizer policy surface explicit.
