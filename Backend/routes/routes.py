from fastapi import APIRouter
from config.config import customers_collection
from serializer.serializer import convert_all_customer_details,convert_customer_details
from bson import ObjectId
endpoints=APIRouter()

@endpoints.get('/')
def home():
    return {"message":"get request success"}
@endpoints.get('/customers/{id}')
def get_all_customers(id:str):
    customers= customers_collection.find_one({"_id":ObjectId(id)})

    print(customers,">>>>>>>>>>")
    serialized_customers=convert_customer_details(customers)
    print(serialized_customers)
    return {"data":serialized_customers,"message":"random message"}