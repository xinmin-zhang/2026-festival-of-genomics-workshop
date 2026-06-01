# Dataset Catalog

All datasets are publicly accessible. Load them directly from source URLs in your notebook — do not download them to your machine.

If you need a cached copy for performance, use a data version control system like DVC rather than placing files in arbitrary local paths.

## Enzyme Engineering

### IRED Novartis — Imine Reductase Activity and Stereoselectivity

Source: Ma, E. J.; Siirola, E.; Moore, C.; et al. "Machine-Directed Evolution of an Imine Reductase for Activity and Stereoselectivity." *ACS Catal.* **2021**, *11* (20), 12433-12445. DOI: [10.1021/acscatal.1c02786](https://pubs.acs.org/doi/abs/10.1021/acscatal.1c02786)

The supplementary CSV files are hosted behind Cloudflare protection on ACS. Use `cloudscraper` to pull them directly from source:

```python
import cloudscraper
import pandas as pd
from io import StringIO

scraper = cloudscraper.create_scraper()
base = "https://pubs.acs.org/doi/suppl/10.1021/acscatal.1c02786/suppl_file"

activity = pd.read_csv(StringIO(scraper.get(f"{base}/cs1c02786_si_002.csv").text))
stereoselectivity = pd.read_csv(StringIO(scraper.get(f"{base}/cs1c02786_si_003.csv").text))
```

| File | Format | Size | Description |
|------|--------|------|-------------|
| `cs1c02786_si_002.csv` | CSV | ~1 MB | Activity screening data (1,000+ variants). Columns: mutation, mean activity, alpha, date, hash, ratio, count, beta |
| `cs1c02786_si_003.csv` | CSV | ~35 KB | Stereoselectivity data for 427 variants. Columns: mutation, r_enantiomeric_excess, ratio, experiment |

**Suggested questions**: Which mutations increase activity while maintaining stereoselectivity? Are there activity-stereoselectivity tradeoffs? Which experiment type produces the best variants?

---

## Drug Discovery

### Drug Discovery — Hetionet

- **URL**: https://huggingface.co/datasets/khairi/drug-discovery-hetionet
- **Format**: Parquet (~2 MB)
- **Domain**: Drug discovery / pharmacogenomics
- **Description**: 23K examples mapping gene neighborhoods to drug molecule designs (SMILES).
- **Suggested questions**: Which gene neighborhoods are most druggable? What molecular properties cluster together?

### Drug Repurposing Knowledge Graph (DRKG)

- **URL**: https://huggingface.co/datasets/khairi/drug-discovery-drkg
- **Format**: Parquet (<5 MB)
- **Domain**: Drug repurposing / pharmacology
- **Description**: 27.8K structured relationships between drugs, diseases, and genes.
- **Suggested questions**: Which drugs have the most disease targets? Are there surprising drug-disease connections?

### Drug Induced Autoimmunity Prediction

- **URL**: https://archive.ics.uci.edu/dataset/drug+induced+autoimmunity+prediction
- **Format**: CSV (<1 MB)
- **Domain**: Computational toxicology / drug safety
- **Description**: 477 drug compounds with 195 molecular descriptors (from RDKit).
- **Suggested questions**: Which molecular descriptors correlate with autoimmunity risk? Are there structural alerts in the data?

---

## Protein Science

### Protein-Peptide Binding Sequences

- **URL**: https://huggingface.co/datasets/ronig/protein_binding_sequences
- **Format**: CSV (~5 MB)
- **Domain**: Protein structure / molecular binding
- **Description**: 16,370 protein-peptide binding pairs with amino acid sequences.
- **Suggested questions**: What sequence motifs predict binding? Are there binding preferences by protein family?

---

## Antibiotic Resistance

### Antibiotic Resistance Classification

- **URL**: https://huggingface.co/datasets/biomap-research/antibiotic_resistance
- **Format**: Parquet (~1.5 MB)
- **Domain**: Antibiotic resistance / clinical microbiology
- **Description**: 3,416 protein sequences labeled with resistance to 19 antibiotics (from the CARD database).
- **Suggested questions**: Which resistance genes confer multi-drug resistance? Are there sequence patterns that predict resistance class?

### Bacterial Antibiotic Resistance — DNA Sequences

- **URL**: https://huggingface.co/datasets/macwiatrak/bacbench-antibiotic-resistance-dna
- **Format**: Parquet
- **Domain**: Bacterial genomics / antimicrobial resistance
- **Description**: 18.5K DNA sequences from bacterial genomes labeled for antibiotic resistance.
- **Suggested questions**: Can you identify resistance gene patterns? How do resistance sequences differ across antibiotics?

---

## Cancer Biology

### Breast Cancer Wisconsin Diagnostic

- **URL**: https://huggingface.co/datasets/scikit-learn/breast-cancer-wisconsin
- **Format**: CSV (~128 KB)
- **Domain**: Cancer diagnostics / clinical genomics
- **Description**: 569 patient samples with 30 features from digitized FNA images. Binary classification (malignant vs benign).
- **Suggested questions**: Which features best distinguish malignant from benign? Are there clusters within the malignant samples?

### Gene Expression — TCGA/CPTAC Survival Analysis

- **URL**: https://huggingface.co/datasets/VatsalPatel18/gene-expression-tcga-cptac-survival-analysis
- **Format**: Parquet (~90 MB — larger, subset recommended)
- **Domain**: Gene expression / cancer genomics / survival analysis
- **Description**: 617 samples with 18K gene expression features from TCGA/CPTAC with survival labels.
- **Suggested questions**: Which genes correlate with survival? Can you identify expression subtypes? (Recommend working with a subset of genes.)

---

## Genomics

### Splice Junction Gene Sequences

- **URL**: https://archive.ics.uci.edu/dataset/molecular-biology-splice-junction-gene-sequences
- **Format**: CSV (<1 MB)
- **Domain**: Genomics / DNA sequence analysis
- **Description**: 3,190 primate splice-junction DNA sequences (60 bases each) classified as exon/intron boundaries.
- **Suggested questions**: What sequence motifs distinguish exon-intron boundaries? Can you build a simple classifier?

---

## Environmental Chemistry

### ApisTox — Pesticide Toxicity to Honey Bees

- **URL**: https://archive.ics.uci.edu/dataset/apistox
- **Format**: CSV (<1 MB)
- **Domain**: Environmental toxicology / cheminformatics
- **Description**: 1,040 chemicals with 13 features predicting toxicity to honey bees.
- **Suggested questions**: What chemical properties predict bee toxicity? Are certain pesticide classes more dangerous?

---

## Bringing Your Own Data

You are welcome to bring your own dataset. Ensure:
- It is loadable from a public URL or committed to your fork
- The format is standard (CSV, TSV, JSON, Parquet)
- You can load it in one cell of your notebook
