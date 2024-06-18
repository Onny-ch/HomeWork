from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_data: str) -> str:
    """Функция маскировки карты или счета"""
    if account_data[:4].lower() == "счет":
        masks_account = get_mask_account(account_data[5:])
        return f"{account_data[:4]} {masks_account}"
    else:
        masks_card = get_mask_card_number(account_data[-16:])
        return f"{account_data[:-17]} {masks_card}"


def get_data(data: str) -> str:
    """Функция получения даты"""
    year, month, day = data[0:4], data[5:7], data[8:10]
    return f"{day}.{month}.{year}"
