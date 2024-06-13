from fastapi import APIRouter

endpoints=APIRouter()

@endpoints.get('/')
def home():
    return {"message":"get request success"}