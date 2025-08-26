from functools import wraps


def log(filename=None):
    """
    Декоратор для логирования выполнения функций.

    Args:
        filename (str, optional): Имя файла для записи логов.
                                 Если None - вывод в консоль.
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Формируем информацию о входных параметрах в правильном формате
            args_str = ", ".join(repr(arg) for arg in args)
            kwargs_str = ", ".join(f"{k}={repr(v)}" for k, v in kwargs.items())

            # Формируем строку входных параметров
            if not args and not kwargs:
                inputs_str = "()"
            elif not kwargs:
                inputs_str = f"({args_str})"
            elif not args:
                inputs_str = f"{{{kwargs_str}}}"
            else:
                inputs_str = f"({args_str}), {{{kwargs_str}}}"

            try:
                # Выполняем функцию
                result = func(*args, **kwargs)

                # Формируем сообщение об успехе
                success_message = f"{func.__name__} ok\n"

                # Логируем успех
                if filename:
                    with open(filename, 'a', encoding='utf-8') as f:
                        f.write(success_message)
                else:
                    print(success_message, end='')

                return result

            except Exception as e:
                # Формируем сообщение об ошибке
                error_message = f"{func.__name__} error: {type(e).__name__}: {str(e)}. Inputs: {inputs_str}\n"

                # Логируем ошибку
                if filename:
                    with open(filename, 'a', encoding='utf-8') as f:
                        f.write(error_message)
                else:
                    print(error_message, end='')

                # Пробрасываем исключение дальше
                raise

        return wrapper

    return decorator

# # Пример 1: Логирование в файл
# @log(filename="mylog.txt")
# def my_function(x, y):
#     return x + y
#
# my_function(1, 2)  # Запишет "my_function ok" в mylog.txt
#
# # Пример 2: Логирование в консоль
# @log()
# def dangerous_division(a, b):
#     return a / b
#
# try:
#     dangerous_division(10, 0)
# except ZeroDivisionError:
#     pass  # В консоль выведется информация об ошибке
#
# # Пример 3: Функция с ключевыми аргументами
# @log(filename="operations.log")
# def complex_operation(x, y, multiplier=1):
#     return (x + y) * multiplier
#
# complex_operation(2, 3, multiplier=5)  # Запишет успех в operations.log
