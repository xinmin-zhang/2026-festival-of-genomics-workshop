# Hackathon - Low-Level Design

**Created**: 2026-05-31
**HLD Link**: ../../high-level-design.md

## Overview

The hackathon is the 50-minute working segment where participants apply the one-question-at-a-time principle to biology/chemistry datasets. They work individually or in small groups, using provided public datasets or their own life sciences data. The instructor supports initial setup but does not circulate extensively during this phase.

## Context

Per the HLD, datasets are biology/chemistry focused, sourced from the internet. The Festival of Genomics audience spans pharma, biotech, and academia. Participants range from working professionals to current graduate students, all sharing the ability to code.

## Hackathon Flow

```
┌──────────────────────────────────────────────────────────────┐
│ 0:00 - 5:00    Setup and data selection                      │
│   - Verify uv and marimo are installed                       │
│   - Participants choose: provided dataset or own data        │
│   - Instructor does quick setup walkthrough                  │
├──────────────────────────────────────────────────────────────┤
│ 5:00 - 45:00   Working time                                  │
│   - Participants analyze data one question at a time         │
│   - Use Marimo pair coding with AI agent                     │
│   - Instructor available for setup issues only               │
│   - Instructor circulates to identify diverse approaches     │
│     for presentation selection                               │
├──────────────────────────────────────────────────────────────┤
│ 45:00 - 50:00  Wrap-up and presenter selection               │
│   - Announce 3 presenters (selected for diversity)           │
│   - Give 5 minutes to prepare slides/notes                   │
│   - Transition to presentation phase                         │
└──────────────────────────────────────────────────────────────┘
```

## Provided Datasets

Datasets must be curated from the internet and meet these criteria:

| Criterion | Requirement |
|-----------|-------------|
| **Domain** | Biology, chemistry, or life sciences adjacent |
| **Access** | Publicly available, no login/API key required |
| **Size** | Under ~50MB per dataset (loadable in a notebook) |
| **Format** | Standard formats: CSV, TSV, JSON, Parquet |
| **Documentation** | Column descriptions, source link, brief context note |
| **Variety** | At least 3-4 datasets covering different subdomains |

### Dataset Sources to Scour

- **Kaggle**: Biology/chemistry datasets (filter by "public" and "downloadable")
- **UCI Machine Learning Repository**: Bioinformatics and chemistry datasets
- **PDB (Protein Data Bank)**: Structural biology data (may need format conversion)
- **NCBI / GEO**: Gene expression datasets (public, well-documented)
- **ChEMBL**: Bioactive molecule data (chemistry-focused)
- **PubChem**: Chemical compound data
- **Instructor's existing collection**: [2026-pydata-boston-cursor-hackathon](https://github.com/ericmjl/2026-pydata-boston-cursor-hackathon) repo

### Dataset Catalog Template

Each provided dataset should have a catalog entry:

| Field | Description |
|-------|-------------|
| Name | Short descriptive name |
| Source | URL or repository |
| Format | CSV, JSON, etc. |
| Size | Approximate file size |
| Domain | e.g., "gene expression", "molecular properties", "protein structure" |
| Quick start | 1-2 sentences on what the data represents |
| Suggested questions | 2-3 starter analysis questions (optional, participants should define their own) |

## Reproducibility Requirements

Per the HLD, participants should produce notebooks runnable on another person's machine. This is reinforced throughout the hackathon:

| Practice | How it works |
|----------|-------------|
| **Pull data from source, don't download** | The agent writes code that loads data directly from a URL (e.g., `pd.read_csv("https://...")`), not from a downloaded local file |
| **No hardcoded local paths** | Never use paths like `/Users/ericmjl/data/dataset.csv` — these break on any other machine |
| **Cache via data version control if needed** | If a local copy is needed for performance, use a DVC-managed path, not an arbitrary filesystem location |
| **uv for dependencies** | Use `uv run` to execute notebooks; dependencies resolved automatically |
| **Self-contained notebook** | A participant's notebook should run top-to-bottom with `uv run marimo edit notebook.py` |

### Instructor Messaging

During setup walkthrough and circulation, the instructor should say:
- "Don't download data to your machine and reference it with a hardcoded path. Have the agent pull it directly from the source URL."
- "If you need a cached copy, put it in a data version control system like DVC — not just sitting in a folder on your desktop."
- "Your notebook should be something someone else could run without asking you how you set it up."

## Participant Data Options

Participants have two paths:

### Path A: Provided Dataset
- Instructor-curated, vetted, documented
- Lower risk of setup issues
- Easier for instructor to anticipate problems during presentations
- Datasets are sourced from public URLs, reinforcing reproducibility

### Path B: Own Dataset
- More personally relevant and engaging
- Higher risk of format/access issues
- Instructor should warn participants: "If you bring your own data, make sure it's ready to load in a notebook before the workshop starts"
- Encourage participants to use data from public sources (URLs) rather than local files

## Instructor Role During Hackathon

| Activity | Instructor does | Instructor does not |
|----------|----------------|-------------------|
| Setup | Help with uv/marimo installation, dataset download | Debug analysis code or help with Marimo usage |
| During work | Circulate to observe approaches, identify presenters | Sit down and help participants work through problems |
| Presentation selection | Pick 3 people with diverse domains and approaches | Ask for volunteers only (may not give diversity) |

## Success Indicators During Hackathon

The instructor should look for participants who:

1. **Slow down intentionally** - Ask themselves questions before writing code
2. **Validate results** - Check plots/numbers before proceeding to the next step
3. **Engage critically with agent output** - Don't just accept what the AI suggests
4. **Can articulate their domain reasoning** - "In my field, X matters, so I need to check Y"
5. **Practice reproducibility** - Agent pulls data from source URLs (not downloaded local files), no hardcoded paths, cached data in DVC if needed, uv-compatible

These are the participants most likely to give strong presentations.

## Risks and Mitigations

| Risk | Mitigation |
|------|------------|
| Participants struggle with dataset format or loading | Provide 2-3 vetted datasets that are known to work; include quick-start instructions |
| Some participants have no data and no time to choose | Have at least one "easiest to load" dataset ready as a default option |
| Participants revert to prompt-and-pray behavior | This is expected; the presentations phase will surface it as a teachable moment |
| Instructor cannot identify diverse presenters in time | Start looking early (by minute 15); note candidates as you circulate |
| Participants work in isolation with no interaction | Encourage peer help; the networking phase is the main collaboration opportunity |

## Dependencies

- **uv**: Installed on all participant machines
- **Marimo**: Installed on all participant machines
- **Internet access**: For downloading datasets and using Marimo agent feature
- **Provided datasets**: Downloaded and vetted before the workshop
- **Dataset catalog**: Written with links, descriptions, and quick-start notes

## Related Documents

- [High-Level Design](../../high-level-design.md)
- [Demo LLD](../demo/LLD.md)
- [Presentation LLD](../presentations/LLD.md)
