# Agentic Data Science Workshop - High-Level Design

**Created**: 2026-05-31
**Source**: [Design Transcript](./transcripts/design.md)

## Problem Statement

Junior researchers and working professionals in genomics tend to rush through analysis without methodically checking assumptions. They prompt-and-pray with AI tools rather than engaging critically with what the agent produces. This leads to missed steps, wrong results, and wasted time. There is no structured way to teach the principle of slowing down analysis to one question at a time.

## Goals

1. **Teach the one-question-at-a-time principle** - Gate all analysis by one plot at a time, intentionally slowing down to double-check assumptions before proceeding
2. **Introduce Marimo as a tool** - Show that Marimo exists, its pair-coding-with-agent feature, and its graph view for tracking conceptual dependencies
3. **Demonstrate trainable methodology** - Make explicit that methodical analysis is a skill anyone can develop, not a natural talent
4. **Enable networking and collaboration** - Use the workshop format to connect people working on different domains and datasets

## Non-Goals

- **Making people Marimo experts** - Knowing Marimo exists and being curious to try it later is sufficient
- **Teaching genomics domain knowledge** - The principle applies across domains; the demo uses a surface engineering example precisely because it is outside genomics
- **Circulating and debugging everyone** - The instructor cannot help every participant during the hackathon
- **Collecting structured feedback** - No surveys or metrics; success is measured by whether people reach out organically
- **Using proprietary or access-restricted datasets** - All provided datasets must be publicly available and easy to download

## Target Users

- **Working professionals** - Postdocs and researchers who can code and analyze data
- **Current graduate students** - Already writing code, learning to be methodical
- **Mixed experience levels** - All attendees share the ability to code, not a shared domain

## Workshop Structure

```
┌─────────────────────────────────────────────────────────────┐
│  Phase 1: Demo (20 min)                                     │
│  ┌───────────────────────────────────────────────────────┐  │
│  │ - Surface engineering example (instructor's domain)   │  │
│  │ - Pair coding with AI agent as the single featured    │  │
│  │   Marimo capability                                   │  │
│  │ - Engineered mistakes debugged live, thinking out     │  │
│  │   loud, showing domain expertise guiding debugging    │  │
│  │ - Explicit statement: this is a trainable skill       │  │
│  └───────────────────────────────────────────────────────┘  │
│                             ↓                                │
│  Phase 2: Hackathon (50 min)                                │
│  ┌───────────────────────────────────────────────────────┐  │
│  │ - Participants work on provided biology/chemistry     │  │
│  │   datasets (scoured from the internet) or their own   │  │
│  │   life sciences data                                  │  │
│  │ - One question at a time, methodical analysis         │  │
│  │ - Initial setup support (uv, marimo installed)        │  │
│  │ - Free-for-all after setup; instructor not            │  │
│  │   circulating extensively                             │  │
│  └───────────────────────────────────────────────────────┘  │
│                             ↓                                │
│  Phase 3: Presentations (20 min)                              │
│  ┌───────────────────────────────────────────────────────┐  │
│  │ - 3 participants present their work                   │  │
│  │ - Selected for diversity: different domains,          │  │
│  │   different approaches to slowing down                │  │
│  │ - Coaching-style commentary (not Simon Cowell)        │  │
│  │ - Accept both approaches: slow-down-upfront or        │  │
│  │   speed-through-then-validate-backwards               │  │
│  │ - Teachable moments highlighted for the room          │  │
│  └───────────────────────────────────────────────────────┘  │
│                             ↓                                │
│  Phase 4: Networking (unstructured)                           │
│  ┌───────────────────────────────────────────────────────┐  │
│  │ - Organic conversations about others' analysis        │  │
│  │ - Collaboration opportunities                         │  │
│  │ - Instructor offers career chats to presenters        │  │
│  └───────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

## Key Design Decisions

### Decision 1: Demo uses a non-genomics example

**Choice**: Surface engineering dataset for the 20-minute demo

**Rationale**: The instructor knows this example intimately, enabling confident live debugging. Showing the principle works outside genomics reinforces that it is domain-agnostic.

**Alternatives considered**:
- Genomics dataset: Would be more relevant but instructor may not know it well enough for live debugging
- Toy example: Too simple to convey real analytical thinking

### Decision 2: Focus demo on pair coding with agent only

**Choice**: Only demonstrate the pair-coding feature of Marimo, not the graph view

**Rationale**: Pair coding with an agent is the "biggest win" — the feature that most clearly shows why Marimo matters for the principle. The graph view is valuable but would overcomplicate a 20-minute demo.

**Alternatives considered**:
- Show both features: Would dilute focus, neither gets proper treatment in 20 minutes
- Show graph view only: Less compelling; doesn't demonstrate the AI partnership concept

### Decision 3: Engineer mistakes into the demo

**Choice**: Intentionally include mistakes that the instructor catches and debugs live

**Rationale**: Scientists start to see mistakes and that is when it clicks. Engineering a few makes the teaching moment visceral rather than accidental.

**Alternatives considered**:
- Let mistakes happen naturally: Unreliable within a tight 20-minute window
- Point out potential mistakes without executing them: Less impactful than live debugging

### Decision 4: Accept both forward and backward analysis approaches

**Choice**: Validate both "slow down upfront because I know what matters" and "speed through then validate backwards"

**Rationale**: Junior researchers naturally tend toward the latter. Both are legitimate. The teachable moment is when the backward approach misses something — that becomes a discussion point during presentations.

**Alternatives considered**:
- Enforce only forward methodical approach: Discourages a valid strategy, feels prescriptive
- Accept everything without commentary: Misses teachable moments

### Decision 5: Presenters get career chat incentive

**Choice**: Offer free career development chats to the 3 presenters

**Rationale**: Creates incentive to lean in and show work seriously. Also serves as a value-add for engaged participants. The chats are whatever the presenter wants — likely broader career questions.

**Alternatives considered**:
- No incentive: People may not volunteer to present
- Prizes/swag: Less personal, doesn't create follow-up relationship

### Decision 6: Hackathon datasets are biology/chemistry focused

**Choice**: Provide publicly available biology and chemistry datasets sourced from the internet, curated from existing science dataset collections (e.g., the instructor's [2026-pydata-boston-cursor-hackathon](https://github.com/ericmjl/2026-pydata-boston-cursor-hackathon) repo)

**Rationale**: The Festival of Genomics audience spans pharma, biotech, and academia in life sciences and adjacent fields. Biology/chemistry datasets are more relevant and engaging than generic or engineering data. Participants can also bring their own datasets if they prefer.

**Alternatives considered**:
- Only instructor-provided datasets: Limits personal relevance for participants with their own data
- Only participant-provided datasets: Inconsistent quality, some may not have suitable data ready
- Generic datasets (iris, titanic): Too trivial for this audience, doesn't match the festival context

### Decision 7: Reproducibility is a core principle

**Choice**: Notebooks must be runnable on another person's machine. Data is pulled directly from source URLs by the agent — never downloaded to a hardcoded local path. If caching a local copy is necessary, it goes into a data version control system (e.g., DVC), not the filesystem at an arbitrary path.

**Rationale**: A notebook that only runs on one machine is not reproducible research. Hardcoded local paths (`/Users/ericmjl/data/...`) and downloaded copies break reproducibility the moment someone else tries to run it. Pulling from source URLs ensures data provenance is explicit. Data version control systems solve the "I need a local copy for performance" problem without sacrificing reproducibility. This reinforces the methodical principle: document your data provenance, don't assume your environment is stable.

**Alternatives considered**:
- No reproducibility requirement: Easier for participants, but misses a key teaching moment about research rigor
- Require full environment pinning (requirements.txt, conda env): Too much overhead for a 50-minute hackathon
- Only require that the notebook runs locally: Doesn't guarantee another person can run it
- Allow downloaded data with relative paths: Better than hardcoded paths, but still breaks if the data directory is deleted or not shared

## Risks and Mitigations

| Risk | Mitigation |
|------|------------|
| Participants cannot install tools (uv, marimo) beforehand | Build initial setup support into the start; have troubleshooting steps ready |
| Mixed experience levels cause some to fall behind | Use simple demo example everyone can follow; accept diverse approaches in presentations |
| Instructor cannot help everyone during hackathon | Rely on presentations as the main learning vehicle; encourage peer help |
| Presentations all cover similar ground | Instructor circulates during hackathon to identify diverse approaches and invite specific people |
| Participants just go through the motions without internalizing the principle | Presentations require showing where they slowed down and why; audience learns from others' choices |
| Provided datasets are hard to access, poorly documented, or in unusable formats | Vet each dataset before the workshop: confirm public access, document format, include download links and quick-start instructions |

## Success Criteria

- Participants know Marimo exists and are curious to try it
- Participants leave understanding the one-question-at-a-time principle as a trainable skill
- Presentations showcase different domains and different ways of applying the principle
- Networking leads to organic follow-up conversations and potential collaborations
- Some participants reach out after the workshop saying it was useful

## Related Designs

- [Demo Design](./designs/demo/LLD.md)
- [Hackathon Design](./designs/hackathon/LLD.md)
- [Presentation Design](./designs/presentations/LLD.md)
