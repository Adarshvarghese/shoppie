from fastapi import FastAPI
from routes.routes import endpoints

app=FastAPI()

app.include_router(endpoints)