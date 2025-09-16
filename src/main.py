# Для загрузки данных
from src.utils import open_json
from src.file_operations import read_csv_to_list, read_excel_to_list

# Для обработки данных
from src.processing import filter_by_state, sort_by_date, filter_by_description

# Для вывода результатов
from src.widget import mask_account_card, get_date
from src.external_api import convert_rub_currency

# Для фильтрации по валюте (если будем делать отдельную функцию)
from src.utils import convert_amount

def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    # Здесь будет продолжение реализации...

    while True:
        user_choice = input("\nПользователь: ").strip()  # .strip() убирает лишние пробелы

        if user_choice == '1':
            print('\nПрограмма: Для обработки выбран JSON-файл.')
            file_type = 'json'
            break
        elif user_choice == '2':
            print('\nПрограмма: Для обработки выбран CSV-файл.')
            file_type = 'csv'
            break
        elif user_choice == '3':
            print('\nПрограмма: Для обработки выбран XLSX-файл.')
            file_type = 'excel'
            break
        else:
            print('\nНеверный выбор. Пожалуйста, введите 1, 2 или 3')


    # Теперь запрашиваем статус операций
    def show_status_instructions():
        print('\nПрограмма: Введите статус, по которому необходимо выполнить фильтрацию.')
        print('Доступные для фильтрации статусы: EXECUTED, CANCELED, PENDING')

    show_status_instructions()

    valid_statuses = ['executed', 'canceled', 'pending']

    while True:
        user_status = input("\nПользователь: ").strip().lower()

        if user_status in valid_statuses:
            print(f'\nПрограмма: Операции отфильтрованы по статусу "{user_status.upper()}"')
            selected_status = user_status
            break
        else:
            print(f'\nПрограмма: Статус операции "{user_status}" недоступен.')
            show_status_instructions()

    while True:
        sort_choice = input("\nПрограмма: Отсортировать операции по дате? Да/Нет\n").strip().lower()

        if sort_choice == 'да':
            need_sorting = True
            break
        elif sort_choice == 'нет':
            need_sorting = False
            break
        else:
            print('Пожалуйста, введите "Да" или "Нет"')

    # Выбор направления сортировки
    sort_reverse = False  # значение по умолчанию (по возрастанию)

    if need_sorting:
        print("\nПрограмма: Отсортировать по возрастанию или по убыванию?")

        while True:
            direction = input("Пользователь: ").strip().lower()

            if direction in ['по убыванию', 'убыванию', 'убывание']:
                sort_reverse = True  # сортировка от новых к старым
                break
            elif direction in ['по возрастанию', 'возрастанию', 'возрастание']:
                sort_reverse = False  # сортировка от старых к новым
                break
            else:
                print('Пожалуйста, введите "по возрастанию" или "по убыванию"')

    # Фильтрация по валюте
    print("\nПрограмма: Выводить только рублевые транзакции? Да/Нет")

    while True:
        currency_choice = input("Пользователь: ").strip().lower()

        if currency_choice == 'да':
            only_rub = True
            break
        elif currency_choice == 'нет':
            only_rub = False
            break
        else:
            print('Пожалуйста, введите "Да" или "Нет"')

    print('\nПрограмма: Отфильтровать список транзакций по определенному слову в описании? Да/Нет')

    while True:
        filtered_choice = input('\nПользователь: ').strip().lower()

        if filtered_choice == "да":
            use_filter = True
            break
        elif filtered_choice == "нет":
            use_filter = False
            break
        else:
            print('Пожалуйста, введите "Да" или "Нет"')

    if use_filter:
        print('\nПрограмма: Введите слово для поиска в описании:')
        search_word = input('Пользователь: ').strip()
        # Дальше используем search_word для фильтрации
    else:
        search_word = None  # или пустая строка


    # 1. ЗАГРУЗКА ДАННЫХ ИЗ ФАЙЛА
    def load_data(file_type):
        """Загружает данные из файла в зависимости от типа"""
        try:
            if file_type == 'json':
                # Используем функцию из utils.py
                data = open_json('../data/operations.json')
            elif file_type == 'csv':
                # Используем функцию из file_operations.py
                data = read_csv_to_list('../data/transactions.csv')
            elif file_type == 'excel':
                # Используем функцию из file_operations.py
                data = read_excel_to_list('../data/transactions_excel.xlsx')
            else:
                print("Ошибка: неизвестный тип файла")
                return []

            print(f"Загружено {len(data)} транзакций")
            return data

        except Exception as e:
            print(f"Ошибка при загрузке данных: {e}")
            return []

    # Загружаем данные
    data = load_data(file_type)
    if not data:
        print("Не удалось загрузить данные. Программа завершена.")
        return

    # 2. ФИЛЬТРАЦИЯ ПО СТАТУСУ
    filtered_data = filter_by_state(data, selected_status.upper())
    print(f'Программа: Операции отфильтрованы по статусу "{selected_status.upper()}"')

    # 3. СОРТИРОВКА ПО ДАТЕ (ЕСЛИ НУЖНО)
    if need_sorting:
        filtered_data = sort_by_date(filtered_data, reverse=sort_reverse)
        # Просто сортируем, без лишних сообщений

    # 4. ФИЛЬТРАЦИЯ ПО ВАЛЮТЕ (ЕСЛИ НУЖНО)
    if only_rub:
        ruble_data = []
        for transaction in filtered_data:
            # Для унифицированного формата (после преобразования)
            if 'operationAmount' in transaction and isinstance(transaction['operationAmount'], dict):
                currency = transaction['operationAmount']['currency']['code']
                if currency == 'RUB':
                    ruble_data.append(transaction)
        filtered_data = ruble_data

    # 5. ФИЛЬТРАЦИЯ ПО ОПИСАНИЮ (ЕСЛИ НУЖНО)
    if use_filter and search_word:
        filtered_data = filter_by_description(filtered_data, search_word)

    # 6. ФИНАЛЬНЫЙ ВЫВОД
    print('Программа: Распечатываю итоговый список транзакций...')
    print()
    print(f'Всего банковских операций в выборке: {len(filtered_data)}')
    print()

    for transaction in filtered_data:
        # Форматируем дату
        date_str = get_date(transaction['date'])

        # Форматируем откуда/куда
        from_str = mask_account_card(transaction.get('from', '')) if transaction.get('from') else ''
        to_str = mask_account_card(transaction.get('to', ''))

        # Форматируем сумму
        amount_str = convert_amount(transaction)

        # Выводим красиво
        print(f'{date_str} {transaction["description"]}')
        if from_str:
            print(f'{from_str} -> {to_str}')
        else:
            print(f'{to_str}')
        print(amount_str)
        print()


    return file_type, selected_status, need_sorting, sort_reverse, only_rub, search_word


main()