def filter_by_state(list_of_dict: list, state: str = 'EXECUTED') -> list:
    """Функция, возвращающая список только тех словарей,
       где ключу 'state' соответствуют аргументу state"""
    state_exec_list_dicts = []
    for dict in list_of_dict:
        if dict.get("state") == state:
            state_exec_list_dicts.append(dict)
        if "state" not in dict:
            return list_of_dict
    return state_exec_list_dicts


def sort_by_date(list_of_dict: list, sort_: bool = True) -> list:
    """Функция, возвращающая список словарей, которые сортированы по дате"""
    list_of_dict_sort_date = sorted(list_of_dict, key=lambda x: x["date"], reverse=sort_)
    return list_of_dict_sort_date


print(sort_by_date(
    [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 88828829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
        ]
    )
)