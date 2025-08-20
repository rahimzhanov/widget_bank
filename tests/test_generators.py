import  pytest
from src.generators import filter_by_currency, card_number_generator, transaction_descriptions

full_test_data = [
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

expected_usd = [
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
]

expected_rub = [
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


@pytest.mark.parametrize("filter_curr, expected", [
    ("USD", expected_usd),
    ("RUB", expected_rub),
    ({}, [])
])

def test_filter_by_currency(filter_curr, expected):
    assert list(filter_by_currency(full_test_data, filter_curr)) == expected


# Параметризованный тест
@pytest.mark.parametrize("trans_input, expected", [
    (full_test_data, ["Перевод организации", "Перевод со счета на счет", "Перевод со счета на счет"]),
    ([full_test_data[0]], ["Перевод организации"]),
    ([full_test_data[1], full_test_data[2]], ["Перевод со счета на счет", "Перевод со счета на счет"]),
    ([],[]),
])


def test_transaction_descriptions(trans_input, expected):
    """
    Параметризованный тест: проверяет, что функция возвращает корректные описания транзакций.
    """
    assert list(transaction_descriptions(trans_input)) == expected


@pytest.mark.parametrize(
    "start, end, expected_first, expected_last, expected_count",
    [
        # Случай 1: от 1 до 1 — один элемент
        (1, 1, "0000 0000 0000 0001", "0000 0000 0000 0001", 1),
        # Случай 2: от 1 до 3 — три элемента
        (1, 3, "0000 0000 0000 0001", "0000 0000 0000 0003", 3),
        # Случай 3: от 9999999999999997 до 9999999999999999 — близко к максимуму
        (
            9999999999999997,
            9999999999999999,
            "9999 9999 9999 9997",
            "9999 9999 9999 9999",
            3
        ),
        # Случай 4: от 100 до 102 — средние значения
        (100, 102, "0000 0000 0000 0100", "0000 0000 0000 0102", 3),
        # Случай 5: диапазон из одного "большого" числа
        (1234567890123456, 1234567890123456, "1234 5678 9012 3456", "1234 5678 9012 3456", 1),
    ]
)
def test_card_number_generator_parametrized(start, end, expected_first, expected_last, expected_count):
    """
    Параметризованный тест: проверяет, что генератор корректно форматирует номера карт
    и правильно работает с разными диапазонами.
    """
    generator = card_number_generator(start, end)
    result_list = list(generator)

    # Проверка: количество сгенерированных номеров
    assert len(result_list) == expected_count, (
        f"Ожидалось {expected_count} номеров, получено {len(result_list)}"
    )

    # Проверка: первый номер
    if expected_count > 0:
        assert result_list[0] == expected_first, (
            f"Первый номер не совпадает: ожидалось {expected_first}, получено {result_list[0]}"
        )

        # Проверка: последний номер
        assert result_list[-1] == expected_last, (
            f"Последний номер не совпадает: ожидалось {expected_last}, получено {result_list[-1]}"
        )

    # Проверка формата: каждый номер должен быть в формате XXXX XXXX XXXX XXXX
    for card_number in result_list:
        parts = card_number.split()
        assert len(parts) == 4, f"Неверный формат: {card_number} — должно быть 4 части"
        assert all(len(part) == 4 and part.isdigit() for part in parts), (
            f"Некорректная часть номера: {card_number}"
        )