import json
import os
from datetime import datetime, timedelta
from typing import Any, Union
import jwt
from fastapi import HTTPException, status
from fastapi.encoders import jsonable_encoder


def create_access_token(data: dict):
    user_list = data.get('user', None)
    if not user_list:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='wrong username or password')
    
    user_dict = user_list[0]
    user = user_dict.get('User', None)
    if user is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='error')

    dict_encode = jsonable_encoder(user)
    to_encode = json.dumps(dict_encode.get('username', None))
    encoded_jwt = jwt.encode({'username': to_encode}, os.getenv("SECRET_KEY", " "), algorithm="HS256")
    return encoded_jwt


def create_refresh_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=60)
    
    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, os.getenv("SECRET_KEY", " "), algorithm="HS256")
    return encoded_jwt