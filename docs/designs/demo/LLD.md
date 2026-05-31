# Demo - Low-Level Design

**Created**: 2026-05-31
**HLD Link**: ../../high-level-design.md

## Overview

The demo is the opening 20-minute segment of the workshop. Its purpose is to demonstrate the one-question-at-a-time principle through a live pair-coding session with an AI agent in Marimo, using a surface engineering dataset. The demo must be simple enough that everyone can follow, but substantive enough to show real analytical thinking.

## Context

Per the HLD, the demo uses a non-genomics example (surface engineering) to show the principle is domain-agnostic. The instructor knows this dataset intimately, enabling confident live debugging. The single featured Marimo capability is pair coding with an AI agent — the graph view is not demonstrated.

## Demo Flow

```
┌──────────────────────────────────────────────────────────────┐
│ 0:00 - 2:00    Introduction                                  │
│   - State the principle: slow down, one question at a time   │
│   - State: this is a trainable skill, not natural talent     │
│   - Introduce Marimo briefly, pair coding as the focus       │
├──────────────────────────────────────────────────────────────┤
│ 2:00 - 10:00   First analysis question                       │
│   - Load surface engineering dataset                         │
│   - Ask one question, let agent help write code               │
│   - Execute, inspect result, validate before proceeding      │
│   - Narrate thinking: "In my field, X matters, so I check Y" │
├──────────────────────────────────────────────────────────────┤
│ 10:00 - 16:00  Engineered mistake + live debugging           │
│   - Agent suggests something slightly wrong (instructor      │
│     pre-plants the mistake)                                  │
│   - Instructor catches it, debugs live                       │
│   - Thinks out loud: shows how domain expertise guides       │
│     where to look first                                      │
│   - Fixes it, explains what went wrong                       │
├──────────────────────────────────────────────────────────────┤
│ 16:00 - 20:00  Wrap-up and transition to hackathon           │
│   - Recap: one question at a time, trust but verify          │
│   - Explain hackathon structure and dataset options           │
│   - Tell people to get setup ready                           │
└──────────────────────────────────────────────────────────────┘
```

## Dataset Requirements

The surface engineering dataset used in the demo must:

| Requirement | Details |
|-------------|---------|
| Publicly accessible | No login, no API key required |
| Small enough to load quickly | Under ~10MB, loads in seconds |
| Has clear structure | Tabular or near-tabular, easy to understand columns |
| Supports at least 2 analysis questions | Enough for the first question + the mistake/debugging segment |
| Instructor knows intimately | Must be able to predict where mistakes would naturally arise |

## Engineered Mistakes

The demo must include 2-3 pre-planned mistakes that the instructor catches and debugs. These should be:

| Type | Example | Why it works |
|------|---------|-------------|
| **Statistical misinterpretation** | Confusing correlation with causation | Common mistake, easy to catch with domain knowledge |
| **Plotting error** | Wrong axis, wrong aggregation | Visually obvious, creates teachable moment |
| **Assumption violation** | Applying a test that requires normality to non-normal data | Shows why checking assumptions matters |

Each mistake follows this pattern:
1. Agent suggests code/interpretation containing the mistake
2. Instructor executes and observes unexpected result
3. Instructor narrates their debugging thought process
4. Instructor identifies the root cause using domain expertise
5. Instructor fixes it and explains the lesson

## Reproducibility in the Demo

The demo notebook itself models reproducibility practices:

- **Data from source**: Load the surface engineering dataset from a URL via the agent (e.g., `pd.read_csv("https://...")`), never from a hardcoded local path
- **uv-compatible**: Runs with `uv run marimo edit demo.py`
- **No hardcoded paths**: Uses source URLs only
- **Self-contained**: Anyone can clone the repo and run the demo notebook

The instructor should explicitly mention this during the demo: "Notice I'm having the agent pull data directly from the source URL — not downloading it to my desktop and pointing at a hardcoded path. That's what makes this reproducible."

## Marimo Setup

The demo notebook must be prepared in advance:

- **File**: A single Marimo notebook (`.py` file) in the workshop repo
- **Cells**: Pre-structured to follow the demo flow (intro → question 1 → mistake → debug → wrap-up)
- **Execution**: Must run cleanly from top to bottom before the workshop
- **Agent integration**: Pair coding session must be ready to start mid-demo

## Risks and Mitigations

| Risk | Mitigation |
|------|------------|
| Demo runs longer than 20 minutes | Time-box each segment; be willing to skip the second analysis question if needed |
| Agent produces unexpected output | Have a backup notebook with pre-recorded outputs; fall back to narrating what would happen |
| Mistake is too obvious or too subtle | Rehearse with a colleague; calibrate based on their reaction |
| Marimo pair coding feature doesn't work live | Have screenshots or a pre-recorded clip as backup |

## Dependencies

- **Marimo**: Installed and functional on the instructor's machine
- **Surface engineering dataset**: Publicly accessible, small, well-understood
- **uv**: Available for any one-off dependency installation
- **Internet connection**: Needed for Marimo agent feature (if cloud-based)

## Related Documents

- [High-Level Design](../../high-level-design.md)
- [Hackathon LLD](../hackathon/LLD.md)
- [Presentation LLD](../presentations/LLD.md)
