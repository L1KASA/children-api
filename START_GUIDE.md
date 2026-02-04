# Инструкция по запуску проекта

Для полноценной работы проекта необходимо запустить два сервера: бэкенд (Django) и фронтенд (React).

### 1. Запуск бэкенда (Django)
Откройте первый терминал и выполните:
```bash
python manage.py runserver 8000
```
*Бэкенд будет доступен по адресу: `http://localhost:8000`*

### 2. Запуск фронтенда (React)
Откройте второй терминал и выполните:
```bash
cd frontend
npm start
```
*Фронтенд будет доступен по адресу: `http://localhost:3000`*

---

### Важные ссылки:
- **Интерфейс приложения**: [http://localhost:3000](http://localhost:3000)
- **Админка Django**: [http://localhost:8000/admin/](http://localhost:8000/admin/)
- **API (список клиентов)**: [http://localhost:8000/children/?status=client](http://localhost:8000/children/?status=client)
