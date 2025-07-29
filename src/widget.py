from masks import get_mask_card_number
from masks import get_mask_account
from datetime import datetime


def mask_account_card(account_card: str) -> str:
    """
       Принимает строку с именем и номером карты или счета,
       определяет номер это или счет за счет длины,
       маскирует номер или счет используя
       импортированные функции

       Args:
           account_card: строка с именем и номером или счетом

       Returns:
           Строка в таком же формате, только замаскированный номер или счет
       """

    code = ""
    account = ""

    for char in account_card:
        if char.isdigit():
            code += char
        else:
            account += char

    if len(code) > 16:
        masked = account + get_mask_account(code)
    else:
        masked = account + get_mask_card_number(code)

    return masked


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
