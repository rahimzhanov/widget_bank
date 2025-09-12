from unittest.mock import mock_open, patch
from src.utils import open_json, convert_amount


def test_open_json():
    with patch("builtins.open", mock_open(read_data='{"1":"2"}')):
        assert open_json("") == {"1": "2"}


def test_summ_operation():
    with patch("requests.get") as n_mock:
        n_mock.return_value.json.return_value = {'result': 111}
        assert (convert_amount({
            'operationAmount': {'amount': '1', 'currency': {'code': "USD"}}}) == 'Сумма транзакции - 83.854343 руб.')
        assert (convert_amount({
            'operationAmount': {'amount': '1000', 'currency': {'code': "RUB"}}}) == 'Сумма транзакции - 1000.0 руб.')


def test_convert_amount_csv_data():
    """Тест конвертации для CSV данных"""
    with patch('src.utils.convert_rub_currency') as mock_convert:
        mock_convert.return_value = 7500.0

        item = {
            'amount': '100.0',
            'currency_code': 'USD'
        }
        result = convert_amount(item)

        assert result == 'Сумма транзакции - 7500.0 руб.'
        mock_convert.assert_called_once_with('USD', '100.0')


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