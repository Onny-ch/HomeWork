def filter_by_state(my_list: list[dict[str, str]], state_value: str = "EXECUTED") -> list[dict[str, str]]:
    """Фильтрует список словарей по ключу 'state'"""
    state_filtered_list = [elem for elem in my_list if "state" in elem and elem["state"] == state_value]
    return state_filtered_list


def sort_by_date(my_list: list[dict[str, str]], sort_order: bool = False) -> list[dict[str, str]]:
    """Сортирует список словарей по ключу 'date'"""
    return sorted(my_list, key=lambda transaction_data_dict: transaction_data_dict["date"], reverse=sort_order)
