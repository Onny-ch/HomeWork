def get_mask_card_number(card_name: str) -> str:
    """Функция, маскирующая номер карты"""
    masc_card_number = card_name[:4] + " " + card_name[4:6] + "** **** " + card_name[-4:]
    # masc_card_number = [card_name[i:i+4] for i in range(0, len(card_name), 4)]
    # masc_card_number[1] = masc_card_number[1][:2] + '**'
    # masc_card_number[2] = '****'
    # return ' '.join(masc_card_number)
    return masc_card_number


def get_mask_account(account_name: str) -> str:
    """Функция, маскирующая номер банковского аккаунта"""
    masc_account = "**" + account_name[-4:]
    return masc_account
