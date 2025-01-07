from fastapi import APIRouter, Depends
from sqlmodel import Session

from common import get_db
from common.response import success_data
from schemas.request.user import UserRequest
from services.user import user

user_router = APIRouter()

@user_router.post('/login')
async def login(req: UserRequest, db: Session = Depends(get_db)):
    resp = user.login(db, req)
    return success_data(resp)


@user_router.post('/user/register')
async def register(req: UserRequest, db: Session = Depends(get_db)):
    resp = user.register(db, req)
    return success_data(resp)