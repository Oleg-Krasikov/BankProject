from datetime import datetime
from typing import Any, Dict, List

input_data = List[Dict[str, Any]]
data = List[Dict[str, Any]]


def filter_by_state(transactions: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """
    Фильтрует список транзакций по указанному статусу.
    """
    return [transaction for transaction in transactions if transaction.get("state") == state]


# Фильтрация с параметром по умолчанию
# filtered = filter_by_state(input_data)
# print(filtered)

# Фильтрация с указанием статуса
# filtered_canceled = filter_by_state(input_data, 'CANCELED')
# print(filtered_canceled)


def sort_by_date(data: list[dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    """
    Сортирует список словарей по дате в указанном порядке
    """

    def get_date(item: Dict[str, Any]) -> datetime:
        # Преобразуем строку даты в объект datetime
        return datetime.fromisoformat(item["date"])

    # Сортируем данные с использованием ключа
    sorted_data = sorted(data, key=get_date, reverse=reverse)
    return sorted_data


# print(sort_by_date(data)) # по умолчанию
# print(sort_by_date(data, reverse=False))  # по возрастанию
