import time
import jwt
from decouple import config

JWT_SECRET_KEY = config("SECRET")
JWT_ALGORITHM = config("ALGORITHM")


def token_response(token: str)
    return {
        "access_token":token
    }
    
def sign_jwt(user_id: str):
    payload ={
        "user_id": user_id,
        "expiry": time.time() + 3600
        
    }
    token = jwt.encode(payload, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)

def decode_jwt(token: str):
    try:
        decode_jwt = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
        return decode_jwt if decode_token['expires'] >= time.time() else  None
    except:
        return {}