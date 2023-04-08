import json
from typing import Dict
from fastapi import APIRouter, Depends, Header, HTTPException, Response, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from auth.app.models import user as models
from auth.app.schemas.user import User, UserInDB, UserLogin
from auth.app.utils.generate_token import (create_access_token,
                                           create_refresh_token)
from auth.app.utils.hash_password import get_password_hash
from auth.app.database.posgresql import get_session

router = APIRouter()


@router.post('/register', response_model=User)
async def register(payload: User, session: AsyncSession = Depends(get_session)) -> Dict:
    verified_pass = get_password_hash(payload.password)
    payload.password = verified_pass
    new_user = models.User(**payload.dict())
    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)
    return {"new user": verified_pass}


@router.post('/login')
async def login(payload: UserLogin, response: Response, session: AsyncSession = Depends(get_session)):
    statement = select(models.User).where(models.User.username == payload.username)
    exist_user = await session.execute(statement)
    if not exist_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='Incorrect Username or Password')
    access_token = create_access_token({'user': exist_user.mappings().all()})
    refresh_token = create_refresh_token({'user': exist_user.mappings().all()})
    return {'access token': access_token, 'refresh token': refresh_token}


    

