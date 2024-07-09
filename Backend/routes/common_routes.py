from fastapi import APIRouter, HTTPException
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
from utils.auth_utils import create_access_token, create_refresh_token
from pydantic import ValidationError




common_endpoints=APIRouter()

@common_endpoints.post("/customers/register")
def register_customer(customer: Customer):
    customer_id = str(uuid.uuid4())
    customer_dict = dict(customer)
    customer_dict["cust_id"] = customer_id
    customer_dict["created_at"] = datetime.datetime.now()
    if customer_dict["dob"]:
        customer_dict["dob"] = customer_dict["dob"].isoformat()

    # Hash the password
    hashed_password = bcrypt.hashpw(customer_dict["password"].encode('utf-8'), bcrypt.gensalt())
    customer_dict["password"] = hashed_password

    try:
        result = customers_collection.insert_one(customer_dict)
        customer = customers_collection.find_one({"email": customer_dict["email"]})
        print("customers>>>>>>>>>>>>>>>>>>>>>", customer["cust_id"])
        access_token = create_access_token(customer["cust_id"])
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
    except ValidationError as e:
        print("validation error >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",e)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"{e}Customer not registered")