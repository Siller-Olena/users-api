from fastapi import FastAPI  # правильний імпорт FastAPI
from fastapi import FastAPI
from src.middlewares.error_handler import ErrorHandlerMiddleware  # Правильний імпорт класу
from src.api import users
from src.api.users import router
from src.middlewares import error_handler

app = FastAPI()


# Додаємо middleware для обробки помилок
app.add_middleware(ErrorHandlerMiddleware)

# Налаштовуємо обробники виключень
error_handler.setup_exception_handlers(app)

# Додаємо маршрути
app.include_router(router)
app.include_router(users.router)
app.include_router(router, prefix="/users", tags=["Users"])
app.add_middleware(error_handler.ErrorHandlerMiddleware)
