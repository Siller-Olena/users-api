# Используем официальный образ Python
FROM python:3.11-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем зависимости
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы проекта
COPY . .

# Прокси-порт (подбирай под свое приложение, например, FastAPI — 8000, Flask — 5000)
EXPOSE 8000

# Команда запуска (зависит от фреймворка)
# Для FastAPI (через uvicorn):
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

# Для Flask (раскомментируй и измени путь к app.py):
# CMD ["python", "app.py"]

