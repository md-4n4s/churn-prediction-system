from . import *


def main():

    churn_labels = load_data(INPUT_DIR / "churn_labels.csv")
    customer_info = load_data(INPUT_DIR / "customer_info.csv", dates=["SignupDate"])
    usage_data = load_data(INPUT_DIR / "usage_data.csv", dates=["Month"])

    churn_labels = standardize_column_names(churn_labels)
    customer_info = standardize_column_names(customer_info)
    usage_data = standardize_column_names(usage_data)

    customer_info = drop_unnecessary_columns(customer_info, ["Age"])

    customer_info = drop_duplicates(customer_info, ["CustomerID"])

    customer_info = fix_invalid_monthly_charges(customer_info)

    # Merge 3 datasets into one using CustomerID
    df = churn_labels.merge(customer_info, on="CustomerID").merge(
        usage_data, on="CustomerID"
    )

    return df


if __name__ == "__main__":
    main()
