card_number = 0
account_number = 0


def get_mask_card_number(card_number: int) -> str:
    """
    Маскирует номер карты, оставляя первые 6 и последние 4 цифры, остальные заменяет на '*'
    """
    digits = str(card_number).replace(" ", "")

    if not digits.isdigit():
        raise ValueError("Номер карты должен содержать только цифры")

    if len(digits) < 16 or len(digits) > 19:
        raise ValueError("Номер карты должен содержать от 16 до 19 цифр")

    if len(digits) == 16:
        return f"{digits[:4]} {digits[4:6]}** **** {digits[-4:]}"
    else:  # 17-19 цифр
        return f"{digits[:4]} {digits[4:6]}** ***** {digits[-4:]}"


def get_mask_account(account_number: int) -> str:
    """
    Маскирует номер счёта, оставляя только последние 4 цифры.
    """
    str_number = str(account_number)

    if not str_number.isdigit():
        raise ValueError("Номер счёта должен содержать только цифры")

    if len(str_number) < 4:
        raise ValueError("Номер счёта должен содержать минимум 4 цифры")

    return f"**{str_number[-4:]}"
