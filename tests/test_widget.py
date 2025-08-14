import pytest
from src.widget import mask_account_card
from src.widget import get_date

# @pytest.mark.parametrize('account_card, expected',[
#     ('Visa 1234567890123456', 'Visa 1234 56** **** 3456'),
#     ('kiska 1234567890123456', 'kiska 1234 56** **** 3456'),
#     ('Vodka 12345678901234567890', 'Vodka **7890'),
#     ('Счет 12345678901234567890', 'Счет **7890'),
#     ('12345678901234567890', '**7890'),
# ])


def test_mask_account_card(mask_account_test_cases):
    for account_card, expected in mask_account_test_cases:
        assert mask_account_card(account_card) == expected

def test_get_date(get_date_test_cases):
    for format_date, expected in get_date_test_cases:
        assert get_date(format_date) == expected