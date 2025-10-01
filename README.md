# Research Paper (Local Run)

This repository contains Jupyter notebooks and data processing code for the NBA analysis pipeline.
It was adapted to run locally without Google Colab.

## Layout
```
Research Paper/
  ├─ Datasets/
  │   ├─ RAW/         # input CSVs from basketball-reference
  │   ├─ TEMP/        # intermediate Excel files
  │   ├─ EDITED/      # manually edited Excel files
  │   ├─ FINAL/       # per-season final Excel files (inputs for analysis)
  │   └─ ANALYSIS/    # analysis outputs (Consolidated, Rank Score, ML outputs, etc.)
  └─ Python Codes/
      ├─ Data Cleaning.ipynb
      ├─ True Label and ML Classification.ipynb
      ├─ Rank Score Classification.ipynb
      └─ Classification Methods Comparison.ipynb
scripts/
  └─ run_all.py
requirements.txt
README.md
```

## Install
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Run the full pipeline headlessly
- Put your data under `Research Paper/Datasets` (subfolders as above).
- Option A (recommended): execute all notebooks via `papermill`

```bash
# From the repository root (where README.md lives):
export RP_PROJECT_ROOT="$PWD/Research Paper"
python scripts/run_all.py
```

- Option B: open notebooks in Jupyter and run cells manually. No Colab code remains.

## Notes
- The notebooks read and write **relative to** `Research Paper/Datasets`.
- You can override the base path by setting `RP_PROJECT_ROOT` before running.
