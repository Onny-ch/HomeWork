def filter_by_currency(my_list, my_code="USD"):
    """
    Функция, возвращающая итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной
    """
    for x in (dict_elem for dict_elem in my_list if dict_elem["operationAmount"]["currency"]["code"] == my_code):
        yield x


def transaction_descriptions(my_list):
    """Функция, анализирующая информацию о транзакциях и возвращающая описание каждой операции по очереди"""
    for x in (dict_elem["description"] for dict_elem in my_list):
        yield x


def card_number_generator(start, stop):
    """Функция, генерирующая номер банковской карты в соответствии с начальным и конечным значением диапазона"""
    count, card_num = start, start
    while count <= stop:
        cnd = "".join("0" for _ in range(16 - len(str(card_num)))) + str(card_num)
        yield f"{cnd[:4]} {cnd[4:8]} {cnd[8:12]} {cnd[12:]}"
        count += 1
        card_num += 1
