import pytest
import logging
import os
import sys

# Добавляем путь к src для корректного импорта
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

# Отключаем логирование для тестов
logging.disable(logging.CRITICAL)

# Временно отключаем FileHandler в модулях

# Импортируем модули и удаляем FileHandler
try:
    import src.masks
    import src.utils
    import src.widget

    # Удаляем FileHandler если они есть
    for logger_name in ['masks', 'utils', 'widget']:
        logger = logging.getLogger(logger_name)
        for handler in logger.handlers[:]:
            if isinstance(handler, logging.FileHandler):
                logger.removeHandler(handler)
except ImportError as e:
    print(f"Import error during handler removal: {e}")
    # Продолжаем выполнение, так как это может быть нормально для некоторых тестов


@pytest.fixture
def card_number_test_cases():
    return [
        ("1234567890123456", "1234 56** **** 3456"),
        ("123456789012345", "Номер карты должен состоять из 16 цифр"),
        ("123456789012345c", "Номер карты должен состоять из 16 цифр"),
        ("1234567890123456667734", "Номер карты должен состоять из 16 цифр"),
    ]


@pytest.fixture
def account_number_test_cases():
    return [
        ('12345678901234567890', '**7890'),
        ('123456789012345678', 'Номер счета должен содержать 20 цифр'),
        ('1234567890123456789012345', 'Номер счета должен содержать 20 цифр'),
        ('123456789012345667RF', 'Номер счета должен содержать 20 цифр'),
    ]


@pytest.fixture
def mask_account_test_cases():
    return [
        ('Visa 1234567890123456', 'Visa 1234 56** **** 3456'),
        ('kiska 1234567890123456', 'kiska 1234 56** **** 3456'),
        ('Vodka 12345678901234567890', 'Vodka **7890'),
        ('Счет 12345678901234567890', 'Счет **7890'),
        ('12345678901234567890', '**7890'),
    ]


@pytest.fixture
def get_date_test_cases():
    return [
        ('2024-03-11T02:26:18.671407', '11.03.2024'),
        # Корректные даты (ISO-формат)
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2024-03-11", "11.03.2024"),
        ("2024-03-11T02:26:18+03:00", "11.03.2024"),
        # Некорректные данные
        ("не дата", "Ошибка: Неверный формат даты (ожидается 'ГГГГ-ММ-ДД' или ISO-формат)"),
        ("", "Ошибка: Некорректный формат даты (ожидается строка)"),
        (None, "Ошибка: Некорректный формат даты (ожидается строка)"),
        (12345, "Ошибка: Некорректный формат даты (ожидается строка)"),
    ]