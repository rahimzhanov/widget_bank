from masks import get_mask_card_number
from masks import get_mask_account

def mask_account_card(account_card: str) -> str:
    code = ''
    account = ''

    for char in account_card:
        if char.isdigit():
            code += char
        else:
            account += char

    masked = account + get_mask_card_number(code)
    return masked

#print(mask_account_card('Visa Platinum 7000792289606361'))