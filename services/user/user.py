import uuid

from fastapi import HTTPException
from sqlmodel import Session
from starlette import status

from common.exception import MyException
from repos.user import user
from schemas.models.user import User
from schemas.request.user import UserRequest, UserResponse


def login(db: Session, req: UserRequest) -> UserResponse:
    user_model = user.get_user_by_email(db, req.username)
    if not user_model:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    if user_model.password != req.password:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    return UserResponse(username=user_model.username)


def register(db: Session, req: UserRequest) -> User:
    u = User(id=uuid.uuid4(), username=req.username, password=req.password)
    user.create_user(db,u)
    try:
        db.commit()
    except Exception:
        db.rollback()
        raise MyException(code=550, detail="asdsa")

    return u