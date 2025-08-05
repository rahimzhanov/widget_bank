from typing import List, Dict
from datetime import datetime


def filter_by_state(data: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Фильтрует словари по ключу state, оставляя только те, где значение равно переданному state.

    Args:
        data: Список словарей, содержащих ключ 'state'.
        state: Значение для фильтрации (по умолчанию 'EXECUTED').

    Returns:
        Новый список словарей, где значение у ключа 'state' соответствует переданному.
    """
    result = []

    for item in data:
        if item.get("state") == state:
            result.append(item)
    return result


def sort_by_date(data: List[Dict], reverse: bool = True) -> List[Dict]:
    """
    Сортирует список словарей по дате (ключ 'date').

    Args:
        data: Список словарей, содержащих ключ 'date' в формате ISO
        reverse: Если True (по умолчанию) - сортировка по убыванию (новые сначала),
                 Если False - по возрастанию (старые сначала)

    Returns:
        Новый отсортированный список словарей
    """
    return sorted(
        data,
        key=lambda x: datetime.fromisoformat(x["date"]),
        reverse=reverse
    )
