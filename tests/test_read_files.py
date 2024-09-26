import json
from unittest.mock import Mock, patch

import pandas as pd

from src.read_files import read_csv, read_xls


@patch("pandas.read_csv")
def test_read_csv(mock_read_csv):
    mock_read_csv.return_value = pd.DataFrame({"column1": [1, 2], "column2": ["a", "b"]})

    expected_json = mock_read_csv.return_value.to_json(orient="records", indent=4)
    test_results = json.loads(expected_json)

    assert read_csv("data\\transactions.csv") == test_results


def test_read_xls():
    mock_read_xls = pd.DataFrame({"column1": [1, 2], "column2": ["a", "b"]})
    expected_json = mock_read_xls.to_json(orient="records", indent=4)
    test_result = json.loads(expected_json)

    pd.read_excel = Mock(return_value=mock_read_xls)

    assert read_xls("data\\transactions_excel.xlsx") == test_result
