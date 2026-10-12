from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

INPUT_DIR = BASE_DIR / "data" / "raw"

OUTPUT_DIR = BASE_DIR / "data" / "processed" / "processed.csv"
