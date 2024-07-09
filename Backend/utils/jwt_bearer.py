from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from .jwt_handler import decode_jwt

class JwtBearer(HTTPBearer):
    def __init__(self, auto_Error: bool = True):
        super(JwtBearer, self).__init__(auto_error=auto_Error)
        
    async def __call__(self, request: Request):
        credentials : HTTPAuthorizationCredentials = await super(JwtBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403, detail="In  valid credentials")
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail="In  valid credentials")
    def verify_jwt(self, jwttoken: str):
        is_token_valid : bool = False
        payload = decode_jwt(jwttoken)
        if payload:
            is_token_valid = True
            return payload
        
        
        
        