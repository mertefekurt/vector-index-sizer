# Vector Index Sizer

| | |
| --- | --- |
| Focus | vector search sizing |
| Command | `vector-index-sizer` |
| Inputs | text, JSON, JSONL, or CSV |
| Output | Markdown or JSON |

![Vector Index Sizer cover](assets/readme-cover.svg)

Estimate vector index footprint and flag capacity risks from planning notes. I keep it small because this kind of check is most useful when it can run beside the work, not after the work has already shipped.

## Policy surface

| Rule | Level | Why it matters |
| --- | --- | --- |
| `huge-document-count` | high | document count is very large |
| `large-dimensions` | medium | embedding dimension is large |
| `no-compression` | low | compression is not configured |

## Local run

```bash
git clone https://github.com/mertefekurt/vector-index-sizer.git
cd vector-index-sizer
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
vector-index-sizer examples/sample.txt
vector-index-sizer examples/sample.txt --json
```

## Why the sample fails

`documents 10000000 dimensions 3072 replicas 3 compression none` is intentionally shaped to hit the rules above, so it is useful as a quick smoke test after edits.
