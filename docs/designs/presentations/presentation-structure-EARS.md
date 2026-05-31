# Presentation Structure - EARS

**Parent LLD**: ./LLD.md

## Presentation Flow

- **PRES-STRUCT-001**: The system shall structure each presentation into 7 segments: domain context (30s), dataset (30s), question (30s), where they slowed down (1 min), where they sped up (30s), reproducibility (30s), and agent help (30s).
- **PRES-STRUCT-002**: The system shall allocate approximately 6 minutes per presenter across 3 presenters.
- **PRES-STRUCT-003**: The system shall allocate 2 minutes for the transition from hackathon and the final wrap-up.

## Domain Context

- **PRES-STRUCT-010**: When a presenter begins, the system shall have them state their domain context: "In my field, X is really important because..."
- **PRES-STRUCT-011**: When a presenter describes their dataset, the system shall have them mention the source (URL vs local file).

## Analysis Approach

- **PRES-STRUCT-020**: When a presenter describes where they slowed down, the system shall have them explain why: "I knew X mattered, so I checked Y before proceeding."
- **PRES-STRUCT-021**: When a presenter describes where they sped up, the system shall have them explain their confidence: "I felt confident about Z, so I moved through it quickly."
- **PRES-STRUCT-022**: Where a presenter used the speed-through-then-validate-backwards approach, the system shall accept it as legitimate.
- **PRES-STRUCT-023**: Where a presenter used the slow-down-upfront approach, the system shall accept it as legitimate.

## Reproducibility

- **PRES-STRUCT-030**: When a presenter describes reproducibility, the system shall have them explain how they ensured their notebook is runnable by others: data from source URLs, no hardcoded paths, DVC for cached data, uv-compatible.

## Agent Collaboration

- **PRES-STRUCT-040**: When a presenter describes agent help, the system shall have them explain how pair coding contributed to their analysis.

## Related Documents

- [Presentation LLD](./LLD.md)
