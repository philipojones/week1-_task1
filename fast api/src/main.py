from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import schemas, models
from .database import SessionLocal, engine,get_db
from sqlmodel import SQLModel
from .routes import crud,user

app = FastAPI()

# Create tables in the database
SQLModel.metadata.create_all(bind=engine)


app.include_router(crud.router)

app.include_router(user.router)
