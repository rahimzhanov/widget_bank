from masks import get_mask_card_number
from datetime import datetime


def mask_account_card(account_card: str) -> str:
    code = ""
    account = ""

    for char in account_card:
        if char.isdigit():
            code += char
        else:
            account += char

    masked = account + get_mask_card_number(code)
    return masked


def get_date(date_str: str) -> str:
    """
    Преобразует дату из формата 'ГГГГ-ММ-ДДTЧЧ:ММ:СС.микросекунды' в 'ДД.ММ.ГГГГ'

    Args:
        date_str: Строка с датой в ISO формате

    Returns:
        Строка с датой в формате 'ДД.ММ.ГГГГ'
    """
    dt = datetime.fromisoformat(date_str)
    return dt.strftime("%d.%m.%Y")

#print(mask_account_card('Visa Platinum 7000792289606361'))
#print(get_date('2024-03-11T02:26:18.671407'))