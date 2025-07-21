from typing import List, Tuple, Union

import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.fixture
def valid_card_numbers() -> List[Tuple[int, str]]:
    return [
        (7000792289606361, "7000 79** **** 6361"),
        (5105105105105100, "5105 10** **** 5100"),
        (4111111111111111, "4111 11** **** 1111"),
        (1234567890123456789, "1234 56** ***** 6789")
    ]


@pytest.fixture
def invalid_card_numbers() -> List[Union[str, int]]:
    return [
        "1234",
        "12345678901234567890",
        "abcdefghijklmnop",
        "1234 5678 9012 345",
        12345
    ]


@pytest.fixture
def valid_account_numbers() -> List[Tuple[int, str]]:
    return [
        (12345678, "**5678"),
        (123400005678, "**5678"),
        (99999999, "**9999")
    ]


@pytest.fixture
def invalid_account_numbers() -> List[Union[str, int]]:
    return [
        123,
        "abc",
        "1234abc"
    ]


def test_valid_card_numbers(valid_card_numbers: List[Tuple[int, str]]) -> None:
    """Тест валидных номеров карт"""
    for number, expected in valid_card_numbers:
        assert get_mask_card_number(number) == expected


def test_invalid_card_numbers(invalid_card_numbers: List[Union[str, int]]) -> None:
    """Тест обработки невалидных номеров карт"""
    for number in invalid_card_numbers:
        with pytest.raises(ValueError):
            if isinstance(number, str):
                if number.isdigit():
                    get_mask_card_number(int(number))
                else:
                    get_mask_card_number(number)
            else:
                get_mask_card_number(number)


def test_valid_account_numbers(valid_account_numbers: List[Tuple[int, str]]) -> None:
    """Тест валидных номеров счетов"""
    for number, expected in valid_account_numbers:
        assert get_mask_account(number) == expected


def test_invalid_account_numbers(invalid_account_numbers: List[Union[str, int]]) -> None:
    """Тест обработки невалидных номеров счетов"""
    for number in invalid_account_numbers:
        with pytest.raises(ValueError):
            if isinstance(number, str):
                if number.isdigit():
                    get_mask_account(int(number))
                else:
                    get_mask_account(number)
            else:
                get_mask_account(number)
