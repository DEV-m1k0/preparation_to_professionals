# Сессия 1 "Разработка базы данных и API"

В данной сесси был разработан следующий функционал:

1. Структура базы данных.
2. API.
3. Импорт экселя.

## Запуск проекта

переходим в рабочую директорию(core) и прописываем следующие команды для создания миграций:

```
python ./manage.py makemigrations
python ./manage.py migrate
```

После заполнения базы данных, запускаем наш сервер коммандой:

```
python ./manage.py runserver
```

Запуск скрипта:

```
python .\manage.py script_excel
```

Ссылки на api:

1. http://127.0.0.1:8000/api/v1/SignIn
2. http://127.0.0.1:8000/api/v1/Documents
3. http://127.0.0.1:8000/api/v1/Document/[documentId](int:documentId)/Comments
4. http://127.0.0.1:8000/api/v1/document
