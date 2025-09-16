from unittest.mock import mock_open, patch
from src.utils import open_json, convert_amount


def test_open_json():
    with patch("builtins.open", mock_open(read_data='{"1":"2"}')):
        assert open_json("") == {"1": "2"}


def test_summ_operation():
    """Тест конвертации суммы операции из USD в RUB"""
    with patch("src.utils.convert_rub_currency") as mock_convert:
        # Мокируем конвертацию: 1 USD = 83.854343 RUB
        mock_convert.return_value = 83.854343

        result = convert_amount({
            'operationAmount': {
                'amount': '1',
                'currency': {'code': "USD"}
            }
        })

        # Проверяем, что функция конвертации вызвана с правильными параметрами
        mock_convert.assert_called_once_with("USD", "1")

        # Проверяем результат конвертации
        assert result == 'Сумма транзакции - 83.854343 руб.'


def test_convert_amount_csv_data():
    """Тест конвертации для JSON данных (после преобразования из CSV)"""
    with patch('src.utils.convert_rub_currency') as mock_convert:
        mock_convert.return_value = 7500.0

        # Передаем данные в JSON-формате (как после преобразования из CSV)
        item = {
            'operationAmount': {
                'amount': '100.0',
                'currency': {
                    'code': 'USD'
                }
            }
        }
        result = convert_amount(item)

        # Проверяем вызов конвертации
        mock_convert.assert_called_once_with("USD", "100.0")

        # Проверяем результат
        assert result == 'Сумма транзакции - 7500.0 руб.'


def test_convert_amount_rub():
    """Тест для RUB валюты (без конвертации)"""
    # Не нужно мокировать convert_rub_currency, так как для RUB она не вызывается

    item = {
        'operationAmount': {
            'amount': '5000.0',
            'currency': {
                'code': 'RUB'
            }
        }
    }
    result = convert_amount(item)

    # Для RUB просто возвращаем сумму
    assert result == 'Сумма транзакции - 5000.0 руб.'


def test_convert_amount_invalid_format():
    """Тест обработки неверного формата данных"""
    item = {'some_field': 'value'}
    result = convert_amount(item)
    assert result == "Ошибка: неверный формат данных транзакции"


def test_open_json_file_not_found():
    """Тест обработки отсутствующего JSON файла"""
    with patch("builtins.open") as mock_open:
        mock_open.side_effect = FileNotFoundError()

        result = open_json('nonexistent.json')
        assert result == []