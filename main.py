from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.widget import get_data, mask_account_card

test_list_of_dict = [
        {'id': '41428829', 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': '939719570', 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': '594226727', 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': '615064591', 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]


if __name__ == '__main__':
    print(get_mask_card_number("7000792289606361"))
    print(get_mask_account("73654108430135874305"))
    print(get_data("2018-07-11T02:26:18.671407"))
    print(mask_account_card("Maestro 1596837868705199".strip()))
    print(mask_account_card("Счет 64686473678894779589".strip()))
    print(mask_account_card("MasterCard 7158300734726758".strip()))
    print(mask_account_card("Счет 35383033474447895560".strip()))
    print(mask_account_card("Visa Classic 6831982476737658".strip()))
    print(mask_account_card("Visa Platinum 8990922113665229".strip()))
    print(mask_account_card("Visa Gold 5999414228426353".strip()))
    print(mask_account_card("Счет 73654108430135874305".strip()))
    print(filter_by_state(test_list_of_dict, "EXECUTED"))
    print(filter_by_state(test_list_of_dict, "CANCELED"))
    print(sort_by_date(test_list_of_dict, False))
    print(sort_by_date(test_list_of_dict, True))
