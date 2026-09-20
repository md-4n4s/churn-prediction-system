import pandas as pd

__all__ = ["clean", "drop_duplicates"]


def standardize_column_names(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = df.columns.str.strip().str.replace(" ", "_")

    return df


def drop_unnecessary_columns(
    df: pd.DataFrame, columns: list[str] | None = None
) -> pd.DataFrame:
    df.drop(columns, axis=1, inplace=True)

    return df


def drop_duplicates(df: pd.DataFrame, columns: list[str] | None = None) -> pd.DataFrame:
    df.drop_duplicates(subset=columns, inplace=True)

    return df


def fix_invalid_monthly_charges(df: pd.DataFrame) -> pd.DataFrame:
    """Replace negative Monthly Charges with mean"""

    # Calculate mean of non-negative values
    mean_charge = df.loc[df["MonthlyCharges"] >= 0, "MonthlyCharges"].mean()

    df.loc[df["MonthlyCharges"] < 0, "MonthlyCharges"] = mean_charge

    return df


def clean(
    df: pd.DataFrame,
    unnecessary_columns: list[str] | None = None,
    duplicate_columns: list[str] | None = None,
) -> pd.DataFrame:
    df = standardize_column_names(df)

    if unnecessary_columns:
        df = drop_unnecessary_columns(df, unnecessary_columns)

    df = drop_duplicates(df, duplicate_columns)

    if "MonthlyCharges" in df.columns:
        df = fix_invalid_monthly_charges(df)

    return df
