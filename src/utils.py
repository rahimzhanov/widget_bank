from typing import Any
import requests
import json
from src.external_api import convert_rub_currency
from dotenv import load_dotenv
import logging
from src.file_operations import read_csv_to_list, read_excel_to_list  #

# Настройка базового логирования
# logging.basicConfig(
#     level=logging.INFO,
#     format='%(asctime)s - %(levelname)s - %(message)s',
#     handlers=[
#         logging.FileHandler("utils.log", encoding="utf-8"),
# #         logging.StreamHandler()
# #     ]
# # )

logger = logging.getLogger("utils")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('./logs/utils.log', encoding="utf-8")
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

# Загрузка переменных из .env-файла
load_dotenv()

# Путь к CSV файлу
data_operations_csv = '../data/transactions.csv'
# Путь к Excel файлу
data_operations_excel = '../data/transactions_excel.xlsx'

transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]


data_operations = '../data/operations.json'


def open_json(path: str) -> list[Any]:
    """
    Открывает и загружает JSON файл.
    """
    try:
        logger.info(f"Попытка открыть файл: {path}")
        with open(path, 'r', encoding="utf-8") as f:
            data = json.load(f)
        logger.info(f"Файл успешно загружен, получено {len(data)} записей")
        return data
    except FileNotFoundError:
        logger.error(f"Файл '{path}' не найден")
        return []
    except json.JSONDecodeError as e:
        logger.error(f"Ошибка декодирования JSON в файле '{path}': {e}")
        return []
    except Exception as error:
        logger.error(f"Неизвестная ошибка при открытии файла '{path}': {error}")
        return []


def convert_amount(item):
    """
    Конвертирует сумму транзакции в рубли.
    """
    try:
        # Для CSV данных (ваша структура)
        if 'currency_code' in item and 'amount' in item:
            currency = item['currency_code']
            amount = item['amount']
        # Для оригинальных JSON данных
        elif 'operationAmount' in item and isinstance(item['operationAmount'], dict):
            currency = item['operationAmount']['currency']['code']
            amount = item['operationAmount']['amount']
        # Для плоского CSV с точками
        elif 'operationAmount.currency.code' in item:
            currency = item['operationAmount.currency.code']
            amount = item['operationAmount.amount']
        else:
            return "Ошибка: неверный формат данных транзакции"

        if currency == "RUB":
            return f'Сумма транзакции - {float(amount)} руб.'
        else:
            result = convert_rub_currency(currency, amount)
            return f'Сумма транзакции - {result} руб.'

    except KeyError:
        return "Ошибка: неверный формат данных транзакции"
    except Exception:
        return "Ошибка при конвертации суммы"

# Вариант 1: работа с JSON файлом
# if __name__ == '__main__':
#     data = open_json(data_operations)
#     for item in data:
#         result = convert_amount(item)
#         print(result)

# Вариант 2: работа с CSV файлом
# if __name__ == '__main__':
#     data = read_csv_to_list(data_operations_csv)  # Используем новую функцию
#     for item in data:
#         result = convert_amount(item)
#         print(result)

# Вариант 3: работа с Excel файлом
# if __name__ == '__main__':
#     data = read_excel_to_list(data_operations_excel)  # Используем новую функцию
#     for item in data:
#         result = convert_amount(item)
#         print(result)

