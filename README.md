Django проект (без venv, к сожалению, его я импортировать не могу)<br>
/ - Главная<br>
/shop/ - Магазин<br>
/author/ - Автор<br>

Ответы на вопросы
1. Django — это Python-фреймворк для создания веб-сайтов.
2. `pip install django`
3. `python -m venv venv`
4. * Windows: `venv\Scripts\activate`
   * Linux/Mac: `source venv/bin/activate`
5. `django-admin startproject myproject`
6. `manage.py` — файл для управления проектом (запуск сервера, миграции и т.д.).
7. `settings.py`, `urls.py`, `asgi.py`, `wsgi.py`, `__init__.py`
8. В `settings.py`
9. Изменить `TIME_ZONE = 'Europe/Moscow'`
10. Параметр `DATABASES`
11. SQLite
12. Создать приложение и добавить в `INSTALLED_APPS`
13. `python manage.py startapp myapp`
14. Список подключённых приложений проекта
15. Добавить имя приложения в `INSTALLED_APPS`
16. Настройка путей (URL → функция/представление)
17. Через `include()` в основном `urls.py`
18. Открыть `http://127.0.0.1:8000/`
19. `python manage.py runserver`
20. Миграции — обновление БД; `makemigrations` и `migrate`
21. Перейти на `http://127.0.0.1:8000/`
22. Указать другой порт: `runserver 8001`
23. `urls.py`
24. `path()` — задаёт маршрут URL
25. Изменить `LANGUAGE_CODE`
26. Делает папку Python-модулем
27. `python -m django --version`
28. Разделение проекта на независимые приложения
29. `DEBUG = False` — для безопасности
30. Создать приложение, добавить в `INSTALLED_APPS`, настроить БД, выполнить миграции.
