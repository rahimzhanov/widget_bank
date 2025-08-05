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

#print(filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))
#print(sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))