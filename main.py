from fastapi import FastAPI, Request, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from router import product , user , category
from db.models import Product
from fastapi.staticfiles import StaticFiles
from db import models
from db.database import engine

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(user.router)
app.include_router(product.router)
app.include_router(category.router)
models.Base.metadata.create_all(bind=engine)