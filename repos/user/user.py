import email

from sqlalchemy import Select
from sqlmodel import Session

from schemas.models.user import User


def create_user(db: Session, user: User):
    db.add(user)


def get_user_by_email(db: Session, username: str) -> User|None:
    statement = Select(User).where(User.username == username)
    result = db.exec(statement).scalar_one()
    return result
