import pandas as pd
from typing import List, Any
import logging

logger = logging.getLogger(__name__)


def read_csv_to_list(file_path: str) -> List[Any]:
    """
    Считывает финансовые операции из CSV файла.

    Args:
        file_path (str): Путь к файлу CSV

    Returns:
        List[Any]: Список словарей с транзакциями
    """
    try:
        logger.info(f"Чтение CSV файла: {file_path}")
        df = pd.read_csv(file_path, sep=';')
        data = df.to_dict('records')
        logger.info(f"Успешно прочитано {len(data)} записей из CSV")
        return data
    except FileNotFoundError:
        logger.error(f"CSV файл не найден: {file_path}")
        return []
    except Exception as e:
        logger.error(f"Ошибка при чтении CSV файла: {e}")
        return []


def read_excel_to_list(file_path: str) -> List[Any]:
    """
    Считывает финансовые операции из Excel файла.

    Args:
        file_path (str): Путь к файлу Excel

    Returns:
        List[Any]: Список словарей с транзакциями
    """
    try:
        logger.info(f"Чтение Excel файла: {file_path}")
        df = pd.read_excel(file_path)
        data = df.to_dict('records')
        logger.info(f"Успешно прочитано {len(data)} записей из Excel")
        return data
    except FileNotFoundError:
        logger.error(f"Excel файл не найден: {file_path}")
        return []
    except Exception as e:
        logger.error(f"Ошибка при чтении Excel файла: {e}")
        return []