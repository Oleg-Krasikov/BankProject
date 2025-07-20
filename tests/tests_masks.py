import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.fixture
def valid_card_numbers() -> list[tuple[int | str, str]]:
    """Фикстура с валидными номерами карт и ожидаемыми результатами."""
    return [
        # (номер карты, ожидаемый результат)
        (1234567890123456, "1234 56**** 3456"),    # 16 цифр
        (12345678901234567, "1234 56***** 4567"),  # 17 цифр
        (1234567890123456789, "1234 56***** 6789"),  # 19 цифр
        ("1234 5678 9012 3456", "1234 56**** 3456"),  # с пробелами
    ]


@pytest.fixture
def invalid_card_numbers() -> list[int | str]:
    """Фикстура с невалидными номерами карт."""
    return [
        123456789012345,        # слишком короткий
        12345678901234567890,   # слишком длинный
        "",                     # пустая строка
        "abcd efgh ijkl mnop",  # не цифры
    ]


def test_get_mask_card_number_valid(valid_card_numbers: list[tuple[int, str]]) -> None:
    """Тестирует корректную маскировку номеров карт."""
    for card_number, expected in valid_card_numbers:
        assert get_mask_card_number(card_number) == expected


def test_get_mask_card_number_invalid(invalid_card_numbers: list[int]) -> None:
    """Тестирует обработку некорректных номеров карт."""
    for card_number in invalid_card_numbers:
        assert get_mask_card_number(card_number) == "Номер карты должен содержать от 16 до 19 цифр"


@pytest.mark.parametrize(
    "card_number, expected",
    [
        (1000000000000000, "1234 56**** 0000"),    # минимальная длина
        (9999999999999999999, "1234 56***** 9999"),  # максимальная длина
    ],
)
def test_get_mask_card_number_edge_cases(card_number: int, expected: str) -> None:
    """Тестирует граничные случаи."""
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize("account_number, expected", [
    (1000, "Номер счёта должен содержать минимум 4 цифры"),   # минимальная длина
    (1234567890, "**7890"),  # обычный случай
    (9999999999999999, "**9999")  # максимальная длина
])
def test_get_mask_account(account_number: int, expected: str) -> None:
    """Тестирует маскировку номеров счетов с различными входными данными."""
    assert get_mask_account(account_number) == expected


@pytest.fixture
def valid_account_numbers() -> list[tuple]:
    """Фикстура с валидными номерами счетов и ожидаемыми результатами."""
    return [
        (12345678, "**5678"),
        (123400005678, "**5678"),
        (9999, "Номер счёта должен содержать минимум 4 цифры")
    ]


def test_get_mask_account_with_fixture(valid_account_numbers: list[tuple]) -> None:
    """Тестирует маскировку номеров счетов с использованием фикстуры."""
    for account_number, expected in valid_account_numbers:
        assert get_mask_account(account_number) == expected
