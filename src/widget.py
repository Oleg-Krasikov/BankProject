from datetime import datetime

account_info = input(str())
date_string = input(str())


def mask_account_card(account_info: str) -> str:
    """
    Маскирует номер карты или счета в переданной строке.
    """

    def mask_card_number(card_number: str) -> str:
        """Маскирует номер карты, оставляя первые 6 и последние 4 цифры"""
        if len(card_number) < 10:
            return card_number
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"

    def mask_account_number(account_number: str) -> str:
        """Маскирует номер счета, оставляя последние 4 цифры"""
        if len(account_number) < 4:
            return account_number
        return f"**{account_number[-4:]}"

    # Разделяем строку на части (тип и номер)
    parts = account_info.split()

    # Проверяем, является ли последняя часть номером (содержит только цифры)
    if parts[-1].isdigit():
        number = parts[-1]
        account_type = " ".join(parts[:-1])

        if account_type.lower() == "счет":
            masked_number = mask_account_number(number)
        else:
            masked_number = mask_card_number(number)

        return f"{account_type} {masked_number}"
    else:
        return "Некорректные данные"


mask_account_card(account_info)


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


get_date(date_string)
