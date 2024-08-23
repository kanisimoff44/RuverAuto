from typing import Annotated

from fastapi import APIRouter, Form, Depends

from app.exceptions import CannotAddDataToDatabase, UserAlreadyExistsException, IncorrectEmailOrPasswordException
from app.users.auth import get_password_hash
from app.users.dao import UserDAO
from app.users.models import Roles, Users
from app.users.dependencies import get_current_user

router = APIRouter(
    prefix="/auth",
    tags=["Аутентификация"],
)


@router.post("/register", status_code=201)
async def register_user(email: Annotated[str, Form()], password: Annotated[str, Form()]):
    existing_user = await UserDAO.find_one_or_none(email=email)
    if existing_user:
        raise UserAlreadyExistsException
    hashed_password = get_password_hash(password)
    new_user = await UserDAO.add(email=email, hashed_password=hashed_password, is_active=True, is_superuser=True, role=Roles.ROOT)
    if not new_user:
        raise CannotAddDataToDatabase
