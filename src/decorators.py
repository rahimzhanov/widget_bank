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