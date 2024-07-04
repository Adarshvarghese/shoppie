from fastapi import APIRouter
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
from utils.utils import create_access_token, create_refresh_token

endpoints=APIRouter()



from bson import ObjectId
from schema.schemas import list_serial

@endpoints.get("/customers/get")
def get_all_customers():
    customers = list_serial(customers_collection.find())

    return {"data": customers, "message": "Customers retrieved successfully"} 

from fastapi import HTTPException

@endpoints.post("/customers/register")
def register_customer(customer: Customer):
    customer_id = str(uuid.uuid4())
    customer_dict = dict(customer)
    customer_dict["cust_id"] = customer_id
    customer_dict["created_at"] = datetime.datetime.now()

    # Hash the password
    hashed_password = bcrypt.hashpw(customer_dict["password"].encode('utf-8'), bcrypt.gensalt())
    customer_dict["password"] = hashed_password

    try:
        result = customers_collection.insert_one(customer_dict)
        access_token = create_access_token(customer_id)
        refresh_token = create_refresh_token(customer_id)

        if result.inserted_id:
            return {
                "message": "Customer registered successfully",
                "customer_id": customer_id,
                "access_token": access_token,
                "refresh_token": refresh_token
            }
    except HTTPException as e:
        print("inide >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Customer not registered")
@endpoints.get('/customers/{id}')
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