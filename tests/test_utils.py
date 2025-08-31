from unittest.mock import mock_open, patch
from src.utils import open_json, convert_amount

def test_open_json():
    with patch("builtins.open", mock_open(read_data='{"1":"2"}')):
        assert open_json("") == {"1": "2"}


def test_summ_operation():
    with patch("requests.get") as n_mock:
        n_mock.return_value.json.return_value = {'result': 111}
        assert (convert_amount({
            'operationAmount': {'amount': '79114.93', 'currency': {'code': "USD"}}}) == 'Сумма транзакции - Количество запросов превысило 100, API не работает! руб.')
        assert (convert_amount({
            'operationAmount': {'amount': '1000', 'currency': {'code': "RUB"}}}) == 'Сумма транзакции - 1000 руб.')