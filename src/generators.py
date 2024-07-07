def filter_by_currency(my_list, my_code="USD"):
    return (dict_elem for dict_elem in my_list if dict_elem["operationAmount"]["currency"]["code"] == my_code)


def transaction_descriptions(my_list):
    return (dict_elem["description"] for dict_elem in my_list)


def card_number_generator(start, stop):

    return
