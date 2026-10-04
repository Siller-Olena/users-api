# Users API

REST API для керування користувачами в системі (CRUD: створення, отримання, оновлення, видалення).

## Мова та фреймворк
- Python 3.11
- FastAPI (документація OpenAPI та Swagger UI доступні за адресою `/docs`)
- Pytest для unit-тестів

## Збірка та запуск Docker image
```bash
cd users-api
docker build -t users-api:latest .
docker run -p 8000:8000 users-api:latest
```
Після запуску Swagger UI доступний за адресою http://localhost:8000/docs

## Запуск тестів
```bash
cd users-api
pip install -r requirements.txt
pytest -v
## Посилання
- GitHub: https://github.com/Siller-Olena/users-api
- Docker Hub: https://hub.docker.com/r/sillerolena/sillerolena1

```