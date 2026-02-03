# Быстрый старт

## Создать и активировать виртуальное окружение
```
python -m venv venv

# Для Windows:
venv\Scripts\activate

# Для MacOS/Linux:
source venv/bin/activate
```

## Установить зависимости
```
pip install -r requirements.txt
```

## Создать и применить миграции
```
# Создать миграции
python manage.py makemigrations

# Применить миграции
python manage.py migrate
```

## Создать суперпользователя
```
python manage.py createsuperuser
```

## Запустить сервер
```
python manage.py runserver
```
