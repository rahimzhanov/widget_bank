transactions = [
    {
        "id": 939719570,
    "state": "EXECUTED",
    "date": "2018-06-30T02:08:58.425572",
    "operationAmount": {
        "amount": "9824.07",
        "currency": {
            "name": "USD",
            "code": "USD"
        }
    },
    "description": "Перевод организации",
    "from": "Счет 75106830613657916952",
    "to": "Счет 11776614605963066702"
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {
            "amount": "79114.93",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188"
    },
    {
        "id": 142264568,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {
            "amount": "79114.93",
            "currency": {
                "name": "RUB",
                "code": "RUB"
            }
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188"
    },
]


def filter_by_currency(transactions: list[dict], currency: str) -> iter:
    """
    Фильтрует транзакции по заданной валюте и возвращает итератор.

    :param transactions: Список словарей с транзакциями.
    :param currency: Код валюты для фильтрации (например, "USD").
    :return: Итератор, выдающий транзакции с заданной валютой.
    """
    for transaction in transactions:
        operation_amount = transaction.get("operationAmount", {})
        transaction_currency = operation_amount.get("currency", {}).get("code")
        if transaction_currency == currency:
            yield transaction



# usd_transactions = filter_by_currency(transactions, "USD")
# for _ in range(2):
#     print(next(usd_transactions))


def transaction_descriptions(transactions):
    """
    Генератор, который возвращает описания транзакций по очереди.

    :param transactions: Список словарей с транзакциями
    :yield: Описание транзакции (строка)
    """
    for transaction in transactions:
        yield transaction["description"]


# descriptions = transaction_descriptions(transactions)
#
# # Получаем описания по одному
# print(next(descriptions))  # "Перевод организации"
# print(next(descriptions))  # "Перевод со счета на счет"
# print(next(descriptions))  # "Перевод со счета на счет"

def card_number_generator(start: int, end: int):
    """
    Генератор номеров банковских карт в формате XXXX XXXX XXXX XXXX.

    :param start: Начальный номер карты (от 1)
    :param end: Конечный номер карты (до 9999999999999999)
    :yield: Номер карты в формате XXXX XXXX XXXX XXXX
    """
    for number in range(start, end + 1):
        card_str = f"{number:016d}"
        formatted_card = f"{card_str[:4]} {card_str[4:8]} {card_str[8:12]} {card_str[12:16]}"
        yield formatted_card

# Пример использования
# for card_number in card_number_generator(1, 3):
#             print(card_number)