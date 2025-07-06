from .masks import get_mask_account, get_mask_card_number
from datetime import datetime

account_info = input()
date_string = input()


def mask_account_card(account_info: str) -> str:
    """
    Маскирует номер карты или счета в переданной строке.
    """

    parts = account_info.split()
    number_card = int(parts[-1])
    if parts[-1].isdigit():
        account_type = " ".join(parts[:-1])
        if parts[0] == "Счет":
            result = f"{account_type[:-1]}: {get_mask_account(number_card)}"
        else:
            result = f"{account_type[:-1]}: {get_mask_card_number(number_card)}"
        return result
    else:
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
