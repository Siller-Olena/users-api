
# Базовий образ з Python 3.11
FROM python:3.11

# Робоча директорія
WORKDIR /app

# Копіюємо файл залежностей і встановлюємо їх
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо весь код у контейнер
COPY . /app

# Змінна середовища для FastAPI/Python
ENV PYTHONUNBUFFERED=1

# Відкриваємо порт, на якому реально працює застосунок
EXPOSE 8000

# Запускаємо застосунок при старті контейнера
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
