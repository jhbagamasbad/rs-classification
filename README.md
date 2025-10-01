Sequence of Python Notebooks to run (first to last):

- Data Cleaning.ipynb
- Rank Score Classification.ipynb
- True Label and ML Classification.ipynb
- Classification Methods Comparison.ipynb



NOTE:

All Python Notebooks were written with the help of ChatGPT. The algorithms for Rank Score and Machine Learning benchmarks were formulated by the authors, but were implemented with ChatGPT assistance regarding structure and package use.  Player roles under PER and DARKO were determined by obtaining published scores by Hollinger and Medvedovsky and imposing appropriate cutoffs.



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


   An additional step for Linux users to install a Jupyter kernel pointing to the venv:

           python -m ipykernel install --user --name rs-classification --display-name "rs-classification (venv)"
   

5. Run pipeline:

        python scripts/run_all.py --timeout 0
