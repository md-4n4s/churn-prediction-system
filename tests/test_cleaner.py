import pandas as pd

from src.preprocessing.cleaner import (
    clean,
    drop_duplicates,
    drop_unnecessary_columns,
    fix_invalid_monthly_charges,
    standardize_column_names,
)


def test_standardize_column_names() -> None:
    original = pd.DataFrame(
        {
            "  Age": [20, 30, 40],
            "student name": ["Alice", "Bob", "Charlie"],
            "Marks  ": [5, 6, 7],
        }
    )

    expected = pd.DataFrame(
        {
            "Age": [20, 30, 40],
            "student_name": ["Alice", "Bob", "Charlie"],
            "Marks": [5, 6, 7],
        }
    )

    result = standardize_column_names(original)

    pd.testing.assert_frame_equal(result, expected)


def test_drop_unnecessary_columns() -> None:

    original = pd.DataFrame(
        {"Age": [20, 30, 40], "Name": ["Alice", "Bob", "Charlie"], "Marks": [5, 6, 7]}
    )

    expected = pd.DataFrame({"Age": [20, 30, 40]})

    result = drop_unnecessary_columns(original, ["Name", "Marks"])

    pd.testing.assert_frame_equal(result, expected)


def test_drop_duplicates() -> None:

    original = pd.DataFrame(
        {"Age": [20, 30, 20], "Name": ["Alice", "Bob", "Alice"], "Marks  ": [5, 6, 5]}
    )

    expected = pd.DataFrame(
        {"Age": [20, 30], "Name": ["Alice", "Bob"], "Marks  ": [5, 6]}
    )

    result = drop_duplicates(original)

    pd.testing.assert_frame_equal(result, expected)


def test_fix_invalid_monthly_charges() -> None:
    original = pd.DataFrame({"MonthlyCharges": [10, 20, -3]})

    expected = pd.DataFrame({"MonthlyCharges": [10, 20, 15]})

    result = fix_invalid_monthly_charges(original)

    pd.testing.assert_frame_equal(result, expected)


def test_clean() -> None:
    original = pd.DataFrame({"  Age": [10, 20, 20], "Marks": [10, 20, 20]})

    expected = pd.DataFrame({"Age": [10, 20], "Marks": [10, 20]})

    result = clean(original)

    pd.testing.assert_frame_equal(result, expected)
