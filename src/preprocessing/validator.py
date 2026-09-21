import pandas as pd
from pandas.api.types import is_datetime64_any_dtype

from src.preprocessing.exceptions import InvalidFieldException, MissingColumnException


def check_missing_values(df: pd.DataFrame, column: str) -> None:
    if df[column].isnull().any():
        raise InvalidFieldException(f"Column {column} has missing value.")


def check_duplicated(df: pd.DataFrame, column: str) -> None:
    if df[column].duplicated().any():
        raise InvalidFieldException(f"Column {column} has duplicate values.")


def check_dtype(df: pd.DataFrame, column: str, data_type: str) -> None:
    if df[column].dtype != data_type:
        raise InvalidFieldException(f"Column {column} has invalid dtype.")


def check_unique_values(df: pd.DataFrame, column: str, allowed: int) -> None:
    if df[column].nunique() > allowed:
        raise InvalidFieldException(
            f"Column {column} has more than {allowed} unique values."
        )


def check_negative(df: pd.DataFrame, column: str) -> None:
    if df[column].min() < 0:
        raise InvalidFieldException(f"Column {column} has negative values.")


def check_datetime(df: pd.DataFrame, column: str) -> None:
    if not is_datetime64_any_dtype(df[column]):
        raise InvalidFieldException(f"Column {column} has invalid dtype.")


def check_columns(df: pd.DataFrame, columns: list) -> None:
    missing_columns = [col for col in columns if col not in df.columns]

    if missing_columns:
        raise MissingColumnException(f"Missing columns: {missing_columns}")


def validate_simple(df: pd.DataFrame, column: str, dtype: str) -> None:
    check_missing_values(df, column)

    check_dtype(df, column, dtype)


def validate_id(df: pd.DataFrame, column: str, dtype: str) -> None:
    validate_simple(df, column, dtype)

    check_duplicated(df, column)


def validate_category(df: pd.DataFrame, column: str, dtype: str, allowed: int) -> None:
    validate_id(df, column, dtype)

    check_unique_values(df, column, allowed)


def validate_positive(df: pd.DataFrame, column: str, dtype: str) -> None:
    validate_simple(df, column, dtype)

    check_negative(df, column)


def validate(df: pd.DataFrame) -> None:
    check_columns(
        df,
        [
            "CustomerID",
            "Churn",
            "Gender",
            "Region",
            "ContractType",
            "MonthlyCharges",
            "SignupDate",
            "CallMinutes_Mean",
            "CallMinutes_Range",
            "CallMinutes_Mean3M",
            "CallMinutes_Change",
            "DataUsageGB_Mean",
            "DataUsageGB_Mean6M",
            "DataUsageGB_Change",
            "SMSCount_Mean",
            "Complaints_Mean",
        ],
    )
    validate_id(df, "CustomerID", "str")
    validate_category(df, "Churn", "int64", 2)
    validate_category(df, "Gender", "str", 2)
    validate_category(df, "Region", "str", 3)
    validate_category(df, "ContractType", "str", 3)
    validate_positive(df, "MonthlyCharges", "float64")
    check_datetime(df, "SignupDate")
    validate_positive(df, "CallMinutes_Mean", "float64")
    validate_positive(df, "CallMinutes_Mean3M", "float64")
    validate_simple(df, "CallMinutes_Change", "float64")
    validate_simple(df, "CallMinutes_Range", "float64")
    validate_positive(df, "DataUsageGB_Mean", "float64")
    validate_positive(df, "DataUsageGB_Mean6M", "float64")
    validate_simple(df, "DataUsageGB_Change", "float64")
    validate_positive(df, "SMSCount_Mean", "float64")
    validate_positive(df, "Complaints_Mean", "float64")
