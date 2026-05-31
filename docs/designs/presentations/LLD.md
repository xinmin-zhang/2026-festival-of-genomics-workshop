# Presentations - Low-Level Design

**Created**: 2026-05-31
**HLD Link**: ../../high-level-design.md

## Overview

The presentations are the final 20-minute segment where 3 participants share their hackathon work. The instructor selects presenters for diversity of domain and approach, not for polish or correctness. Commentary is coaching-style — supportive, not critical. The goal is for the audience to learn from each presenter's choices about where to slow down and where to speed up.

## Context

Per the HLD, presenters are selected during the hackathon (not by volunteer) to ensure diversity. Both forward methodical analysis and speed-through-then-validate-backwards approaches are accepted. Teachable moments are highlighted for the room.

## Presentation Flow

```
┌──────────────────────────────────────────────────────────────┐
│ 0:00 - 2:00    Transition from hackathon                     │
│   - Thank everyone for working                               │
│   - Announce 3 presenters (pre-selected)                     │
│   - Give 5 minutes to prepare (hackathon wrap-up)            │
├──────────────────────────────────────────────────────────────┤
│ 2:00 - 8:00    Presenter 1                                   │
│   - 2 min context: domain, dataset, question                 │
│   - 3 min walk-through: where they slowed down, why          │
│   - 1 min instructor coaching commentary                     │
├──────────────────────────────────────────────────────────────┤
│ 8:00 - 14:00   Presenter 2                                   │
│   - Same structure                                           │
│   - Look for different approach from Presenter 1             │
├──────────────────────────────────────────────────────────────┤
│ 14:00 - 20:00  Presenter 3 + wrap-up                         │
│   - Same structure                                           │
│   - 1 min wrap-up: thank everyone, encourage networking      │
└──────────────────────────────────────────────────────────────┘
```

## Presenter Selection Criteria

The instructor should select 3 presenters who demonstrate:

| Criterion | What to look for |
|-----------|-----------------|
| **Different domains** | e.g., one genomics, one chemistry, one adjacent field |
| **Different approaches** | e.g., one slow-down-upfront, one speed-then-validate, one hybrid |
| **Willingness to share** | Not necessarily the "best" work — the most instructive work |
| **Clear story** | Can articulate why their domain required specific checks |

### Selection Process

1. **Start early** — Begin identifying candidates by minute 15 of the hackathon
2. **Ask what people are working on** — Quick conversations: "What question are you trying to answer?" "Where did you slow down?"
3. **Note diversity** — Keep a mental (or physical) list of domains and approaches represented
4. **Invite, don't ask** — Approach specific people rather than calling for volunteers
5. **Give advance notice** — Tell selected presenters early so they can prepare

## Presentation Structure (for participants)

Each presenter should cover:

1. **Domain context** (30 seconds): "In my field, X is really important because..."
2. **Dataset** (30 seconds): What data they used, where it came from (source URL vs local file)
3. **Question** (30 seconds): The one question they were trying to answer
4. **Where they slowed down** (1 minute): "I knew X mattered, so I checked Y before proceeding"
5. **Where they sped up** (30 seconds): "I felt confident about Z, so I moved through it quickly"
6. **Reproducibility** (30 seconds): How they ensured their notebook is runnable by others — data pulled from source URLs by the agent, no hardcoded local paths, cached data in DVC if needed, uv-compatible
7. **What the agent helped with** (30 seconds): How pair coding contributed

Both approaches are valid:
- **Forward**: "I slowed down upfront because I knew what mattered in my domain"
- **Backward**: "I sped through to get a result, then worked backwards to validate"

## Instructor Commentary Style

### Do:
- Frame observations as generalizable lessons: "What I noticed here is..."
- Connect to the principle: "This is exactly what we talked about — slowing down where your domain expertise says to"
- Highlight teachable moments for the room: "For everyone else, a thing to watch for here is..."
- Be warm and encouraging: "Great example of checking assumptions before proceeding"

### Don't:
- Be a "Simon Cowell" — no harsh criticism or public embarrassment
- Focus on what went wrong without acknowledging what went right
- Give unsolicited advice that turns it into a one-on-one coaching session
- Spend more than 1 minute on commentary per presenter

## Handling Missed Steps

When a presenter missed something important (common with the backward approach):

| Situation | Instructor response |
|-----------|-------------------|
| Presenter missed a check that was important | "A teachable moment for the room — when working backwards, it's easy to skip X. Here's why checking it matters..." |
| Audience member spots the miss | "Good catch — what would you have done differently?" |
| Presenter is aware and addressed it | "Nice — you caught that yourself, which is exactly the skill we're building" |
| Miss is minor and doesn't affect conclusions | Acknowledge briefly, move on: "One thing to keep in mind for next time..." |

## Incentive Structure

Presenters receive an offer: **free career development chat with the instructor**.

| Aspect | Details |
|--------|---------|
| **What it is** | One-on-one conversation, whatever the presenter wants |
| **Likely topics** | Career development, but open to anything |
| **When it happens** | After the workshop, arranged organically |
| **Why it works** | Creates incentive to prepare seriously; builds relationship; adds value beyond the workshop |

## Risks and Mitigations

| Risk | Mitigation |
|------|------------|
| Fewer than 3 willing presenters | Instructor pre-selects during hackathon; approach specific people rather than calling for volunteers |
| All presenters have similar approaches | Instructor actively seeks diversity during circulation; if not possible, acknowledge the similarity and discuss why |
| Presenters ramble or go over time | Give a 1-minute warning; gently guide back to the structure |
| Presenter's data doesn't load or show properly | Ask them to describe their process verbally; don't try to debug live |
| Commentary feels too critical | Pre-plan 2-3 generalizable lessons to share; frame everything as "what we can learn" not "what went wrong" |

## Dependencies

- **3 selected presenters**: Identified during hackathon, given 5 minutes to prepare
- **Projection/screen**: Presenters need to share their Marimo notebooks
- **Timer**: To keep each presentation within ~6 minutes
- **Instructor's notes**: Mental or written list of diversity criteria and pre-identified candidates

## Related Documents

- [High-Level Design](../../high-level-design.md)
- [Demo LLD](../demo/LLD.md)
- [Hackathon LLD](../hackathon/LLD.md)
