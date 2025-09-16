import pytest
import os
import tempfile
from src.decorators import log


def test_log_to_file_success():
    """Тест логирования успешного выполнения в файл"""
    with tempfile.NamedTemporaryFile(mode='w', delete=False, encoding='utf-8') as tmp:
        filename = tmp.name

    try:
        @log(filename=filename)
        def add(a, b):
            return a + b

        result = add(1, 2)

        # Проверяем результат функции
        assert result == 3

        # Проверяем запись в файл
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            assert "add ok" in content

    finally:
        os.unlink(filename)


def test_log_to_file_error():
    """Тест логирования ошибки в файл"""
    with tempfile.NamedTemporaryFile(mode='w', delete=False, encoding='utf-8') as tmp:
        filename = tmp.name

    try:
        @log(filename=filename)
        def divide(a, b):
            return a / b

        # Проверяем, что исключение пробрасывается
        with pytest.raises(ZeroDivisionError):
            divide(1, 0)

        # Проверяем запись в файл
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            assert "divide error" in content
            assert "ZeroDivisionError" in content
            assert "Inputs: (1, 0)" in content

    finally:
        os.unlink(filename)


def test_log_to_console_success(capsys):
    """Тест логирования успешного выполнения в консоль"""

    @log()
    def multiply(a, b):
        return a * b

    result = multiply(3, 4)

    # Проверяем результат функции
    assert result == 12

    # Проверяем вывод в консоль
    captured = capsys.readouterr()
    assert "multiply ok" in captured.out


def test_log_to_console_error(capsys):
    """Тест логирования ошибки в консоль"""

    @log()
    def failing_function(x, y, z=10):
        raise ValueError("Custom error message")

    # Проверяем, что исключение пробрасывается
    with pytest.raises(ValueError):
        failing_function(1, 2, z=3)

    # Проверяем вывод в консоль
    captured = capsys.readouterr()
    assert "failing_function error" in captured.out
    assert "ValueError" in captured.out
    assert "Inputs: (1, 2), {z=3}" in captured.out  # Исправлено на правильный формат


def test_log_with_kwargs(capsys):
    """Тест логирования функции с ключевыми аргументами"""

    @log()
    def complex_function(a, b, c=0, d=1):
        return a + b + c + d

    result = complex_function(1, 2, c=3, d=4)

    # Проверяем результат
    assert result == 10

    # Проверяем вывод в консоль
    captured = capsys.readouterr()
    assert "complex_function ok" in captured.out


def test_log_with_no_args(capsys):
    """Тест логирования функции без аргументов"""

    @log()
    def no_args_function():
        return "success"

    result = no_args_function()

    # Проверяем результат
    assert result == "success"

    # Проверяем вывод в консоль
    captured = capsys.readouterr()
    assert "no_args_function ok" in captured.out


def test_log_multiple_calls(capsys):
    """Тест многократного вызова функции с логированием"""

    @log()
    def counter():
        return 1

    results = [counter() for _ in range(3)]

    # Проверяем результаты
    assert results == [1, 1, 1]

    # Проверяем вывод в консоль (3 записи)
    captured = capsys.readouterr()
    lines = captured.out.strip().split('\n')
    assert len(lines) == 3
    assert all("counter ok" in line for line in lines)


def test_log_preserves_function_metadata():
    """Тест, что декоратор сохраняет метаданные функции"""

    @log()
    def documented_function(x):
        """Тестовая функция с документацией"""
        return x * 2

    assert documented_function.__name__ == "documented_function"
    assert documented_function.__doc__ == "Тестовая функция с документацией"