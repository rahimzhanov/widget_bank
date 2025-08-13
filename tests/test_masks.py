import pytest
from src.masks import get_mask_card_number
from src.masks import get_mask_account

# @pytest.mark.parametrize("card_number, expected", [
#     ('1234567890123456', '1234 56** **** 3456'),
#     ('123456789012345', 'Номер карты должен состоять из 16 цифр'),
#     ('123456789012345c', 'Номер карты должен состоять из 16 цифр'),
#     ('1234567890123456667734', 'Номер карты должен состоять из 16 цифр'),
# ])

def test_get_mask_card_number(card_number_test_cases):
    for card_number, expected in card_number_test_cases:
        assert get_mask_card_number(card_number) == expected


# @pytest.mark.parametrize("account_number, expected", [
#     ('12345678901234567890', '**7890'),
#     ('123456789012345678', 'Номер счета должен содержать 20 цифр'),
#     ('1234567890123456789012345', 'Номер счета должен содержать 20 цифр'),
#     ('123456789012345667RF', 'Номер счета должен содержать 20 цифр'),
# ])

def test_get_mask_account(account_number_test_cases):
    for account_number, expected in account_number_test_cases:
        assert get_mask_account(account_number) == expected