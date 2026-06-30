from __future__ import annotations

from vector_index_sizer.models import Rule

PROJECT_NAME = 'vector-index-sizer'
SUMMARY = 'Estimate vector index footprint and flag capacity risks from planning notes.'
SAMPLE_RISK = 'documents 10000000 dimensions 3072 replicas 3 compression none'
SAMPLE_CLEAN = 'documents 100000 dimensions 768 replicas 1 compression scalar'
TEXT_FIELDS = ("text", "content", "description", "summary", "body", "notes", "message")
SUBJECT_FIELDS = ("id", "name", "path", "endpoint", "service", "job", "route", "event")

RULES = (
    Rule(
        code='huge-document-count',
        severity='high',
        pattern='\\bdocuments\\s*(10000000|[2-9][0-9]{7,})\\b',
        message='document count is very large',
        recommendation='Estimate shard count, cost, and ingestion window.',
    ),
    Rule(
        code='large-dimensions',
        severity='medium',
        pattern='\\bdimensions\\s*(3072|4096|8192)\\b',
        message='embedding dimension is large',
        recommendation='Consider smaller embeddings or compression.',
    ),
    Rule(
        code='no-compression',
        severity='low',
        pattern='\\bcompression\\s*(none|missing|null)\\b',
        message='compression is not configured',
        recommendation='Evaluate quantization or scalar compression.',
    ),
)
