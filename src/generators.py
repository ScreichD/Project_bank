from tests.conftest import transactions


def filter_by_currency(transaction_list, currency):
    for transaction in transaction_list:
        if transaction.get("operationAmount", [{}]).get("currency", [{}]).get("code", [{}]) == currency:
            yield transaction


usd_transactions = filter_by_currency(transactions, "USD")
try:
    for i in range(len(transactions)):
        print(next(usd_transactions))

except StopIteration:
    pass


def transaction_descriptions(transaction_list):
    for transaction in transaction_list:
        yield transaction.get("description")


descriptions = transaction_descriptions(transactions)
for _ in range(len(transactions)):
    print(next(descriptions))


def card_number_generator(start: int, end: int) -> str:
    """Функция генерирует номера карт"""
    for number in range(start, end + 1):
        card_number = str(number)
        while len(card_number) < 16:
            card_number = "0" + card_number

        formatted_card_number = f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:16]}"

        yield (formatted_card_number)


# gen_number = card_number_generator(1,3)
# print(next(gen_number))
# print(next(gen_number))
# print(next(gen_number))
