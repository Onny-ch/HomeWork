import pytest


@pytest.fixture
def card_number_strings():
    return ["7000792289606361", "1596837868705199", "7158300734726758",
            "6831982476737658", "8990922113665229", "5999414228426353"]


@pytest.fixture
def accounts_strings():
    return ["73654108430135874305", "64686473678894779589", "35383033474447895560", "73654108430135874305"]


@pytest.fixture
def transaction_data():
    return ["2018-07-11T02:26:18.671407", "2018-06-30T02:08:58.425572",
            "2018-09-12T21:27:25.241689", "2018-10-14T08:21:33.419441"]


@pytest.fixture
def account_transaction_data():
    return [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]
