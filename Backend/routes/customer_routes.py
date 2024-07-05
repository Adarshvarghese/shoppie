from fastapi import APIRouter, Depends
from config.config import customers_collection
from serializer.serializer import convert_all_customer_details,convert_customer_details
from bson import ObjectId
import random
from enum import Enum
from pydantic import BaseModel
import uuid
import datetime 
from config.config import customers_collection
from models.models import Customer
import bcrypt
from utils.auth_utils import create_access_token, create_refresh_token, get_current_user
from pydantic import ValidationError
from passlib.context import CryptContext
from bson import ObjectId
from schema.schemas import list_serial
from fastapi import HTTPException



customer_endpoints=APIRouter()

@customer_endpoints.get("/customers/get")
def get_all_customers():
    customers = list_serial(customers_collection.find())

    return {"data": customers, "message": "Customers retrieved successfully"} 



@customer_endpoints.get('/customers/{id}')
def get_by_customer_id(id:str):
    try:
        customers = customers_collection.find_one({"_id": ObjectId(id)})
        print("type of the customes id", type(customers["_id"]))
        customers["_id"] = str(customers["_id"])  # Convert _id to string
        print(customers, "<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        return {"data": customers, "message": "Customer retrieved successfully"}
    except ValueError as e:
        print(e)
    except:
        return {"data": None, "message": "Customer not found"}


password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
@customer_endpoints.get("/user/me")

def get_customer_details(user: dict = Depends(get_current_user)):

    
    print("user.................", user['sub'])
    try:
        print("customer<<<<<<<<<<<<<", user['sub'])
        customer = customers_collection.find_one({"cust_id":user["sub"]})
        customer["_id"] = str(customer["_id"]) 
        import pdb
        pdb.set_trace()
        return {"data": customer, "message": "Customers retrieved successfully"}
    except Exception as e:
        print(">>>>>>>>>>>>>>>",e)