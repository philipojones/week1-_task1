from pydantic import BaseModel

class CrudBase(BaseModel):
    username: str
    email: str

class CrudCreate(CrudBase):
    pass

class Crud(CrudBase):
    id: int

    class Config:
        orm_mode = True
