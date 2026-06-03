# Workshop follow-along guide

Follow along live during each phase of the workshop.

---

## Phase 1: live demo (20 min)

Eric will demonstrate the one-question-at-a-time principle using Marimo's AI pair coding feature. Follow along by copying each prompt into your own coding agent as Eric works through them.

Open your notebook now:

```bash
uvx marimo edit --sandbox --no-token notebooks/demo.py
```

### Step 1 — connect to your notebook

Copy this prompt into your agent:

> Connect to the Marimo notebook running at <http://localhost:2718> using the marimo-pair skill.

### Step 2 — load data from source

Copy this prompt into your agent:

> Load two datasets directly from ACS using cloudscraper and polars. URL 1: <https://pubs.acs.org/doi/suppl/10.1021/acscatal.1c02786/suppl_file/cs1c02786_si_002.csv> — this contains enzyme activity screening data. URL 2: <https://pubs.acs.org/doi/suppl/10.1021/acscatal.1c02786/suppl_file/cs1c02786_si_003.csv> — this contains chiral selectivity (enantioselectivity) data. Use cloudscraper to fetch the CSVs and polars to read them into dataframes. Show me the dataframes.

The two datasets come from the same IRED enzyme engineering study:

- **`si_002` (activity)**: Each row is a variant. The `mean` column is activity, `mutation` is the variant name, `experiment` is the campaign it came from.
- **`si_003` (chiral selectivity)**: Each row is a variant. The `r_enantiomeric_excess` column measures stereoselectivity (ranges from -1 to +1), `ratio` is the activity, `experiment` is the campaign.

**The lesson**: Data pulled directly from ACS URLs is reproducible. No hardcoded local paths, no downloaded files, no "can you send me that CSV?" Anyone can run your notebook from scratch.

### Step 3 — ask your first question

Copy this prompt:

> Filter both dataframes to keep only single-point mutants — these are rows where the `mutation` column does not contain a semicolon (`;`). Then create a joint scatter plot using plotly with x=activity (the `ratio` or `mean` column from the activity dataframe), y=enantioselectivity (`r_enantiomeric_excess` from the chiral selectivity dataframe), and marginal distributions on both axes. Only include variants that appear in both dataframes.

**The lesson**: Don't speed past the data table. Before jumping into visualizations, look at the raw data. Seeing the table live gives you a feel for what's actually going on — column types, value ranges, weird entries. This is where slowing down pays off.

### Step 4 — plot ECDFs

ECDFs (Empirical Cumulative Distribution Functions) are better than histograms for visualizing distributions. They show all data points without binning, make percentiles trivial to read, and reveal outliers, multimodality, and repeat values. See [Eric's blog post on ECDFs](https://ericmjl.github.io/blog/2018/7/14/ecdfs/) for the full argument.

Copy this prompt:

> Now plot ECDFs of the single-point mutants. One plotly line plot for the ECDF of enantioselectivity (`r_enantiomeric_excess`), and a separate plotly line plot for the ECDF of activity (`mean` or `ratio`). On each ECDF, annotate the 25th, 50th, and 75th percentile: draw a horizontal line from the y-axis at the corresponding cumulative probability (0.25, 0.50, 0.75) to the ECDF curve, then drop a vertical line down to the x-axis, and label the exact value at the x-axis.

**The lesson**: Always prefer ECDFs over histograms. No binning artifacts, every data point is visible, and percentiles are trivial to read off the plot.

### Step 5 — heatmap with dropdown

Copy this prompt:

> Create a heatmap using plotly where x-axis is the amino acid position (extract the position number from the mutation string), y-axis is the mutant amino acid (the letter the position was mutated to), and the color is the value. Use the viridis colorscale for activity and the rdbu colorscale for enantioselectivity. Below the heatmap, show a line plot of the mean or maximum value at each position across all single-point mutants. Use a marimo dropdown to toggle between activity and enantioselectivity for the heatmap colorscale, and another marimo dropdown to toggle between mean and max for the line plot. Display both plots together in the same output.

**Why these colorscales**: Activity ranges from 0 to 1, so viridis (sequential) shows low-to-high clearly. Enantioselectivity ranges from -1 to +1, so rdbu (diverging, centered at zero) makes it easy to see which mutants favor the R vs S enantiomer.

**The lesson**: Marimo's reactive UI widgets — dropdowns, sliders, and the like — make it trivial to build interactive dashboards. Use them to explore data without rewriting code.

### Step 6 — protein structure viewer

Copy this prompt:

> Create an anywidget that loads and displays the 7OG3 protein structure (PDB ID: 7OG3) using 3Dmol.js. The structure should be fetchable from the RCSB PDB at <https://files.rcsb.org/download/7OG3.pdb>. Show the protein as a cartoon representation. Place it in a marimo cell so it renders inline in the notebook.

**The lesson**: When you venture into unfamiliar territory — 3D molecular visualization, custom widgets, whatever — don't jump straight to the final product. Start with de-risking questions: "Is this even possible?" "Can I get a basic version working first?" Break the unfamiliar into small, verifiable steps.

### Step 7 — color residues by activity or enantioselectivity

Copy this prompt:

> Now color the protein residues by the same metric selected in the dropdown from Step 5 (activity or enantioselectivity). For each position that has a single-point mutant, color the residue using viridis for activity or rdbu for enantioselectivity, matching the heatmap colorscheme. The mean vs max dropdown should also apply here. Uncolored positions remain grey. This view should be reactive to the same dropdown controls.

**The lesson**: Build on what works. We had the viewer from Step 6 and the color logic from Step 5. Now we combine them. Each step is small enough to verify before moving on.

### Step 8 — add tooltip to protein viewer

Copy this prompt:

> Add a tooltip to the 3Dmol.js viewer. When the user clicks on a colored residue, show a tooltip with the residue identifier and the exact value (activity or enantioselectivity, depending on the dropdown). When the user clicks on blank space, hide the tooltip.

**The lesson**: Make your visualizations explorable. Tooltips, click interactions, and hover info let your audience investigate the data themselves. Custom data exploration should be easy.

---

## Phase 2: hack time (50 min)

Now apply the same principle on your own dataset.

### Pick a dataset

Here are the recommended datasets for hack time, with links and starter prompts. For the full catalog, see [datasets.md](./datasets.md).

### Create your notebook

Replace the filename with your own given name and surname:

```bash
uvx marimo edit --sandbox --no-token notebooks/givenname-surname.py
```

### Apply the principle

For each analysis step:

1. **State your question** — Write it as a markdown cell or comment before you write any code
2. **Load data from source** — Pull data directly from the URL using polars or pandas. No downloaded files, no hardcoded local paths. If you need a cache, use DVC.
3. **Write the code** — Use the AI agent to help, but review what it produces
4. **Inspect the result** — Look at the output before moving on. Does it make sense?
5. **Validate with domain knowledge** — "In my field, X matters, so I should check Y"
6. **Move to the next question** — Only after validating the current one

### Suggested datasets and potential questions

Full disclosure: Eric hasn't worked with these datasets before either. This is genuine exploration — you and the instructor are in the same boat. That's the point. The methodical approach works even when you're seeing the data for the first time.

**Drug discovery — Hetionet** ([dataset](https://huggingface.co/datasets/khairi/drug-discovery-hetionet), ~2 MB, Parquet)
- How many unique drugs are in this dataset, and what do the gene neighborhood features look like?
- Which gene neighborhoods are most druggable?
- What molecular properties cluster together?

**Drug repurposing — DRKG** ([dataset](https://huggingface.co/datasets/khairi/drug-discovery-drkg), <5 MB, Parquet)
- Which drugs have the most disease targets?
- Are there surprising drug-disease connections?

**Antibiotic resistance classification** ([dataset](https://huggingface.co/datasets/biomap-research/antibiotic_resistance), ~1.5 MB, Parquet)
- How many sequences are resistant to each antibiotic, and is there overlap (multi-drug resistance)?
- Are there sequence patterns that predict resistance class?

**Breast cancer diagnostics** ([dataset](https://huggingface.co/datasets/scikit-learn/breast-cancer-wisconsin), ~128 KB, CSV)
- Which features show the largest difference between malignant and benign tumors?
- Are there clusters within the malignant samples?

**Protein-peptide binding** ([dataset](https://huggingface.co/datasets/ronig/protein_binding_sequences), ~5 MB, CSV)
- What sequence motifs predict binding?
- Are there binding preferences by protein family?

**Drug induced autoimmunity** ([dataset](https://archive.ics.uci.edu/dataset/1104/drug_induced_autoimmunity_prediction), <1 MB, CSV)
- Which molecular descriptors correlate with autoimmunity risk?
- Are there structural alerts in the data?

**Splice junction gene sequences** ([dataset](https://archive.ics.uci.edu/dataset/69/molecular+biology+splice+junction+gene+sequences), <1 MB, CSV)
- What sequence motifs distinguish exon-intron boundaries?
- Can you build a simple classifier?

**Pesticide toxicity to honey bees** ([dataset](https://archive.ics.uci.edu/dataset/995/apistox), <1 MB, CSV)
- What chemical properties predict bee toxicity?
- Are certain pesticide classes more dangerous?

---

## Phase 3: presentations (20 min)

We will invite 3 participants to present what they worked on during hack time. If you're selected, use the structure below to walk us through your analysis.

### How to present

When you present your notebook:

1. **Domain context** (30s): "In my field, X is really important because..."
2. **Dataset** (30s): What data you used and where you loaded it from
3. **Your question** (30s): The question you were trying to answer
4. **Where you slowed down** (1 min): "I knew X mattered, so I checked Y before proceeding"
5. **Where you sped up** (30s): "I felt confident about Z, so I moved through it quickly"
6. **Reproducibility** (30s): How you ensured someone else can run your notebook (data from source URLs, no hardcoded paths)
7. **What the agent helped with** (30s): How pair coding contributed

### How to submit your work

1. Push your notebook to your fork
2. Open a pull request against [github.com/ericmjl/2026-festival-of-genomics-workshop](https://github.com/ericmjl/2026-festival-of-genomics-workshop)
3. Ask your agent to use the `gh` CLI to open the PR with a summary of your analysis

---

## Phase 4: networking

After the presentations:

- Connect with people whose analyses were interesting
- Discuss different approaches to the same data
- Follow up on collaboration opportunities
- Presenters: Eric is available for a career development chat — [book a time](https://calendly.com/ericmjl/45-minute-meeting)
