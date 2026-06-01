import marimo

__generated_with = "0.13.11"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    mo.md("# Skill-Amplified AI for Biological Data")
    return (mo,)


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
