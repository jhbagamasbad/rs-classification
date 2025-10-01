#!/usr/bin/env python3
"""
Execute the full pipeline by running the notebooks in order using papermill.
Requires: pip install papermill jupyter
You can set RP_PROJECT_ROOT to point to the 'Research Paper' folder (default: current working directory).
"""
import os
from pathlib import Path
import papermill as pm

# Resolve the project root that contains 'Datasets' and 'Python Codes'
PROJECT_ROOT = Path(os.environ.get("RP_PROJECT_ROOT", Path.cwd())) / "Research Paper"

# Ensure kernels inherit the same environment variable
os.environ["RP_PROJECT_ROOT"] = str(PROJECT_ROOT)

nb_dir = PROJECT_ROOT / "Python Codes"
out_dir = PROJECT_ROOT / "notebook_runs"
out_dir.mkdir(parents=True, exist_ok=True)

order = [
    "Data Cleaning.ipynb",
    "True Label and ML Classification.ipynb",
    "Rank Score Classification.ipynb",
    "Classification Methods Comparison.ipynb",
]

for name in order:
    in_nb  = nb_dir / name
    out_nb = out_dir / name.replace(".ipynb", ".executed.ipynb")
    print(f"Executing: {in_nb}")
    pm.execute_notebook(
        input_path=str(in_nb),
        output_path=str(out_nb),
        parameters={}  # not used; notebooks read env var instead
    )
print("Pipeline execution complete.")
