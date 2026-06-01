# 2026-festival-of-genomics-workshop

Skill-Amplified AI for Biological Data Workshop

Made with :heart: by Eric Ma (@ericmjl).

## Setup Instructions (Workshop Participants)

You need three things before the workshop begins:

1. **Git** — to clone this repository
2. **[uv](https://docs.astral.sh/uv/getting-started/installation/)** — to run Marimo notebooks with automatic dependency resolution
3. **Internet connection** — to pull datasets from source and use the AI pair coding feature

### Step 1: Fork the repo

Click the **Fork** button on [github.com/ericmjl/2026-festival-of-genomics-workshop](https://github.com/ericmjl/2026-festival-of-genomics-workshop), then clone **your fork**:

```bash
git clone https://github.com/YOUR_USERNAME/2026-festival-of-genomics-workshop
cd 2026-festival-of-genomics-workshop
```

You will make a pull request to the original repo later to present your work.

### Step 2: Install uv

If you don't already have uv:

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Step 3: Launch the demo notebook

```bash
uvx marimo edit --sandbox --no-token notebooks/demo.py
```

This opens the demo notebook in your browser with a fresh sandboxed environment. Dependencies are resolved automatically.

### Verify everything works

```bash
uv run python -c "import marimo; print(marimo.__version__)"
```

If you see a version number, you're ready.

## Workshop Plan

| Time | Activity |
|------|----------|
| First 20 min | **Live demo** — Eric demonstrates methodical, one-question-at-a-time analysis using Marimo's AI pair coding feature |
| Next 50 min | **Hack time** — You work on your own analysis using provided datasets or your own data, applying the same methodical approach |
| Final 20 min | **Presentations** — 3 participants share their work by opening a pull request against this repo |

During the hack time, you will build your analysis in a Marimo notebook. When it's time to present, you'll push your notebook to your fork and open a pull request to this repository.

## Datasets

See [docs/datasets.md](docs/datasets.md) for the full catalog of biology and chemistry datasets available for the hackathon. You can use any of these or bring your own data.

## Get started for development

To get started:

```bash
git clone git@github.com:ericmjl/2026-festival-of-genomics-workshop
cd 2026-festival-of-genomics-workshop
pixi install
```
