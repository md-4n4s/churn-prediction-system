from . import *


def main():

    churn_labels = load_data(INPUT_DIR / "churn_labels.csv")
    customer_info = load_data(INPUT_DIR / "customer_info.csv", dates=["SignupDate"])
    usage_data = load_data(INPUT_DIR / "usage_data.csv", dates=["Month"])

    churn_labels = clean(churn_labels)
    customer_info = clean(
        customer_info, unnecessary_columns=["Age"], duplicate_columns=["CustomerID"]
    )
    usage_data = clean(usage_data)

    # Merge 3 datasets into one using CustomerID
    df = churn_labels.merge(customer_info, on="CustomerID").merge(
        usage_data, on="CustomerID"
    )

    df = aggregate(df)

    # Drop all duplicates to have one row per customer
    df = drop_duplicates(df, ["CustomerID"])

    validate(df)

    return df


if __name__ == "__main__":
    main()
