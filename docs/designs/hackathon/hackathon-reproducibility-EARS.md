# Hackathon Reproducibility - EARS

**Parent LLD**: ./LLD.md

## Data Loading

- **HACK-REPRO-001**: The system shall encourage participants to have the agent pull data directly from source URLs (e.g., `pd.read_csv("https://...")`) rather than downloading to a local file.
- **HACK-REPRO-002**: If a participant downloads data to a local file, then the system shall not allow hardcoded absolute paths (e.g., `/Users/ericmjl/data/...`).
- **HACK-REPRO-003**: Where a local cached copy is needed for performance, the system shall direct the participant to use a data version control system (e.g., DVC) rather than an arbitrary filesystem location.

## Dependency Management

- **HACK-REPRO-010**: The system shall encourage participants to use `uv run` to execute their notebooks.
- **HACK-REPRO-011**: The system shall ensure that all dependencies required by a participant's notebook are resolvable via uv.

## Notebook Structure

- **HACK-REPRO-020**: The system shall expect each participant's notebook to run top-to-bottom with `uv run marimo edit notebook.py` on another machine.
- **HACK-REPRO-021**: The system shall encourage participants to use relative paths or source URLs instead of hardcoded local paths.

## Instructor Guidance

- **HACK-REPRO-030**: During the setup walkthrough, the system shall instruct participants: "Don't download data to your machine and reference it with a hardcoded path. Have the agent pull it directly from the source URL."
- **HACK-REPRO-031**: During circulation, the system shall reinforce: "If you need a cached copy, put it in a data version control system like DVC — not just sitting in a folder on your desktop."
- **HACK-REPRO-032**: During circulation, the system shall reinforce: "Your notebook should be something someone else could run without asking you how you set it up."

## Related Documents

- [Hackathon LLD](./LLD.md)
