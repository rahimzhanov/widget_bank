import pandas as pd
from typing import List, Any
import logging

logger = logging.getLogger(__name__)


def read_csv_to_list(file_path: str) -> List[Any]:
    """
    Считывает финансовые операции из CSV файла и преобразует в JSON-подобный формат.
    """
    try:
        logger.info(f"Чтение CSV файла: {file_path}")
        df = pd.read_csv(file_path, sep=';')
        data = df.to_dict('records')

        # Преобразуем CSV-формат в JSON-подобный формат
        converted_data = []
        for item in data:
            # Обрабатываем NaN значения
            def get_value(key):
                value = item.get(key)
                if pd.isna(value):  # Проверяем на NaN
                    return None
                # Если число - преобразуем в int, затем в str для полей from/to
                if isinstance(value, (int, float)) and key in ['from', 'to']:
                    return str(int(value))
                # Для остальных числовых полей оставляем как есть
                if isinstance(value, (int, float)):
                    return value
                return value

            converted_item = {
                "id": get_value("id"),
                "state": get_value("state"),
                "date": get_value("date"),
                "description": get_value("description"),
                "from": get_value("from"),
                "to": get_value("to"),
                "operationAmount": {
                    "amount": str(get_value("amount")),
                    "currency": {
                        "name": get_value("currency_name"),
                        "code": get_value("currency_code")
                    }
                }
            }
            # Удаляем None значения
            converted_item = {k: v for k, v in converted_item.items() if v is not None}
            converted_data.append(converted_item)

        logger.info(f"Успешно прочитано и преобразовано {len(converted_data)} записей из CSV")
        return converted_data
    except FileNotFoundError:
        logger.error(f"CSV файл не найден: {file_path}")
        return []
    except Exception as e:
        logger.error(f"Ошибка при чтении CSV файла: {e}")
        return []

def read_excel_to_list(file_path: str) -> List[Any]:
    """
    Считывает финансовые операции из Excel файла и преобразует в JSON-подобный формат.
    """
    try:
        logger.info(f"Чтение Excel файла: {file_path}")
        df = pd.read_excel(file_path)
        data = df.to_dict('records')

        # Преобразуем Excel-формат в JSON-подобный формат
        converted_data = []
        for item in data:
            # Обрабатываем NaN значения
            def get_value(key):
                value = item.get(key)
                if pd.isna(value):  # Проверяем на NaN
                    return None
                # Если число - преобразуем в int, затем в str для полей from/to
                if isinstance(value, (int, float)) and key in ['from', 'to']:
                    return str(int(value))
                # Для остальных числовых полей оставляем как есть
                if isinstance(value, (int, float)):
                    return value
                return value

            converted_item = {
                "id": get_value("id"),
                "state": get_value("state"),
                "date": get_value("date"),
                "description": get_value("description"),
                "from": get_value("from"),
                "to": get_value("to"),
                "operationAmount": {
                    "amount": str(get_value("amount")),
                    "currency": {
                        "name": get_value("currency_name"),
                        "code": get_value("currency_code")
                    }
                }
            }
            # Удаляем None значения
            converted_item = {k: v for k, v in converted_item.items() if v is not None}
            converted_data.append(converted_item)

        logger.info(f"Успешно прочитано и преобразовано {len(converted_data)} записей из Excel")
        return converted_data
    except FileNotFoundError:
        logger.error(f"Excel файл не найден: {file_path}")
        return []
    except Exception as e:
        logger.error(f"Ошибка при чтении Excel файла: {e}")
        return []