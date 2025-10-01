# scripts/run_all.py
from __future__ import annotations

import asyncio
import os
import platform
import sys
from pathlib import Path

import nbformat
from nbclient import NotebookClient

# Some nbclient versions move this; be defensive
try:
    from nbclient.exceptions import CellExecutionError  # modern
except Exception:  # pragma: no cover
    try:
        from nbclient.client import CellExecutionError  # older
    except Exception:  # fallback
        class CellExecutionError(Exception):
            pass

# ---- Windows event loop fix (avoids zmq "add_reader" warning) ----
if platform.system() == "Windows":
    try:
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    except Exception:
        pass

# ---- Paths & environment ----
REPO_ROOT     = Path(__file__).resolve().parents[1]
NOTEBOOKS_DIR = REPO_ROOT / "notebooks"
OUTPUT_DIR    = REPO_ROOT / "executed_notebooks"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Make the repo importable inside the spawned Jupyter kernel (so notebooks can `import project_paths`)
_existing = os.environ.get("PYTHONPATH", "")
os.environ["PYTHONPATH"] = str(REPO_ROOT) + (os.pathsep + _existing if _existing else "")

# Choose the kernel to use (create it with `python -m ipykernel install --user --name rs-classification`)
KERNEL_NAME = os.environ.get("KERNEL_NAME", "rs-classification")

def run_notebook(nb_name: str, timeout: int = 0) -> None:
    """
    Execute a single notebook located in NOTEBOOKS_DIR and save executed copy to OUTPUT_DIR.
    timeout=0 means no per-cell timeout.
    """
    nb_path  = NOTEBOOKS_DIR / nb_name
    if not nb_path.exists():
        print(f"[skip] Not found: {nb_path}", file=sys.stderr)
        sys.exit(1)

    print(f"[run] Executing: {nb_name} (cwd={NOTEBOOKS_DIR})", flush=True)
    nb = nbformat.read(nb_path.open("r", encoding="utf-8"), as_version=4)

    # None = no timeout in nbclient
    per_cell_timeout = None if (timeout is None or int(timeout) == 0) else int(timeout)

    client = NotebookClient(
        nb,
        kernel_name=KERNEL_NAME,
        timeout=per_cell_timeout,
        allow_errors=False,
    )

    try:
        # Prefer nbclient's 'cwd' kwarg; fall back to changing dirs if not supported
        try:
            client.execute(cwd=str(NOTEBOOKS_DIR))
        except TypeError:
            # Older nbclient: no 'cwd' parameter -> temporarily chdir
            old_cwd = os.getcwd()
            try:
                os.chdir(str(NOTEBOOKS_DIR))
                client.execute()
            finally:
                os.chdir(old_cwd)
    except CellExecutionError as e:
        print("\n[error] A cell raised an exception while executing this notebook.\n", file=sys.stderr)
        print(str(e), file=sys.stderr)
        sys.exit(1)

    out_path = OUTPUT_DIR / nb_name
    with out_path.open("w", encoding="utf-8") as f:
        nbformat.write(nb, f)
    print(f"[ok] Saved executed notebook -> {out_path}")

def parse_args(argv: list[str]) -> tuple[list[str], int]:
    """
    Minimal CLI parsing for:
      --one <Notebook.ipynb>
      --timeout <seconds>
    """
    run_order = [
        "Data Cleaning.ipynb",
        "Rank Score Classification.ipynb",
        "True Label and ML Classification.ipynb",
        "Classification Methods Comparison.ipynb",
    ]
    timeout = 0

    if "--one" in argv:
        i = argv.index("--one")
        try:
            run_order = [argv[i + 1]]
        except IndexError:
            print("Usage: --one <Notebook Name.ipynb>", file=sys.stderr)
            sys.exit(2)

    if "--timeout" in argv:
        i = argv.index("--timeout")
        try:
            timeout = int(argv[i + 1])
        except Exception:
            print("Usage: --timeout <seconds>", file=sys.stderr)
            sys.exit(2)

    return run_order, timeout

def main() -> int:
    # Basic validation / helpful diagnostics
    if not NOTEBOOKS_DIR.exists():
        print(f"[error] Notebooks folder missing: {NOTEBOOKS_DIR}", file=sys.stderr)
        return 1

    # Show effective kernel and PYTHONPATH for debugging
    print(f"[env] KERNEL_NAME={KERNEL_NAME}")
    print(f"[env] PYTHONPATH={os.environ.get('PYTHONPATH','')}")

    run_order, timeout = parse_args(sys.argv)

    for nb_name in run_order:
        run_notebook(nb_name, timeout=timeout)

    print("\n[done] All notebooks executed successfully.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
