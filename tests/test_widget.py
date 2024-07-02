import pytest

from src.widget import get_data, mask_account_card


@pytest.mark.parametrize("account_data, expected_result", [
    ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
    ("Счет 64686473678894779589", "Счет **9589"),
    ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
    ("Счет 35383033474447895560", "Счет **5560"),
    ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
    ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
    ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
    ("Счет 73654108430135874305", "Счет **4305")
])
def test_mask_account_card(account_data, expected_result):
    assert mask_account_card(account_data) == expected_result


@pytest.mark.parametrize("transaction_data, expected_result", [
    ("transaction_data_first", "11.07.2018"),
    ("transaction_data_second", "30.06.2018"),
    ("transaction_data_third", "12.09.2018"),
])
def test_get_data(transaction_data, expected_result, request):
    requested_transaction_data = request.getfixturevalue(transaction_data)
    assert get_data(requested_transaction_data) == expected_result
