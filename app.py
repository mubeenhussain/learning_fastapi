from fastapi import FastAPI
from core.database import engine, Base
from api.v1.app import api_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="My E-commerce Project")

app.include_router(api_router, prefix="/api/v1")