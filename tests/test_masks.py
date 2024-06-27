from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number(card_number_strings):
    for elem in card_number_strings:
        assert get_mask_card_number(elem) == f"{elem[:4]} {elem[4:6]}** **** {elem[-4:]}"


def test_get_mask_account(accounts_strings):
    for elem in accounts_strings:
        assert get_mask_account(elem) == f"**{elem[-4:]}"
