import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(account_transaction):
    usd_transactions = [
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
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

    assert filter_by_currency(account_transaction) == usd_transactions


def test_transaction_descriptions(account_transaction):
    descriptions = transaction_descriptions(account_transaction)

    assert next(descriptions) == "Перевод организации"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод с карты на карту"
    assert next(descriptions) == "Перевод организации"


@pytest.mark.parametrize(
    "start_value, stop_value, expected", [(1, 4, "card_numbers_1"), (111872, 111875, "card_numbers_2")]
)
def test_card_number_generator(start_value, stop_value, expected, request):
    card_number = card_number_generator(start_value, stop_value)
    expected_card_number = request.getfixturevalue(expected)

    assert next(card_number) == next(expected_card_number)
    assert next(card_number) == next(expected_card_number)
    assert next(card_number) == next(expected_card_number)
    assert next(card_number) == next(expected_card_number)
