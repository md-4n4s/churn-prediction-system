import pandas as pd
import pytest

from src.preprocessing.exceptions import *
from src.preprocessing.validator import *


def test_check_missing_values() -> None:
    with pytest.raises(InvalidFieldException):
        check_missing_values(pd.DataFrame({"a": [1, None], "b": [2, 2]}), "a")


def test_check_duplicated() -> None:
    with pytest.raises(InvalidFieldException):
        check_duplicated(pd.DataFrame({"a": [1, 1], "b": [1, 2]}), "a")


def test_check_dtypes() -> None:
    with pytest.raises(InvalidFieldException):
        check_dtype(pd.DataFrame({"a": [1, 2], "b": [1, 2]}), "a", "str")


def test_check_unique_values() -> None:
    with pytest.raises(InvalidFieldException):
        check_unique_values(pd.DataFrame({"a": [1, 2], "b": [1, 2]}), "a", 1)


def test_check_negative() -> None:
    with pytest.raises(InvalidFieldException):
        check_negative(pd.DataFrame({"a": [1, 2], "b": [1, -2]}), "b")


def test_check_datetime() -> None:
    with pytest.raises(InvalidFieldException):
        check_datetime(pd.DataFrame({"a": [1, 2], "b": [1, 2]}), "a")


def test_check_columns() -> None:
    with pytest.raises(MissingColumnException):
        check_columns(pd.DataFrame({"a": [1, 2], "b": [1, 2]}), ["a", "b", "c"])


def test_validate_simple() -> None:
    with pytest.raises(InvalidFieldException):
        validate_simple(pd.DataFrame({"a": [1, 2], "b": [1, None]}), "b", "int")


def test_validate_id() -> None:
    with pytest.raises(InvalidFieldException):
        validate_id(pd.DataFrame({"a": [1, 2], "b": [1, 2]}), "a", "str")


def test_validate_category() -> None:
    with pytest.raises(InvalidFieldException):
        validate_category(pd.DataFrame({"a": [1, 2], "b": [1, 2]}), "a", "int", 1)


def test_validate_positive() -> None:
    with pytest.raises(InvalidFieldException):
        validate_positive(pd.DataFrame({"a": [1, -2], "b": [1, 2]}), "a", "int")
