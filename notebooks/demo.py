# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "anywidget==0.11.0",
#     "cloudscraper==1.2.71",
#     "marimo>=0.23.8",
#     "numpy==2.4.6",
#     "plotly==6.7.0",
#     "polars==1.41.2",
#     "traitlets==5.15.1",
# ]
# ///

import marimo

__generated_with = "0.23.8"
app = marimo.App(width="medium")


@app.cell
def title():
    import marimo as mo

    mo.md("# Skill-Amplified AI for Biological Data Analysis")
    return


if __name__ == "__main__":
    app.run()
