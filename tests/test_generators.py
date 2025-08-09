import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


# Фикстура с тестовыми транзакциями
@pytest.fixture
def sample_transactions():
    return [
        {"operationAmount": {"currency": {"code": "USD"}}},
        {"operationAmount": {"currency": {"code": "EUR"}}},
        {"operationAmount": {"currency": {"code": "GBP"}}},
        {"operationAmount": {"currency": {"code": "USD"}}},
    ]


# Параметризованные тесты
@pytest.mark.parametrize("currency, expected_count", [("USD", 2), ("EUR", 1), ("GBP", 1), ("RUB", 0)])
def test_filter_by_currency(sample_transactions, currency, expected_count):
    """Тестирование фильтрации по разным валютам"""
    result = list(filter_by_currency(sample_transactions, currency))
    assert len(result) == expected_count
    if expected_count > 0:
        assert all(t["operationAmount"]["currency"]["code"] == currency for t in result)


def test_empty_list():
    """Тест обработки пустого списка"""
    assert list(filter_by_currency([], "USD")) == []


def test_missing_currency_field():
    """Тест обработки транзакций с отсутствующим полем валюты"""
    with pytest.raises(KeyError):
        list(filter_by_currency([{"operationAmount": {}}], "USD"))


@pytest.fixture
def normal_transactions():
    """Фикстура с обычными транзакциями"""
    return [{"description": "Payment for services", "amount": 100}, {"description": "Grocery shopping", "amount": 50}]


@pytest.fixture
def empty_transactions():
    """Фикстура с пустым списком"""
    return []


@pytest.fixture
def large_transactions():
    """Фикстура с большим количеством транзакций"""
    return [{"description": f"Transaction {i}"} for i in range(1000)]


@pytest.fixture
def missing_description_transaction():
    """Фикстура с транзакцией без описания"""
    return [{"amount": 100}]


@pytest.fixture
def invalid_transactions():
    """Фикстура с некорректными элементами"""
    return ["not a dict", 123]


@pytest.mark.parametrize(
    "transactions_fixture, expected",
    [
        ("normal_transactions", ["Payment for services", "Grocery shopping"]),
        ("empty_transactions", []),
        ("large_transactions", [f"Transaction {i}" for i in range(1000)]),
    ],
    ids=["normal_transactions", "empty_list", "large_number_of_transactions"],
)
def test_transaction_descriptions(request, transactions_fixture, expected):
    """Параметризованный тест основных сценариев"""
    transactions = request.getfixturevalue(transactions_fixture)
    result = list(transaction_descriptions(transactions))
    assert result == expected


@pytest.mark.parametrize(
    "transactions_fixture, exception",
    [
        ("missing_description_transaction", KeyError),
        ("invalid_transactions", TypeError),
    ],
    ids=["missing_description", "invalid_elements"],
)
def test_error_cases(request, transactions_fixture, exception):
    """Параметризованный тест обработки ошибок"""
    transactions = request.getfixturevalue(transactions_fixture)
    with pytest.raises(exception):
        list(transaction_descriptions(transactions))


@pytest.mark.parametrize(
    "start, end, expected",
    [
        (
            1,
            5,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
                "0000 0000 0000 0004",
                "0000 0000 0000 0005",
            ],
        ),
        (9999999999999998, 9999999999999999, ["9999 9999 9999 9998", "9999 9999 9999 9999"]),
    ],
    ids=["small_range", "upper_bound"],
)
def test_valid_ranges(start, end, expected):
    """Тест корректных диапазонов"""
    result = list(card_number_generator(start, end))
    assert result == expected


@pytest.mark.parametrize(
    "start, end",
    [(-1, 5), (5, 1), (1, 99999999999999999)],  # Отрицательный старт  # Старт больше конца  # Переполнение максимума
    ids=["negative_start", "start_gt_end", "overflow"],
)
def test_invalid_ranges(start, end):
    """Тест обработки невалидных диапазонов"""
    with pytest.raises(ValueError):
        list(card_number_generator(start, end))


def test_format_correctness():
    """Тест корректности форматирования"""
    result = next(card_number_generator(1234567812345678, 1234567812345678))
    assert result == "1234 5678 1234 5678"
    assert len(result) == 19  # 16 цифр + 3 пробела
