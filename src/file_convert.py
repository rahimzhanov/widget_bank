import pandas as pd
import json
from typing import Any
import logging

# Настройка логирования
logger = logging.getLogger("file_convert")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('../logs/file_convert.log', encoding="utf-8")
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

# Загрузка переменных из .env-файла

# Путь к CSV файлу
data_operations_csv = '../data/transactions.csv'


def open_csv(path: str) -> list[Any]:
    """
    Открывает и загружает CSV файл.

    Args:
        path (str): Путь к CSV файлу

    Returns:
        List[Any]: Данные из файла или пустой список в случае ошибки
    """
    try:
        logger.info(f"Попытка открыть файл: {path}")
        # Читаем CSV файл и преобразуем в список словарей
        df = pd.read_csv(path)
        data = df.to_dict('records')
        logger.info(f"Файл успешно загружен, получено {len(data)} записей")
        return data

    except FileNotFoundError:
        logger.error(f"Файл '{path}' не найден")
        return []

    except pd.errors.EmptyDataError:
        logger.error(f"Файл '{path}' пуст")
        return []

    except Exception as error:
        logger.error(f"Неизвестная ошибка при открытии файла '{path}': {error}")
        return []


# Путь к Excel файлу вместо JSON
data_operations_exel = '../data/operations.xlsx'

def open_excel(path: str) -> list[Any]:
    """
    Открывает и загружает Excel файл.

    Args:
        path (str): Путь к Excel файлу

    Returns:
        List[Any]: Данные из файла или пустой список в случае ошибки
    """
    try:
        logger.info(f"Попытка открыть файл: {path}")
        # Читаем Excel файл и преобразуем в список словарей
        df = pd.read_excel(path)
        data = df.to_dict('records')
        logger.info(f"Файл успешно загружен, получено {len(data)} записей")
        return data

    except FileNotFoundError:
        logger.error(f"Файл '{path}' не найден")
        return []

    except pd.errors.EmptyDataError:
        logger.error(f"Файл '{path}' пуст")
        return []

    except Exception as error:
        logger.error(f"Неизвестная ошибка при открытии файла '{path}': {error}")
        return []


# Вариант csv
# if __name__ == '__main__':
#     data = open_csv(data_operations)
#     for item in data:
#         result = convert_amount(item)
#         print(result)
#
#
# Вариант exel
# if __name__ == '__main__':
#     data = open_excel(data_operations)
#     for item in data:
#         result = convert_amount(item)
#         print(result)
