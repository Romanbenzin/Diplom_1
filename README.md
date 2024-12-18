## Дипломный проект. Задание 1: Юнит-тесты

### Автотесты для проверки программы, которая помогает заказать бургер в Stellar Burgers

### Реализованные сценарии

Созданы юнит-тесты, покрывающие классы `Bun`, `Burger`, `Ingredient`, `Database`

Процент покрытия 100% (отчет: `htmlcov/index.html`)

### Структура проекта

- `praktikum` - пакет, содержащий код программы
- `tests` - пакет, содержащий тесты, разделенные по классам. Например, `bun_test.py`, `burger_test.py` и т.д.

### Запуск автотестов

**Установка зависимостей**

> `$ pip install -r requirements.txt`

**Запуск автотестов и создание HTML-отчета о покрытии**

>  `$ pytest --cov=praktikum --cov-report=html`

**Запуск на windows**
>  `$env:PYTHONPATH="."; pytest tests/ --alluredir=allure-results -v`
>  `$env:PYTHONPATH="."; pytest tests/ --cov=praktikum --cov-report=html`
>  `$env:PYTHONPATH="."; pytest tests/ -v`


**Открыть отчет в брузере**
>  `coverage html`
>  `start htmlcov\index.html`
