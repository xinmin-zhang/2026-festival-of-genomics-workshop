# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "anywidget==0.11.0",
#     "cloudscraper==1.2.71",
#     "marimo>=0.23.8",
#     "numpy==2.4.6",
#     "pandas==3.0.3",
#     "plotly==6.7.0",
#     "polars==1.41.2",
#     "pyarrow==24.0.0",
#     "traitlets==5.15.1",
# ]
# ///

import marimo

__generated_with = "0.23.9"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import cloudscraper
    import polars as pl
    import io

    return cloudscraper, io, mo, pl


@app.cell
def _(mo):
    mo.md("""
    # Skill-Amplified AI for Biological Data Analysis
    """)
    return


@app.cell
def _(cloudscraper, io, pl):
    import time

    def _fetch_csv(url):
        s = cloudscraper.create_scraper()
        # Visit the journal page first to establish a valid session
        base = "https://pubs.acs.org/doi/10.1021/acscatal.1c02786"
        s.get(base, headers={"Referer": "https://pubs.acs.org/"})
        time.sleep(2)
        r = s.get(url, headers={"Referer": base})
        r.raise_for_status()
        return pl.read_csv(io.BytesIO(r.content))

    df_activity = _fetch_csv("https://pubs.acs.org/doi/suppl/10.1021/acscatal.1c02786/suppl_file/cs1c02786_si_002.csv")
    time.sleep(3)
    df_selectivity = _fetch_csv("https://pubs.acs.org/doi/suppl/10.1021/acscatal.1c02786/suppl_file/cs1c02786_si_003.csv")
    return df_activity, df_selectivity


@app.cell
def _(df_activity, df_selectivity, mo):
    mo.vstack([
        mo.md("## Enzyme Activity Screening"),
        mo.ui.table(df_activity.to_pandas()),
        mo.md("## Chiral Selectivity / Enantioselectivity"),
        mo.ui.table(df_selectivity.to_pandas()),
    ])
    return


@app.cell
def _(df_activity, df_selectivity, mo, pl):
    import plotly.express as px

    _act = df_activity.filter(~pl.col("mutation").str.contains(";"))
    _sel = df_selectivity.filter(~pl.col("mutation").str.contains(";"))

    _joined = _act.select(["mutation", "ratio"]).join(
        _sel.select(["mutation", "r_enantiomeric_excess"]),
        on="mutation",
        how="inner",
    )

    _fig = px.scatter(
        _joined.to_pandas(),
        x="ratio",
        y="r_enantiomeric_excess",
        marginal_x="histogram",
        marginal_y="histogram",
        hover_name="mutation",
        labels={
            "ratio": "Activity (ratio)",
            "r_enantiomeric_excess": "Enantioselectivity (R-ee)",
        },
        title="Single-point mutants: Activity vs Enantioselectivity",
    )

    mo.vstack([
        mo.md(f"## Single-Point Mutants: Activity vs Enantioselectivity"),
        mo.md(f"*{len(_joined)} variants present in both datasets*"),
        mo.ui.plotly(_fig),
    ])
    return


@app.cell
def _(mo):
    metric_dd = mo.ui.dropdown(
        options={"Activity (ratio)": "activity", "Enantioselectivity (R-ee)": "enantioselectivity"},
        value="Activity (ratio)",
        label="Metric",
    )
    agg_dd = mo.ui.dropdown(
        options={"Mean": "mean", "Max": "max"},
        value="Mean",
        label="Line plot aggregation",
    )
    mo.hstack([metric_dd, agg_dd], gap=2)
    return agg_dd, metric_dd


@app.cell
def _(agg_dd, df_activity, df_selectivity, metric_dd, mo, pl):
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots

    _metric = metric_dd.value
    _agg = agg_dd.value

    # Select the right dataframe, value column, colorscale and label
    if _metric == "activity":
        _df_raw = df_activity
        _value_col = "ratio"
        _colorscale = "viridis"
        _label = "Activity (ratio)"
    else:
        _df_raw = df_selectivity
        _value_col = "r_enantiomeric_excess"
        _colorscale = "rdbu"
        _label = "Enantioselectivity (R-ee)"

    # Filter single-point mutants and parse position + mutant AA
    _df = (
        _df_raw
        .filter(~pl.col("mutation").str.contains(";"))
        .with_columns([
            pl.col("mutation").str.extract(r"(\d+)", 1).cast(pl.Int64).alias("position"),
            pl.col("mutation").str.slice(-1).alias("mutant_aa"),
        ])
        .select(["mutation", "position", "mutant_aa", _value_col])
    )

    _df_pd = _df.to_pandas()

    # Pivot for heatmap: rows=mutant_aa, columns=position
    _pivot = _df_pd.pivot_table(
        index="mutant_aa", columns="position", values=_value_col, aggfunc="mean"
    ).sort_index(axis=1).sort_index(axis=0)

    # Line plot aggregation per position
    _line = (
        _df_pd.groupby("position")[_value_col].mean()
        if _agg == "mean"
        else _df_pd.groupby("position")[_value_col].max()
    ).reset_index().sort_values("position")

    # Build combined figure
    _fig = make_subplots(
        rows=2, cols=1,
        shared_xaxes=True,
        row_heights=[0.7, 0.3],
        vertical_spacing=0.06,
        subplot_titles=["Heatmap", f"{_agg.capitalize()} per position"],
    )

    _fig.add_trace(
        go.Heatmap(
            z=_pivot.values,
            x=_pivot.columns.tolist(),
            y=_pivot.index.tolist(),
            colorscale=_colorscale,
            colorbar=dict(title=_label, len=0.65, y=0.65),
            hoverongaps=False,
            name=_label,
        ),
        row=1, col=1,
    )

    _fig.add_trace(
        go.Scatter(
            x=_line["position"],
            y=_line[_value_col],
            mode="lines+markers",
            line=dict(color="#2196F3"),
            marker=dict(size=5),
            name=f"{_agg.capitalize()} {_label}",
        ),
        row=2, col=1,
    )

    _fig.update_layout(
        title=f"Single-point mutants — {_label}",
        height=750,
        xaxis2_title="Position",
        yaxis_title="Mutant amino acid",
        yaxis2_title=_label,
        showlegend=False,
    )

    mo.vstack([
        mo.md("## Positional Heatmap"),
        mo.ui.plotly(_fig),
    ])
    return


@app.cell
def _():
    import anywidget
    import traitlets

    class MolViewer(anywidget.AnyWidget):
        pdb_id       = traitlets.Unicode("7OG3").tag(sync=True)
        color_map    = traitlets.Dict({}).tag(sync=True)
        value_map    = traitlets.Dict({}).tag(sync=True)   # {str(pos): float}
        metric_label = traitlets.Unicode("").tag(sync=True)

        _esm = """
        function loadScript(src) {
          return new Promise((resolve, reject) => {
            if (document.querySelector(`script[src="${src}"]`)) {
              resolve(); return;
            }
            const s = document.createElement('script');
            s.src = src;
            s.onload = resolve;
            s.onerror = reject;
            document.head.appendChild(s);
          });
        }

        async function render({ model, el }) {
          const pdb_id = model.get('pdb_id');

          // ── layout ──────────────────────────────────────────────
          const wrapper = document.createElement('div');
          wrapper.style.cssText = 'background:#1a1a2e;border-radius:8px;padding:8px;position:relative;';

          const headerLabel = document.createElement('div');
          headerLabel.textContent = `PDB: ${pdb_id}`;
          headerLabel.style.cssText = 'color:#aaa;font-family:monospace;font-size:12px;margin-bottom:4px;';

          const viewerDiv = document.createElement('div');
          viewerDiv.style.cssText = 'width:100%;height:520px;position:relative;';

          // ── tooltip ─────────────────────────────────────────────
          const tooltip = document.createElement('div');
          tooltip.style.cssText = [
            'position:absolute',
            'display:none',
            'background:rgba(15,15,35,0.96)',
            'color:#e8e8f0',
            'padding:7px 11px',
            'border-radius:6px',
            'font-family:monospace',
            'font-size:12px',
            'line-height:1.6',
            'pointer-events:none',
            'z-index:1000',
            'border:1px solid #4a4a6a',
            'white-space:pre',
            'box-shadow:0 3px 12px rgba(0,0,0,0.6)',
          ].join(';');

          wrapper.appendChild(headerLabel);
          wrapper.appendChild(viewerDiv);
          wrapper.appendChild(tooltip);
          el.appendChild(wrapper);

          // ── 3Dmol setup ─────────────────────────────────────────
          await loadScript('https://3dmol.org/build/3Dmol-min.js');
          const viewer = $3Dmol.createViewer(viewerDiv, { backgroundColor: '#1a1a2e' });

          const resp = await fetch(`https://files.rcsb.org/download/${pdb_id}.pdb`);
          const pdbData = await resp.text();
          viewer.addModel(pdbData, 'pdb');
          viewer.zoomTo();

          // ── color application ────────────────────────────────────
          function applyColors() {
            const colorMap = model.get('color_map');
            viewer.setStyle({}, { cartoon: { color: '#888888' } });
            if (colorMap && Object.keys(colorMap).length > 0) {
              for (const [resi, color] of Object.entries(colorMap)) {
                viewer.setStyle({ resi: parseInt(resi) }, { cartoon: { color } });
              }
            }
            viewer.render();
          }

          // ── tooltip helpers ──────────────────────────────────────
          function showTooltip(clientX, clientY, text) {
            tooltip.textContent = text;
            tooltip.style.display = 'block';
            const rect = wrapper.getBoundingClientRect();
            let x = clientX - rect.left + 14;
            let y = clientY - rect.top  - 14;
            // flip left if near right edge
            if (x + tooltip.offsetWidth + 20 > rect.width) {
              x = clientX - rect.left - tooltip.offsetWidth - 14;
            }
            tooltip.style.left = x + 'px';
            tooltip.style.top  = y + 'px';
          }

          function hideTooltip() {
            tooltip.style.display = 'none';
          }

          // ── click handling ───────────────────────────────────────
          // 3Dmol fires its callback before the native DOM click bubbles,
          // so we use a flag to distinguish atom-click from background-click.
          let atomJustClicked = false;

          viewer.setClickable({}, true, function(atom, _v, event) {
            atomJustClicked = true;
            const valueMap    = model.get('value_map');
            const metricLabel = model.get('metric_label');
            const resiStr     = String(atom.resi);
            const val         = valueMap[resiStr];

            const header  = `${atom.resn} ${atom.resi}  (chain ${atom.chain})`;
            const valLine = val !== undefined
              ? `${metricLabel}: ${val.toFixed(4)}`
              : '(no data)';

            showTooltip(event.clientX, event.clientY, `${header}\n${valLine}`);
          });

          viewerDiv.addEventListener('click', () => {
            if (!atomJustClicked) hideTooltip();
            atomJustClicked = false;
          });

          // ── reactivity ───────────────────────────────────────────
          applyColors();
          model.on('change:color_map', applyColors);
        }

        export default { render };
        """

        _css = ".anywidget { width: 100%; }"

    return (MolViewer,)


@app.cell
def _(MolViewer, mo):
    viewer = MolViewer(pdb_id="7OG3")
    mo.vstack([
        mo.md("## 7OG3 Protein Structure — colored by selected metric"),
        viewer,
    ])
    return (viewer,)


@app.cell
def _(agg_dd, df_activity, df_selectivity, metric_dd, pl, viewer):
    import plotly.colors as pc

    _metric = metric_dd.value
    _agg    = agg_dd.value

    if _metric == "activity":
        _df_raw      = df_activity
        _value_col   = "ratio"
        _colorscale  = "Viridis"
        _metric_label = "Activity (ratio)"
    else:
        _df_raw      = df_selectivity
        _value_col   = "r_enantiomeric_excess"
        _colorscale  = "RdBu"
        _metric_label = "Enantioselectivity (R-ee)"

    _df = (
        _df_raw
        .filter(~pl.col("mutation").str.contains(";"))
        .with_columns(
            pl.col("mutation").str.extract(r"(\d+)", 1).cast(pl.Int64).alias("position")
        )
        .group_by("position")
        .agg(
            pl.col(_value_col).mean().alias("value")
            if _agg == "mean"
            else pl.col(_value_col).max().alias("value")
        )
    )

    _pos_vals = {row["position"]: row["value"] for row in _df.iter_rows(named=True)}

    def _to_hex(rgb_str):
        inner = rgb_str.split("(")[1].rstrip(")")
        r, g, b = (round(float(x.strip())) for x in inner.split(","))
        return f"#{r:02x}{g:02x}{b:02x}"

    if _pos_vals:
        _vals  = list(_pos_vals.values())
        _vmin, _vmax = min(_vals), max(_vals)
        _span  = _vmax - _vmin if _vmax != _vmin else 1.0
        _normed = [(_v - _vmin) / _span for _v in _vals]
        _rgb   = pc.sample_colorscale(_colorscale, _normed)
        _color_map = {str(pos): _to_hex(col) for pos, col in zip(_pos_vals.keys(), _rgb)}
        _value_map = {str(pos): float(val)   for pos, val in _pos_vals.items()}
    else:
        _color_map = {}
        _value_map = {}

    viewer.color_map    = _color_map
    viewer.value_map    = _value_map
    viewer.metric_label = _metric_label
    return


if __name__ == "__main__":
    app.run()
