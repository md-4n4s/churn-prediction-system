import pandas as pd

from src.preprocessing.aggregator import *


def test_aggregate_call_minutes() -> None:

    original = pd.DataFrame(
        {
            "CustomerID": [1, 1, 1, 1, 1, 2, 2, 2, 2, 2],
            "Month": [
                "2023-08-31",
                "2023-09-30",
                "2023-10-31",
                "2023-11-30",
                "2023-12-31",
                "2023-08-31",
                "2023-09-30",
                "2023-10-31",
                "2023-11-30",
                "2023-12-31",
            ],
            "CallMinutes": [20, 6, 15, 2, 7, 10, 8, 4, 0, 8],
        }
    )

    expected = pd.DataFrame(
        {
            "CustomerID": [1, 1, 1, 1, 1, 2, 2, 2, 2, 2],
            "Month": [
                "2023-08-31",
                "2023-09-30",
                "2023-10-31",
                "2023-11-30",
                "2023-12-31",
                "2023-08-31",
                "2023-09-30",
                "2023-10-31",
                "2023-11-30",
                "2023-12-31",
            ],
            "CallMinutes_Mean": [10.0, 10.0, 10.0, 10.0, 10.0, 6.0, 6.0, 6.0, 6.0, 6.0],
            "CallMinutes_Range": [18, 18, 18, 18, 18, 10, 10, 10, 10, 10],
            "CallMinutes_Mean3M": [8.0, 8.0, 8.0, 8.0, 8.0, 4.0, 4.0, 4.0, 4.0, 4.0],
            "CallMinutes_Change": [13, 13, 13, 13, 13, 2, 2, 2, 2, 2],
        }
    )

    result = aggregate_call_minutes(original)

    pd.testing.assert_frame_equal(result, expected)


def test_aggregate_data_usage() -> None:
    original = pd.DataFrame(
        {
            "CustomerID": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            "Month": [
                "2023-01-31",
                "2023-02-28",
                "2023-03-31",
                "2023-04-30",
                "2023-05-31",
                "2023-06-30",
                "2023-07-31",
                "2023-08-31",
                "2023-09-30",
                "2023-10-31",
                "2023-11-30",
                "2023-12-31",
            ],
            "DataUsageGB": [20, 20, 20, 20, 20, 20, 10, 10, 10, 10, 10, 10],
        }
    )

    expected = pd.DataFrame(
        {
            "CustomerID": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            "Month": [
                "2023-01-31",
                "2023-02-28",
                "2023-03-31",
                "2023-04-30",
                "2023-05-31",
                "2023-06-30",
                "2023-07-31",
                "2023-08-31",
                "2023-09-30",
                "2023-10-31",
                "2023-11-30",
                "2023-12-31",
            ],
            "DataUsageGB_Mean": [
                15.0,
                15.0,
                15.0,
                15.0,
                15.0,
                15.0,
                15.0,
                15.0,
                15.0,
                15.0,
                15.0,
                15.0,
            ],
            "DataUsageGB_Mean6M": [
                10.0,
                10.0,
                10.0,
                10.0,
                10.0,
                10.0,
                10.0,
                10.0,
                10.0,
                10.0,
                10.0,
                10.0,
            ],
            "DataUsageGB_Change": [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
        }
    )

    result = aggregate_data_usage(original)

    pd.testing.assert_frame_equal(result, expected)


def test_aggregate_sms_count() -> None:
    original = pd.DataFrame(
        {
            "CustomerID": [1, 1, 1, 1, 1, 2, 2, 2, 2, 2],
            "SMSCount": [20, 10, 10, 5, 5, 10, 10, 20, 20, 15],
        }
    )

    expected = pd.DataFrame(
        {
            "CustomerID": [1, 1, 1, 1, 1, 2, 2, 2, 2, 2],
            "SMSCount_Mean": [
                10.0,
                10.0,
                10.0,
                10.0,
                10.0,
                15.0,
                15.0,
                15.0,
                15.0,
                15.0,
            ],
        }
    )

    result = aggregate_sms_count(original)

    pd.testing.assert_frame_equal(result, expected)


def test_aggregate_complaints() -> None:
    original = pd.DataFrame(
        {
            "CustomerID": [1, 1, 1, 1, 1, 2, 2, 2, 2, 2],
            "Complaints": [20, 10, 10, 5, 5, 10, 10, 20, 20, 15],
        }
    )

    expected = pd.DataFrame(
        {
            "CustomerID": [1, 1, 1, 1, 1, 2, 2, 2, 2, 2],
            "Complaints_Mean": [
                10.0,
                10.0,
                10.0,
                10.0,
                10.0,
                15.0,
                15.0,
                15.0,
                15.0,
                15.0,
            ],
        }
    )

    result = aggregate_complaints(original)

    pd.testing.assert_frame_equal(result, expected)
