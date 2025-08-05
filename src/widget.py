from masks import get_mask_card_number
from masks import get_mask_account
from datetime import datetime

from typing import Union
from masks import get_mask_account, get_mask_card_number  # type: ignore[import]


def mask_account_card(account_card: str) -> str:
    """
    Принимает строку с именем и номером карты или счета,
    определяет тип (карта/счет) по длине номера,
    возвращает строку с замаскированным номером.

    Args:
        account_card: строка в формате "Имя Номер" или "Счет Номер"

    Returns:
        Строка в формате "Имя МаскированныйНомер" или "Счет МаскированныйНомер"

    Examples:
        >>> mask_account_card("Visa Platinum 1234567890123456")
        'Visa Platinum 1234 56** **** 3456'

        >>> mask_account_card("Счет 12345678901234567890")
        'Счет **7890'
    """
    code = ""
    account = ""

    for char in account_card:
        if char.isdigit():
            code += char
        else:
            account += char

    masked_number: str
    if len(code) > 16:
        masked_number = get_mask_account(code)
    else:
        masked_number = get_mask_card_number(code)

    return account + masked_number


def get_date(date_str: str) -> str:
    """
    Преобразует дату из формата 'ГГГГ-ММ-ДДTЧЧ:ММ:СС.микросекунды' в
    'ДД.ММ.ГГГГ'

    Args:
        date_str: Строка с датой в ISO формате

    Returns:
        Строка с датой в формате 'ДД.ММ.ГГГГ'
    """
    dt = datetime.fromisoformat(date_str)
    return dt.strftime("%d.%m.%Y")


print(mask_account_card('Счет 73654108430135874305'))
print(get_date('2024-03-11T02:26:18.671407'))
