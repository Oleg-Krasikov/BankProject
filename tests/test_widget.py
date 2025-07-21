import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "account_info, expected",
    [
        ("Счет 1234567890123456", "Счет **3456"),
        ("Visa Platinum 9999888877776666", "Visa Platinum 9999 88** **** 6666"),
        ("Maestro 1234567890123456", "Maestro 1234 56** **** 3456"),
    ],
)
def test_mask_account_card_valid(account_info: str, expected: str) -> None:
    """Тестирует корректный разбор и маскировку строки с информацией о карте/счете"""
    assert mask_account_card(account_info) == expected


@pytest.mark.parametrize(
    "invalid_info",
    [
        "Invalid Info",
        "Card",
        "123",
        "Счет abc",
        "Visa Short 123456789012",  # слишком короткий номер
    ],
)
def test_mask_account_card_invalid(invalid_info: str) -> None:
    """Тестирует обработку некорректных входных данных"""
    assert mask_account_card(invalid_info) == "Некорректные данные"


@pytest.mark.parametrize(
    "date_string, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2023-12-31T23:59:59.999999", "31.12.2023"),
        ("2022-01-01T00:00:00.000000", "01.01.2022"),
    ],
)
def test_get_date_valid(date_string: str, expected: str) -> None:
    """Тестирует корректное преобразование даты"""
    assert get_date(date_string) == expected


@pytest.mark.parametrize(
    "invalid_date",
    [
        "invalid-date-string",
        "2024-13-01",
        "not-a-date",
    ],
)
def test_get_date_invalid(invalid_date: str) -> None:
    """Тестирует обработку некорректного формата даты"""
    with pytest.raises(ValueError):
        get_date(invalid_date)
