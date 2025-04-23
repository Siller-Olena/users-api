from fastapi import FastAPI
from src.middlewares.error_handler import ErrorHandlerMiddleware  # Правильний імпорт класу
from src.api.users import router
from src.middlewares import error_handler

app = FastAPI()

# Додаємо middleware для обробки помилок
app.add_middleware(ErrorHandlerMiddleware)

# Налаштовуємо обробники виключень
error_handler.setup_exception_handlers(app)

# Додаємо маршрути
app.include_router(router, prefix="/users", tags=["Users"])
