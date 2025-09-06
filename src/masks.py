import logging


logger = logging.getLogger("masks")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('../logs/masks.log', encoding="utf-8")
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер банковской карты, оставляя первые 6 и
    последние 4 цифры видимыми.
    Остальные цифры заменяются звездочками, с разбивкой на блоки по 4 цифры.

    :param card_number: Номер карты для маскирования (строка из цифр)
    :return: Замаскированный номер карты в формате XXXX XX** **** XXXX
    """
    if len(card_number) == 16 and card_number.isdigit():
        logger.info(f"Карта успешно замаскирована - {card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}")
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    else:
        logger.warning("Номер карты должен состоять из 16 цифр")
        return "Номер карты должен состоять из 16 цифр"


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер банковского счета, оставляя только последние
    4 цифры видимыми.
    Первые цифры заменяются двумя звездочками.

    :param account_number: Номер счета для маскирования (строка из цифр)
    :return: Замаскированный номер счета в формате **XXXX
    """
    if len(account_number) == 20 and account_number.isdigit():
        logger.info(f'Банковский счет успешно замаскирован - **{account_number[-4:]}')
        return f"**{account_number[-4:]}"
    else:
        logger.warning("Номер счета должен содержать 20 цифр")
        return "Номер счета должен содержать 20 цифр"


# if __name__ == '__main__':
#   print(get_mask_card_number('1234567890123456'))
#   print(get_mask_account('12345678901234567890'))
