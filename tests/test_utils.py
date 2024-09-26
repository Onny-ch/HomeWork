import json
from unittest.mock import Mock, patch

from src.utils import count_descriptions, financial_transactions_data, get_transactions_amount, search_in_transactions


def test_financial_transactions_data_false_path():
    assert financial_transactions_data("data/operati.json") == []


@patch("json.load")
def test_financial_transactions_data_not_list(mock_data):
    mock_data.return_value = {}
    assert financial_transactions_data("data/operations.json") == []


def test_financial_transactions_data_file_empty():
    json.load = Mock(return_value=[])
    assert financial_transactions_data("data/operations.json") == []


def test_get_transactions_amount_rub_currency():
    trans = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }
    assert get_transactions_amount(trans) == 31957.58


@patch("src.utils.currency_conversion")
def test_get_transactions_amount_other_currency(mock_convert):
    trans = {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560",
    }
    mock_convert.return_value = 739923.30
    assert get_transactions_amount(trans) == 739923.30


def test_search_in_transactions(account_transaction):
    after_search_transactions_list = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]
    assert search_in_transactions(account_transaction, "органиЗАЦИИ") == after_search_transactions_list


def test_count_descriptions(account_transaction):
    assert count_descriptions(account_transaction, ["организац"]) == {"Перевод организации": 2}
