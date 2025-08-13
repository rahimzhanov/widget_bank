import pytest
from src.masks import get_mask_card_number
from src.masks import get_mask_account

@pytest.mark.parametrize("card_number, expected", [
    ('1234567890123456', '1234 56** **** 3456'),
    ('123456789012345', 'Номер карты должен состоять из 16 цифр'),
    ('12345678901234r5c', 'Номер карты должен состоять из 16 цифр'),
])

def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected