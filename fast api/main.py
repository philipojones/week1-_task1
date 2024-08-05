from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
from src.routes import crud,user



app = FastAPI()
app.include_router(crud.router)

app.include_router(user.router)