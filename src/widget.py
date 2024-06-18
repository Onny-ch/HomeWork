def mask_account_card():
    """Функция маскировки карты или счета"""
    pass


def get_data(data: str) -> str:
    """Функция получения даты"""
    year, month, day = data[0:4], data[5:7], data[8:10]
    return f"{day}.{month}.{year}"


print(get_data("2018-07-11T02:26:18.671407"))
