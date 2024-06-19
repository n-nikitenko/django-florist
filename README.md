# django-florist

Онлайн-каталог для цветочного магазина

## Функции программы

1. Вывод списка товаров при переходе на страницу 'Prices'

2. Сбор обратной связи через форму на странице 'Contacts'
3. Создание нового товара
4. Редактирование товара
5. Просмотр страницы товара
6. Удаление товара
7. Создание, просмотр, редактирование, удаление статей в блоге.

## Установка и использование

Для работы программы необходимо:

1. установить зависимости, указанные в файле  pyproject.toml:
- для первичной установки:

  ```poetry install```
- для обновления:

  ```poetry update```


2. создать файл `.env` с параметрами доступа к базе данных PostgresSQL и запуска сервера django.
Пример содержимого файла:

```
POSTGRES_HOST=localhost
POSTGRES_USER=postgres
POSTGRES_PASSWORD=your_password
POSTGRES_PORT=5432
POSTGRES_DB=postgres

DJANGO_DEBUG=True
DJANGO_SECRET_KEY=your_secret_key
```
3. выполнить миграции командой
```commandline
python3 ./manage.py migrate
```

4. наполнить БД данными из фикстур:

```
python ./manage.py fill
```

5. запустить сервер:
```commandline
python3 ./manage.py runserver
```

## Создание суперпользователя:
```commandline
python3 ./manage.py createsuperuser
```
