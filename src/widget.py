from datetime import datetime

account_info = input(str())
date_string = input(str())


def mask_account_card(account_info: str) -> str:
    """
    Маскирует номер карты или счета в переданной строке.
    """

    def mask_card_number(card_number: int) -> str:
        """
        Маскирует номер карты, оставляя первые 6 и последние 4 цифры, остальные заменяет на '*'
        """
        digits = str(card_number)  # Преобразуем число в строку

        if len(digits) == 16:
            return f"{digits[:4]} {digits[4:6]} **** {digits[-4:]}"
        elif 16 < len(digits) <= 19:
            return f"{digits[:4]} {digits[4:6]} ***** {digits[-4:]}"
        else:
            return "Номер карты должен содержать от 16 до 19 цифр"

    def mask_account(account_number: int) -> str:
        """
        Маскирует номер счёта, оставляя только последние 4 цифры.
        """
        str_number = str(account_number)

        if len(str_number) <= 4:
            return "Номер счёта должен содержать минимум 4 цифры"
        masked_part = "**" + str_number[-4:]
        return masked_part

    # Разделяем строку на части (тип и номер)
    parts = account_info.split()

    # Проверяем, является ли последняя часть номером (содержит только цифры)
    if parts[-1].isdigit():
        number = int(parts[-1])  # Преобразуем строку в число перед передачей
        account_type = " ".join(parts[:-1])
        if account_type.lower() == "счет":
            masked_number = mask_account(number)
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
