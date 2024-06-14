from pydantic import BaseModel

class Customer(BaseModel):
    cust_id:int
    name:str
    email:str
    dob:str
    gender:str
    address:str
    password:str
