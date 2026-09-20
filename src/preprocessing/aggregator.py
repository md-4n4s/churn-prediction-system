import pandas as pd

from .cleaner import drop_unnecessary_columns


def aggregate_call_minutes(df: pd.DataFrame) -> pd.DataFrame:
    """ Replace monthly call-minute values with customer-level aggregate features """

    df["CallMinutes_Mean"] = df.groupby("CustomerID")["CallMinutes"].transform("mean")

    # Calculate difference between maximum value and minimum value
    df["CallMinutes_Range"] = df.groupby("CustomerID")["CallMinutes"].transform(
        lambda x: x.max() - x.min()
    )

    # Extract last 3 months
    last_3m = df["Month"] > "2023-09-30"

    # Calculate mean of last 3 months per customer
    last_3m_mean = df.loc[last_3m].groupby("CustomerID")["CallMinutes"].mean()

    df["CallMinutes_Mean3M"] = df["CustomerID"].map(last_3m_mean)

    # Calculate change in values from first month to last month
    df["CallMinutes_Change"] = df.groupby("CustomerID")["CallMinutes"].transform(
        lambda x: x.iloc[0] - x.iloc[-1]
    )

    df = drop_unnecessary_columns(df, ["CallMinutes"])

    return df


def aggregate_data_usage(df: pd.DataFrame) -> pd.DataFrame:
    """ Replace monthly data-usage values with customer-level aggregate features """

    df["DataUsageGB_Mean"] = df.groupby("CustomerID")["DataUsageGB"].transform("mean")

    # Extract last 6 months
    last_6m = df["Month"] > "2023-06-30"

    # Calculate mean of last 6 months per customer
    last_6m_mean = df.loc[last_6m].groupby("CustomerID")["DataUsageGB"].mean()

    df["DataUsageGB_Mean6M"] = df["CustomerID"].map(last_6m_mean)

    # Calculate change in values from first month to last month
    df["DataUsageGB_Change"] = df.groupby("CustomerID")["DataUsageGB"].transform(
        lambda x: x.iloc[0] - x.iloc[-1]
    )

    df = drop_unnecessary_columns(df, ["DataUsageGB"])

    return df


def aggregate_sms_count(df: pd.DataFrame) -> pd.DataFrame:
    """ Replace monthly sms-count values with customer-level aggregate features """

    df["SMSCount_Mean"] = df.groupby("CustomerID")["SMSCount"].transform("mean")

    df = drop_unnecessary_columns(df, ["SMSCount"])

    return df


def aggregate_complaints(df: pd.DataFrame) -> pd.DataFrame:
    """ Replace monthly complaints values with customer-level aggregate features """

    df["Complaints_Mean"] = df.groupby("CustomerID")["Complaints"].transform("mean")

    df = drop_unnecessary_columns(df, ["Complaints"])

    return df


def aggregate(df: pd.DataFrame) -> pd.DataFrame:
    df = aggregate_call_minutes(df)

    df = aggregate_data_usage(df)

    df = aggregate_sms_count(df)

    df = aggregate_complaints(df)

    return df
