def get_mask_card_number(card_name: str) -> str:
    """Функция, маскирующая номер карты"""
    return f"{card_name[:4]} {card_name[4:6]}** **** {card_name[-4:]}"


def get_mask_account(account_name: str) -> str:
    """Функция, маскирующая номер банковского аккаунта"""
    masc_account = "**" + account_name[-4:]
    return masc_account
