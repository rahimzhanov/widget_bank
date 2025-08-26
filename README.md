# Учебный проект 'Виджет банковских операций'

### Описание
Проект предоставляет инструменты для фильтрации и анализа банковских операций с возможностью гибкой настройки параметров.

### Цель проекта
создать приложение-виджет, которое, позволит проводить банковские операции
и поможет научится разрабатывать на Python

## ⚙️ Установка

### Требования
- Python 3.9+
- Poetry 1.2+

### Инструкция
```
 1. Клонируйте репозиторий
git clone git@github.com:rahimzhanov/widget_bank.git
cd widget_bank

 2. Установите зависимости
poetry install

 3. Активируйте виртуальное окружение
poetry shell

 4. (Опционально) Настройте pre-commit хуки
pre-commit install

````
## Разработка
### Рабочий процесс

Форматирование кода: black

Проверка стиля: flake8 

Проверка типов: mypy

Запуск тестов: pytest

### Ветвление (Git Flow)
main - стабильная версия

develop - разработка

feature/* - новые функции

hotfix/* - срочные исправления
### В проекте используются функции
```
get_mask_card_number
get_mask_account
mask_account_card
get_date
filter_by_state
sort_by_date
filter_by_currency
transaction_descriptions
card_number_generator
log
```
### Пример вызовов функций
```
print(mask_account_card('Счет 73654108430135874305'))
print(get_date('2024-03-11T02:26:18.671407'))
print(filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))
print(sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))

for card_number in card_number_generator(1, 3):
             print(card_number)
             
print(next(descriptions))  # "Перевод организации"

usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(2):
     print(next(usd_transactions))
     
@log(filename="mylog.txt") 
def my_function(x, y):
    return x + y
 
my_function(1, 2)  # Запишет "my_function ok" в mylog.txt

```
## В проекте используются Тесты основанные на pytest
### Тесты можно запустить командой ```pytest``` в терминале
