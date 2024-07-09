# import os
# from passlib.context import CryptContext
# from datetime import datetime, timedelta
# from typing import Union, Any
# from jwt import DecodeError
from fastapi import Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from decouple import config
ACCESS_TOKEN_EXPIRE_MINUTES = int(config("ACCESS_TOKEN_EXPIRE_MINUTES"))
REFRESH_TOKEN_EXPIRE_MINUTES = int(config("REFRESH_TOKEN_EXPIRE_MINUTES"))
ALGORITHM = config("ALGORITHM")
JWT_SECRET_KEY = config("JWT_SECRET_KEY")  
JWT_REFRESH_SECRET_KEY = config("JWT_REFRESH_SECRET_KEY")

    
security = HTTPBearer()

async def get_current_user(credentials: HTTPAuthorizationCredentials = Security(security)):
    print("jjjjjjjjjjj")
    token = credentials.credentials
    payload = decode_access_token(token)
    print("inside the get_curent user",payload)
    if payload is None:
        raise HTTPException(status_code=403, detail="Invalid token or expired token")
    else:
        return payload


import os
from passlib.context import CryptContext
from datetime import datetime, timedelta
from typing import Union, Any
import jwt  # Ensure jwt is imported
from jwt import DecodeError
from fastapi import Security, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

def create_access_token(subject: Union[str, Any], expires_delta: int = None) -> str:

    print("insid ehte create acess")
    if expires_delta is None:
        expires_delta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    expires_delta = datetime.utcnow() + expires_delta
    print("subject>>>>>>>>>>>>>>>",subject)
    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def create_refresh_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    print("insid ehte refresssssssssssssssscreate acess")

    if expires_delta is None:
        expires_delta = timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)
    expires_delta = datetime.utcnow() + expires_delta
    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, JWT_REFRESH_SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=403, detail="Token has expired")
    except jwt.PyJWTError as e:
        print("JWT decode error:", e)
        raise HTTPException(status_code=403, detail="Invalid token")
    except Exception as e:
        print("Error decoding token:", e)
        raise HTTPException(status_code=500, detail="Could not decode token")
def decode_refresh_token(token: str):
    try:
        payload = jwt.decode(token, JWT_REFRESH_SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.DecodeError:
        raise HTTPException(status_code=403, detail="Invalid refresh token")


def refresh_access_token(refresh_token: str) -> str:
    payload = decode_refresh_token(refresh_token)
    if payload is None:
        raise HTTPException(status_code=403, detail="Invalid refresh token")
    
    access_token = create_access_token(subject=payload["sub"])
    return access_token