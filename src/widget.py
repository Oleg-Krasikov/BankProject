from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_info: str) -> str:
    """
    Маскирует номер карты или счета в переданной строке.
    """

    parts = account_info.split()
    # Проверяем, что последняя часть - число
    if not parts[-1].isdigit():
        return "Некорректные данные"
    try:
        number = int(parts[-1])
        account_type = " ".join(parts[:-1])
        if account_type == "Счет":
            masked_number = f"**{str(number)[-4:]}"
            return f"{account_type} {masked_number}"
        else:
            # Форматирование номера карты: XXXX XX** **** XXXX
            card_number = str(number)
            if len(card_number) != 16:
                return "Некорректные данные"

            masked = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
            return f"{account_type} {masked}"
    except ValueError:
        return "Некорректные данные"


def get_date(date_string: str) -> str:
    """
    Преобразует строку с датой в формате ISO ("2024-03-11T02:26:18.671407")
    в строку формата "ДД.ММ.ГГГГ" ("11.03.2024")
    """
    try:
        dt = datetime.fromisoformat(date_string)
        return dt.strftime("%d.%m.%Y")
    except ValueError as e:
        raise ValueError("Некорректный формат даты") from e
