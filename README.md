# django-florist

Цель проекта заключается в 

## Функции программы

1. Заполнение БД данными из фикстур:

```./manage.py fill```

## Установка и использование

Для работы программы необходимо установить зависимости, указанные в файле  pyproject.toml:
- для первичной установки:

  ```poetry install```
- для обновления:

  ```poetry update```


Для работы программы необходимо создать файл `.env` с параметрами доступа к базе данных PostgresSQL и запуска сервера django.
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
