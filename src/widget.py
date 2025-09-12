from src.masks import get_mask_card_number
from src.masks import get_mask_account
from datetime import datetime


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


# def get_date(date_str: str) -> str:
#     """
#     Преобразует дату из формата 'ГГГГ-ММ-ДДTЧЧ:ММ:СС.микросекунды' в
#     'ДД.ММ.ГГГГ'
#
#     Args:
#         date_str: Строка с датой в ISO формате
#
#     Returns:
#         Строка с датой в формате 'ДД.ММ.ГГГГ'
#     """
#     dt = datetime.fromisoformat(date_str)
#     return dt.strftime("%d.%m.%Y")
#

def get_date(date_str: str) -> str:
    """
    Преобразует дату из формата 'ГГГГ-ММ-ДДTЧЧ:ММ:СС.микросекунды' в 'ДД.ММ.ГГГГ'.
    Если строка некорректна, возвращает сообщение об ошибке вместо падения.

    Args:
        date_str: Строка с датой в ISO-подобном формате.

    Returns:
        Строка с датой в формате 'ДД.ММ.ГГГГ' или сообщение об ошибке.
    """
    if not date_str or not isinstance(date_str, str):
        return "Ошибка: Некорректный формат даты (ожидается строка)"

    try:
        dt = datetime.fromisoformat(date_str)
        return dt.strftime("%d.%m.%Y")
    except ValueError:
        return "Ошибка: Неверный формат даты (ожидается 'ГГГГ-ММ-ДД' или ISO-формат)"
    except Exception as e:
        return f"Ошибка: Непредвиденная проблема при обработке даты ({str(e)})"


# print(get_date('2024-03-11T02:26:18.671407'))
# print(mask_account_card('Счет 73654108430135874305'))
