import src.masks


def mask_account_card(string: str) -> str:
    """Функция, которая обрабатывает информацию о картах и счетах"""

    if "Счет" in string:
        account_number = string[-20:]
        return string[:-20] + src.masks.get_mask_account(account_number)
    else:
        card_number = "".join(string[-16:].split())
        return string[:-16] + src.masks.get_mask_card_number(card_number)


print(mask_account_card("Visa Platinum 7000792289606361"))


def get_data(info_data: str) -> str:
    """Функция преобразования даты и времени"""

    data_day = info_data.split("T")[0]
    return f"{data_day.split('-')[-1]}.{data_day.split('-')[-2]}.{data_day.split('-')[-3]}"


print(get_data("2018-07-11T02:26:18.671407"))
