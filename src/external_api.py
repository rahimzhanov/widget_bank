import os
import json
from typing import Any

import requests
from dotenv import load_dotenv


# Загрузка переменных из .env-файла
load_dotenv()


def convert_rub_currency(currency: str, amount: str) -> float:
    """
    Конвертирует сумму из указанной валюты в рубли.

    :param currency: Исходная валюта (например, "USD", "EUR")
    :param amount: Сумма для конвертации
    :return: Сумма в рублях как float
    """
    to = "RUB"
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={currency}&amount={amount}"

    headers = {
        "apikey": os.getenv("API_KEY")
    }

    try:
        response = requests.request("GET", url, headers=headers, data={})
        if response.status_code == 429:
            return float(amount)  # Возвращаем исходную сумму как float
        else:
            result = response.json().get("result")
            return float(result) if result is not None else float(amount)
    except Exception:
        return float(amount)  # При любой ошибке возвращаем float


# if __name__ == '__main__':
#     print(convert_rub_currency("EUR", "100"))
