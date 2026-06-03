# Agent instructions (2026-festival-of-genomics-workshop)

This file is **repo-local guidance** for coding agents (Cursor, Claude Code, Copilot, and similar) working in this repository. It is the **canonical** place to record project-specific conventions and lessons learned. Prefer updating this file over one-off chat memory.

## Instruction hierarchy

1. **This file (`AGENTS.md`)** — durable rules for *this* repo (stack, layout, style, workflows).
2. **`pyproject.toml`** — tool configuration (Ruff, pytest, Pixi, Hatch, etc.); treat as source of truth for settings.
3. **User chat** — immediate task scope; if the user gives a rule that should persist, fold it into this file (see [Self-improvement](#self-improvement)).

If `CLAUDE.md` or `.claude/CLAUDE.md` appears later, consolidate duplicated guidance here and point those files at `AGENTS.md` (or replace them with a short stub) so instructions do not conflict.

## Stack (do not fight the template)

- **Python**: `>=3.10` (see `pyproject.toml`).
- **Env / tasks**: **Pixi** — use `pixi run …` or `pixi shell` as documented in `pyproject.toml` and the project README.
- **Packaging**: **Hatchling** (`[build-system]` in `pyproject.toml`).
- **Lint & format**: **Ruff** (`ruff check`, `ruff format`) and **pre-commit** (see `.pre-commit-config.yaml`).
- **Tests**: **pytest** (`pixi run test` or the task name defined for tests).
- **CLI**: **Typer** — entrypoint wired in `pyproject.toml` under `[project.scripts]`; implementation lives under `2026_festival_of_genomics_workshop/`.
- **Docs**: **MkDocs** (Material) when the docs workflow is used (`mkdocs.yaml`, `docs/`).
- **Notebooks**: **Marimo** — prefer Marimo (`.py` notebooks with reactive execution) over Jupyter for exploratory work. Always launch in **sandboxed mode**: `uvx marimo edit --sandbox <folder>` (use `.` for the current directory). This ensures a fresh isolated environment with the latest package versions resolved automatically via `uvx`.

When adding dependencies, prefer declaring them in **`pyproject.toml`** and syncing the Pixi environment as this repo already does, rather than ad hoc `pip install` in prose unless the user asks for a one-off experiment.

## Repository layout (expectations)

- **Package code**: `2026_festival_of_genomics_workshop/` — main library and CLI.
- **Tests**: `tests/` — mirror public behavior; prefer pytest functions over heavy class taxonomies unless the codebase already uses patterns.
- **Docs**: `docs/` — Markdown for MkDocs; keep navigation in `mkdocs.yaml` when adding pages.
- **Config**: `pyproject.toml` at repo root; avoid duplicating tool config in random dotfiles.

Use **`pyprojroot.here()`** (or equivalent) for paths anchored at the project root when the project already uses `pyprojroot`; do not invent a new “find project root” helper.

## Code style (match existing code)

- **Type hints** on new functions and public APIs.
- **`pathlib.Path`** over `os.path` where practical.
- **Ruff** is the formatter and linter; run `ruff format` / `ruff check` or `pre-commit run --all-files` before claiming work is clean.
- **Docstrings**: Sphinx-style with `:param` / `:returns` where the project already does so; do not strip existing docstring depth.
- Prefer **small, reviewable diffs** — avoid drive-by refactors unrelated to the task.

If the user’s global preferences (e.g. logging library) differ from this repo, **follow this repo’s existing patterns** unless the user explicitly asks to migrate.

## Quality gates (before saying “done”)

- Run **tests** (`pixi run test` or the repo’s test task) after substantive Python changes.
- Run **Ruff** / **pre-commit** when edits touch Python or config hooks care about.
- Do not claim CI passes unless you actually ran the relevant commands and they succeeded.

## Self-improvement (how this file evolves)

When the user corrects the agent (“always do X”, “never do Y”, “use Z for this repo”), treat that as a candidate **permanent** rule:

1. **Propose** a concrete edit to `AGENTS.md` (section + wording), integrated into existing bullets — not a dated diary entry.
2. **Resolve conflicts** — if the new rule contradicts an older bullet, replace or narrow the old text so there is a single clear rule.
3. **Ask once** — “Should I add this to `AGENTS.md`?” — and apply after confirmation.

This keeps agent behavior stable across sessions and contributors.

## Arrow of intent (design docs must stay coherent)

This project uses design-driven development. The arrow of intent is:

```
HLD → LLDs → EARS → Tests → Code
```

**When the user asks for any code or behavior change, the agent must:**

1. **Read the design docs first** — check `docs/high-level-design.md`, the relevant `docs/designs/<feature>/LLD.md`, and any `docs/designs/<feature>/*-EARS.md` files.
2. **Assess what needs updating** — identify which HLD decisions, LLD components, or EARS requirements are affected by the change.
3. **Update design docs before code** — mutate the docs in place at the correct level (HLD for scope/goal changes, LLD for component/interface changes, EARS for requirement changes). Delete what's obsolete.
4. **Cascade the change** — if the HLD changes, review all linked LLDs; if an LLD changes, review all linked EARS; if an EARS changes, review tests and code.
5. **Preserve cross-links** — ensure all `## Related Documents` / `## Related Designs` sections remain accurate after edits.

This is **supremely important**. Do not implement a change without first verifying that the design docs reflect the new intent. The documentation should always describe what is actually being built, not what was planned weeks ago.

## Marimo notebook conventions

When creating or editing Marimo notebooks in this repo:

- **Markdown cells sandwich code cells.** Every logical step gets a markdown cell with a heading before the code cell, and a markdown cell with observations after it. This makes the notebook readable and reviewable by humans.
- **One action per code cell.** Don't put multiple unrelated operations in a single cell. Each cell should do one thing (load data, compute a metric, create a plot).
- **Use `mo.md()` for markdown cells**, not Python comments. Markdown cells render as rich text in the notebook.
- **Never re-define an import across cells.** Each import (`import X as Y`) must appear in exactly one cell. If another cell needs the same module, reference the name already defined by the earlier cell — do not write another `import X` or `import X as Z`.
- **Never re-import symbols already defined elsewhere.** Before writing any import in a new cell, check which modules are already in scope from earlier cells and reference those names instead.
- **Always run a cell immediately after creating it.** If it errors, fix the issue before moving on — never leave a broken cell behind.

Example structure:

```
[markdown cell] ## Load activity data
               Load the IRED activity screening CSV from source.

[code cell]     import cloudscraper
                import polars as pl
                ...

[markdown cell] ## Activity distribution
               The activity data has N variants...
```

## Scope and safety

- **Stay within the task** — no broad refactors or unrelated files unless the user expands scope.
- **Secrets** — never commit API keys, tokens, or machine-specific paths; use `.env` (gitignored) and documented env vars.
- **Generated or vendored trees** — do not “clean up” generated assets unless the user asked; some paths may be managed by Pixi, notebooks, or build tools.

## Optional: project glossary

Add a short subsection here once stable terms emerge (e.g. domain nouns, experiment IDs, dataset names) so agents use vocabulary consistently in code and docs.

---

*This repository was generated from [cookiecutter-python-project](https://github.com/ericmjl/cookiecutter-python-project). The [`pyds project init`](https://github.com/ericmjl/pyds-cli) command uses that template. Edit freely as the project grows.*
