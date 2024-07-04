from typing import Optional
from pydantic import BaseModel, Field, validator
import re
from config.config import customers_collection

class Customer(BaseModel):
    first_name: str
    last_name: str
    email: str
    dob: Optional[str] = None
    gender: Optional[str] = None
    address: Optional[str] = None
    password: str = Field(..., min_length=8)

    @validator('password')
    def validate_password(cls, value):
        if not re.match(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[\W_])[a-zA-Z\d\W_]+$', value):
            raise ValueError('Password must contain at least one digit, one lowercase letter, one uppercase letter, and one special character')
        return value
    
    @validator('email')
    def validate_email(cls, value):
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', value):
            raise ValueError('Invalid email address')
        customers = customers_collection.find_one({"email": value})
        if(customers):
            print("llllllllllllllllllllllllllllll")
            raise HTTPException(status_code=400, detail='Invalid email address')
        return value