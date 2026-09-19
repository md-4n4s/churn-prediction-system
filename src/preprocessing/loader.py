from pathlib import Path

import pandas as pd


def load_data(filename: Path, dates: list[str] | None = None) -> pd.DataFrame:
    df = pd.read_csv(filename, parse_dates=dates)
    return df
