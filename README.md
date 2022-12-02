# Tech_test
- простой API на базе fast_api, sqlalchemy and alembic
- для запуска перейдите в корневую директорию и введите в консоли "docker compose up --build"
- openAPI интерфейс будет доступен по адресу http://localhost:8000/docs
- pgadmin доступен на http://127.0.0.1:5050/ (pgadmin4@pgadmin.org : admin)
- база данных для тестирования генерируется автоматически ПРИ КАЖДОМ ЗАПУСКЕ приложения (отлючить это поведение можно закоментировав отмеченную строку в src/app/main.py)
