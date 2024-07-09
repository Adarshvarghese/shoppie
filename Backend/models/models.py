from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from pydantic import BaseModel, Field, validator, EmailStr
from typing import Optional
import re
from datetime import date
from config.config import customers_collection
from fastapi import HTTPException
from utils.enum import GenderEnum
app = FastAPI()
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    print("inisde the validation error>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    errors = exc.errors()
    formatted_errors = []
    for err in errors:
        if err["loc"][-1] == "email":
            formatted_errors.append({"errorCode": 1002, "message": "Invalid email address"})
        elif err["loc"][-1] == "dob":
            formatted_errors.append({"errorCode": 1003, "message": "Invalid date of birth"})
        else:
            formatted_errors.append({"errorCode": 1000, "message": err["msg"]})
    return JSONResponse(
        status_code=400,
        content={"errors": formatted_errors},
    )




class Customer(BaseModel):
    
    first_name: str
    
    last_name: str
    email: EmailStr
    dob: Optional[date] = None
    gender: Optional[GenderEnum] = None
    address: Optional[str] = None
    password: str = Field(..., min_length=8)

    @validator('password')
    def validate_password(cls, value):
        if not re.match(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[\W_])[a-zA-Z\d\W_]+$', value):
            raise HTTPException(status_code=400, detail={"errorCode":1001,"message": "Password must contain at least 8 characters, 1 uppercase, 1 lowercase, 1 special character."})
        return value
    
    @validator('email')
    def validate_email(cls, value):
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', value):
            raise ValueError('Invalid email address')
        customers = customers_collection.find_one({"email": value})
        print(">>>>>>>>>>>>>>>>>>>>", customers)
        if(customers):
            raise HTTPException(status_code=400, detail={"errorCode":1001,"message": "Email already exists"})
        return value
    


class CustomerLogin(BaseModel):
    email: EmailStr
    password: str
    
    # @validator('password')
    # def validate_password(cls, value):
    #     if not re.match(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[\W_])[a-zA-Z\d\W_]+$', value):
    #         raise HTTPException(status_code=400, detail={"errorCode":1001,"message": "Password must contain at least 8 characters,"})