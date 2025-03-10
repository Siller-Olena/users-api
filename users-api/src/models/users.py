# Переконайтеся, що цей файл не імпортує нічого, що знову викликає цей файл

from uuid import UUID
from pydantic import BaseModel
from typing import List, Optional

# Опис класу User
class User(BaseModel):
    id: UUID
    name: str
    email: str
    age: int

# Singleton UserService
class UserService:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(UserService, cls).__new__(cls)
            cls._instance.users = []  # Тут  користувачі, для тесту використовується список
        return cls._instance

    def get_users(self) -> List[User]:
        return self.users  # Повертає список користувачів

    def get_user(self, user_id: UUID) -> Optional[User]:
        return next((user for user in self.users if user.id == user_id), None)

    def create_user(self, user: User) -> User:
        self.users.append(user)
        return user

    def update_user(self, user_id: UUID, updated_user: User) -> Optional[User]:
        for idx, user in enumerate(self.users):
            if user.id == user_id:
                self.users[idx] = updated_user
                return updated_user
        return None

    def delete_user(self, user_id: UUID) -> bool:
        for idx, user in enumerate(self.users):
            if user.id == user_id:
                del self.users[idx]
                return True
        return False

