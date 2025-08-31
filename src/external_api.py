import os
from typing import Any
import  requests
import json
from dotenv import load_dotenv

# Загрузка переменных из .env-файла
load_dotenv()

def convert_rub_currency(currency: str, amount: str) -> Any:
    to = "RUB"
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={currency}&amount={amount}"

    headers = {
        "apikey": os.getenv("API_KEY")
    }

    response = requests.request("GET", url, headers=headers, data={})
    if response.status_code == 429:
        return "Количество запросов превысило 100, API не работает!"
    else:
        return response.json().get("result")

if __name__ == '__main__':
    print(convert_rub_currency("EUR", "100"))