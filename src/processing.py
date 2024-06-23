def filter_by_state(my_list: list, state_value: str = 'EXECUTED') -> list:
    return [elem for elem in my_list if elem["state"] == state_value]


def sort_by_date(my_list: list, sort_order: bool = True) -> list:
    return sorted(my_list, key=lambda x: x['date'], reverse=sort_order)


# newbie_list = [
#     {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#     {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
#     {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#     {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
# ]
# print(filter_by_state(newbie_list))
# print(sort_by_date(newbie_list))
