# import os
# from passlib.context import CryptContext
# from datetime import datetime, timedelta
# from typing import Union, Any
# from jwt import DecodeError
from fastapi import Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

ACCESS_TOKEN_EXPIRE_MINUTES = 30  # 30 minutes
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7 # 7 days
ALGORITHM = "HS256"
JWT_SECRET_KEY = "narscbjim@$@&^@&%^&RFghgjvbdsha"   # should be kept secret
JWT_REFRESH_SECRET_KEY = "13ugfdfgh@#$%^@&jkl45678902"

# password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# def get_hashed_password(password: str) -> str:
#     return password_context.hash(password)


# def verify_password(password: str, hashed_pass: str) -> bool:
#     return password_context.verify(password, hashed_pass)

# def create_access_token(subject: Union[str, Any], expires_delta: int = None) -> str:
#     if expires_delta is not None:
#         expires_delta = datetime.utcnow() + expires_delta
#     else:
#         expires_delta = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
#     to_encode = {"exp": expires_delta, "sub": str(subject)}
#     encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, ALGORITHM)
#     return encoded_jwt


# def create_refresh_token(subject: Union[str, Any], expires_delta: int = None) -> str:
#     if expires_delta is not None:
#         expires_delta = datetime.utcnow() + expires_delta
#     else:
#         expires_delta = datetime.utcnow() + timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)
    
#     to_encode = {"exp": expires_delta, "sub": str(subject)}
#     encoded_jwt = jwt.encode(to_encode, JWT_REFRESH_SECRET_KEY, ALGORITHM)
#     return encoded_jwt

# def decode_access_token(token :str):
#     try:
#         payload = jwt.decode(token, JWT_SECRET_KEY, algorithms = [ALGORITHM])
#         return payload
#     except DecodeError as e:
#         print(">>>>>>>>>>>>>decode error ", e)
#         return None
    
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
    if expires_delta is None:
        expires_delta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    expires_delta = datetime.utcnow() + expires_delta
    print("subject>>>>>>>>>>>>>>>",subject)
    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def create_refresh_token(subject: Union[str, Any], expires_delta: int = None) -> str:
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
