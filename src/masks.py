card_number = input(int())
account_number = input(int())


def get_mask_card_number(card_number: int) -> str:
    """
    Маскирует номер карты, оставляя первые 6 и последние 4 цифры, остальные заменяет на '*'
    """

    digits = str(card_number).replace(" ", "")

    if len(digits) == 16:
        return f"{digits[:4]} {digits[4:6]}** **** {digits[-4:]}"
    elif 16 < len(digits) <= 19:
        return f"{digits[:4]} {digits[4:6]}** ***** {digits[-4:]}"
    else:
        return "Номер карты должен содержать от 16 до 19 цифр"


def get_mask_account(account_number: int) -> str:
    """
    Маскирует номер счёта, оставляя только последние 4 цифры.
    """

    str_number = str(account_number)

    if len(str_number) <= 4:  # Проверка длинны
        return "Номер счёта должен содержать минимум 4 цифры"

    masked_part = "**" + str_number[-4:]  # Маскируем номер счета

    return masked_part
