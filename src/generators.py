from typing import Iterable, Iterator, Dict, Generator


def filter_by_currency(transactions: list[dict], currency: str) -> filter:
    """
    Фильтрует транзакции по заданной валюте и возвращает итератор
    """
    return filter(lambda x: x["operationAmount"]["currency"]["code"] == currency, transactions)


def transaction_descriptions(transactions: Iterable[Dict]) -> Iterator[str]:
    """Генератор, который возвращает описания транзакций из списка операций"""
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, end: int) -> Generator[str, None, None]:
    """
    Генератор номеров банковских карт в формате XXXX XXXX XXXX XXXX.
    Диапазон генерации: от start до end включительно.
    """
    if start < 0 or end < 0:
        raise ValueError("start and end must be positive")
    if start > end:
        raise ValueError("start must be less than or equal to end")
    if end > 9999999999999999:
        raise ValueError("end exceeds maximum card number value")

    for number in range(start, end + 1):
        num_str = f"{number:016d}"
        yield f"{num_str[:4]} {num_str[4:8]} {num_str[8:12]} {num_str[12:16]}"
