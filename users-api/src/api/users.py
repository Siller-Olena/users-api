from typing import List
from uuid import UUID
from fastapi import APIRouter, HTTPException, Depends
from src.models.users import User, UserService, get_user_service


router = APIRouter()

# Маршрут для отримання всіх користувачів
@router.get("/users", response_model=List[User])
def get_users(service: UserService = Depends(get_user_service)):
    users = service.get_users()  # Отримуємо список користувачів
    if not users:
        raise HTTPException(status_code=404, detail="No users found")
    return service.get_users()
    return users

# Маршрут для отримання конкретного користувача за його ID
@router.get("/users/{user_id}", response_model=User)
def get_user(user_id: UUID, service: UserService = Depends(get_user_service)):
    user = service.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# Маршрут для створення нового користувача
@router.post("/users", response_model=User)
def create_user(user: User, service: UserService = Depends(get_user_service)):
    return service.create_user(user)

# Маршрут для оновлення користувача
@router.put("/users/{user_id}", response_model=User)
def update_user(user_id: UUID, updated_user: User, service: UserService = Depends(get_user_service)):
    existing_user = service.get_user(user_id)
    if not existing_user:
        raise HTTPException(status_code=404, detail="User not found")
    return service.update_user(user_id, updated_user)

# Маршрут для видалення користувача
@router.delete("/users/{user_id}", response_model=bool)
def delete_user(user_id: UUID, service: UserService = Depends(get_user_service)):
    if not service.delete_user(user_id):
        raise HTTPException(status_code=404, detail="User not found")
    return True
