# Demo Structure - EARS

**Parent LLD**: ./LLD.md

## Demo Timing

- **DEMO-STRUCT-001**: The system shall structure the demo into four segments: introduction (2 min), first analysis question (8 min), engineered mistake and debugging (6 min), and wrap-up (4 min).
- **DEMO-STRUCT-002**: When the introduction segment begins, the system shall state the one-question-at-a-time principle and that it is a trainable skill.
- **DEMO-STRUCT-003**: When the first analysis question segment begins, the system shall load the surface engineering dataset and ask one question.
- **DEMO-STRUCT-004**: When the engineered mistake segment begins, the system shall present a pre-planned mistake and debug it live.
- **DEMO-STRUCT-005**: When the wrap-up segment begins, the system shall recap the principle and explain the hackathon structure.

## Demo Dataset

- **DEMO-STRUCT-010**: The system shall load the surface engineering dataset from a public URL, not a hardcoded local path.
- **DEMO-STRUCT-011**: The dataset shall be under 10MB and loadable within seconds.
- **DEMO-STRUCT-012**: The dataset shall have a clear tabular structure with understandable column names.
- **DEMO-STRUCT-013**: The dataset shall support at least two distinct analysis questions.

## Demo Reproducibility

- **DEMO-STRUCT-020**: The system shall demonstrate loading data directly from a source URL via the agent.
- **DEMO-STRUCT-021**: The demo notebook shall run cleanly from top to bottom with `uv run marimo edit demo.py`.
- **DEMO-STRUCT-022**: The demo notebook shall contain no hardcoded local file paths.

## Engineered Mistakes

- **DEMO-STRUCT-030**: When the agent suggests code or interpretation, the system shall include 2-3 pre-planned mistakes.
- **DEMO-STRUCT-031**: If the agent produces a mistake, then the system shall catch it and debug live.
- **DEMO-STRUCT-032**: The system shall think out loud during debugging, showing how domain expertise guides where to look first.
- **DEMO-STRUCT-033**: The mistakes shall be of types that are common in real analysis: statistical misinterpretation, plotting error, or assumption violation.

## Demo Scope

- **DEMO-STRUCT-040**: Where the demo runs within the 20-minute time budget, the system shall cover the first analysis question and the engineered mistake debugging.
- **DEMO-STRUCT-041**: If the demo runs longer than 20 minutes, then the system shall skip the second analysis question to stay on schedule.

## Related Documents

- [Demo LLD](./LLD.md)
