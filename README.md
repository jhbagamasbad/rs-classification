Sequence of Python Notebooks to run (first to last):

- Data Cleaning.ipynb
- Rank Score Classification.ipynb
- True Label and ML Classification.ipynb
- Classification Methods Comparison.ipynb



NOTE:

All Python Notebooks were written with the help of ChatGPT. For every step/function that was defined/written, I gave detailed descriptions of how it should function properly (e.g.: Computation for Pos1 and Pos2, Rank Score scoring system using lookup tables, etc.). I even gave examples when necessary, and I ask two or three computational questions to ensure understanding of the concept for the processes/functions.



Instructions (for Windows PowerShell):

1. Unzip rs-classification.zip somewhere (e.g., C:\code\rs-classification), then open Windows PowerShell or Linux bash in that folder.
2. Create and activate a virtual environment:

        python -m venv .venv

        .\.venv\Scripts\Activate.ps1

                or

        python -m venv .venv

        source .venv/bin/activate


3. Install dependencies:

        python -m pip install --upgrade pip

        pip install -r requirements.txt

4. Run pipeline:

        python scripts/run_all.py --timeout 0
