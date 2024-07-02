import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize('card_number, expected_result', [
    ('card_string_first', '7000 79** **** 6361'),
    ('card_string_second', '1596 83** **** 5199'),
    ('card_string_third', '7158 30** **** 6758')
])
def test_get_mask_card_number(card_number, expected_result, request):
    card_string = request.getfixturevalue(card_number)
    assert get_mask_card_number(card_string) == expected_result


@pytest.mark.parametrize('account_number, expected_result', [
    ('account_string_first', '**4305'),
    ('account_string_second', '**9589'),
    ('account_string_third', '**5560')
])
def test_get_mask_account(account_number, expected_result, request):
    account_string = request.getfixturevalue(account_number)
    assert get_mask_account(account_string) == expected_result
