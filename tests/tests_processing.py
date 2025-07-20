from datetime import datetime
from typing import Any, Dict, List

import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def sample_transactions() -> List[Dict[str, Any]]:
    """Фикстура предоставляет тестовые данные транзакций"""
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.mark.parametrize(
    "state, expected_count, expected_ids",
    [
        # Проверка стандартного случая (EXECUTED)
        ("EXECUTED", 2, [41428829, 939719570]),
        # Проверка CANCELED
        ("CANCELED", 2, [594226727, 615064591]),
        # Проверка несуществующего статуса
        ("PENDING", 0, []),
        # Проверка пустого списка транзакций
        ("EXECUTED", 0, []),
    ],
)
def test_filter_by_state(
    sample_transactions: List[Dict[str, Any]],
    state: str,
    expected_count: int,
    expected_ids: List[int]
) -> None:
    """Параметризованный тест для функции filter_by_state"""
    # Для последнего тест-кейса используем пустой список
    transactions = sample_transactions if expected_count > 0 else []

    result = filter_by_state(transactions, state)

    # Проверяем количество элементов в результате
    assert len(result) == expected_count

    # Проверяем ID транзакций в результате
    assert [t["id"] for t in result] == expected_ids


def test_filter_by_state_default(sample_transactions: List[Dict[str, Any]]) -> None:
    """Тест проверяет, что функция работает с параметром state по умолчанию"""
    result = filter_by_state(sample_transactions)
    assert len(result) == 2
    assert all(t["state"] == "EXECUTED" for t in result)


@pytest.mark.parametrize(
    "reverse, expected_ids",
    [
        (True, [41428829, 615064591, 594226727, 939719570]),  # По убыванию (новые сначала)
        (False, [939719570, 594226727, 615064591, 41428829])  # По возрастанию (старые сначала)
    ]
)
def test_sort_by_date(
    sample_transactions: List[Dict[str, Any]],
    reverse: bool,
    expected_ids: List[int]
) -> None:
    """Тестирование сортировки по дате с разными параметрами"""
    sorted_data = sort_by_date(sample_transactions, reverse=reverse)
    actual_ids = [item["id"] for item in sorted_data]
    assert actual_ids == expected_ids


def test_sort_by_date_empty_list() -> None:
    """Тестирование сортировки пустого списка"""
    assert sort_by_date([]) == []


def test_sort_by_date_single_item() -> None:
    """Тестирование сортировки списка с одним элементом"""
    single_item = [{"id": 1, "date": "2020-01-01T00:00:00"}]
    assert sort_by_date(single_item) == single_item


def test_sort_by_date_with_missing_date_field() -> None:
    """Тестирование обработки отсутствующего поля date"""
    test_data: List[Dict[str, Any]] = [{"id": 1}]
    with pytest.raises(KeyError):
        sort_by_date(test_data)
