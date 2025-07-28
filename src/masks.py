def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер банковской карты, оставляя первые 6 и
    последние 4 цифры видимыми.
    Остальные цифры заменяются звездочками, с разбивкой на блоки по 4 цифры.

    :param card_number: Номер карты для маскирования (строка из цифр)
    :return: Замаскированный номер карты в формате XXXX XX** **** XXXX
    """
    if len(card_number) != 16 or not card_number.isdigit():
        raise ValueError("Номер карты должен состоять из 16 цифр")

    masked = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    return masked


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер банковского счета, оставляя только последние
    4 цифры видимыми.
    Первые цифры заменяются двумя звездочками.

    :param account_number: Номер счета для маскирования (строка из цифр)
    :return: Замаскированный номер счета в формате **XXXX
    """
    if len(account_number) < 20 or not account_number.isdigit():
        raise ValueError("Номер счета должен содержать минимум 20 цифр")

    masked = f"**{account_number[-20:]}"
    return masked
