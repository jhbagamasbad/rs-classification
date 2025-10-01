from pathlib import Path

# When run via run_all.py, notebooks' CWD is the "notebooks/" folder
REPO_ROOT    = Path(__file__).resolve().parent
DATA_DIR     = REPO_ROOT / "data"

RAW_DIR      = DATA_DIR / "RAW"
EDITED_DIR   = DATA_DIR / "EDITED"
FINAL_DIR    = DATA_DIR / "FINAL"
ANALYSIS_DIR = DATA_DIR / "ANALYSIS"
TEMP_DIR     = DATA_DIR / "TEMP"

# Optional file used by several notebooks
ROOKIES_PATH = DATA_DIR / "Rookies List.xlsx"

# Make sure output dirs exist
for p in (ANALYSIS_DIR, TEMP_DIR):
    p.mkdir(parents=True, exist_ok=True)
