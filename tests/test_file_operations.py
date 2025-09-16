from unittest.mock import patch
import pandas as pd
from src.file_operations import read_csv_to_list, read_excel_to_list


def test_read_csv_to_list_success():
    """Тест успешного чтения CSV файла с преобразованием в JSON-формат"""
    with patch('pandas.read_csv') as mock_read_csv:
        # Мокируем ПРАВИЛЬНЫЕ данные со всеми нужными колонками
        mock_data = pd.DataFrame({
            'id': [1, 2],
            'state': ['EXECUTED', 'PENDING'],
            'date': ['2023-01-01', '2023-01-02'],
            'description': ['Payment', 'Transfer'],
            'from': ['1234567890123456', '9876543210987654'],
            'to': ['1111222233334444', '5555666677778888'],
            'amount': [100.0, 200.5],
            'currency_name': ['US Dollar', 'Russian Ruble'],
            'currency_code': ['USD', 'RUB']
        })
        mock_read_csv.return_value = mock_data

        # Вызываем функцию
        result = read_csv_to_list('test.csv')

        # Проверяем результаты
        assert len(result) == 2

        # Проверяем структуру первого элемента
        assert result[0]['id'] == 1
        assert result[0]['state'] == 'EXECUTED'
        assert result[0]['operationAmount']['amount'] == '100.0'  # Преобразовано в строку
        assert result[0]['operationAmount']['currency']['code'] == 'USD'  # Правильный вложенный доступ

        # Проверяем структуру второго элемента
        assert result[1]['id'] == 2
        assert result[1]['operationAmount']['amount'] == '200.5'
        assert result[1]['operationAmount']['currency']['name'] == 'Russian Ruble'

        mock_read_csv.assert_called_once_with('test.csv', sep=';')


def test_read_csv_to_list_file_not_found():
    """Тест обработки отсутствующего CSV файла"""
    with patch('pandas.read_csv') as mock_read_csv:
        mock_read_csv.side_effect = FileNotFoundError("File not found")

        result = read_csv_to_list('nonexistent.csv')

        assert result == []
        mock_read_csv.assert_called_once_with('nonexistent.csv', sep=';')


def test_read_excel_to_list_success():
    """Тест успешного чтения Excel файла с преобразованием в JSON-формат"""
    with patch('pandas.read_excel') as mock_read_excel:
        # Мокируем ПРАВИЛЬНЫЕ данные со всеми нужными колонками
        mock_data = pd.DataFrame({
            'id': [1, 2],
            'state': ['EXECUTED', 'PENDING'],
            'date': ['2023-01-01', '2023-01-02'],
            'description': ['Payment', 'Transfer'],
            'from': ['1234567890123456', '9876543210987654'],
            'to': ['1111222233334444', '5555666677778888'],
            'amount': [100.0, 200.5],
            'currency_name': ['US Dollar', 'Russian Ruble'],
            'currency_code': ['USD', 'RUB']
        })
        mock_read_excel.return_value = mock_data

        # Вызываем функцию
        result = read_excel_to_list('test.xlsx')

        # Проверяем результаты
        assert len(result) == 2

        # Проверяем структуру первого элемента
        assert result[0]['id'] == 1
        assert result[0]['state'] == 'EXECUTED'
        assert result[0]['operationAmount']['amount'] == '100.0'  # Преобразовано в строку
        assert result[0]['operationAmount']['currency']['code'] == 'USD'  # Правильный вложенный доступ

        # Проверяем структуру второго элемента
        assert result[1]['id'] == 2
        assert result[1]['operationAmount']['amount'] == '200.5'
        assert result[1]['operationAmount']['currency']['name'] == 'Russian Ruble'

        mock_read_excel.assert_called_once_with('test.xlsx')


def test_read_excel_to_list_file_not_found():
    """Тест обработки отсутствующего Excel файла"""
    with patch('pandas.read_excel') as mock_read_excel:
        mock_read_excel.side_effect = FileNotFoundError("File not found")

        result = read_excel_to_list('nonexistent.xlsx')

        assert result == []
        mock_read_excel.assert_called_once_with('nonexistent.xlsx')