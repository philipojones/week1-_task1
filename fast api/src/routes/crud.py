from fastapi import APIRouter,Depends, HTTPException
from .. import schemas,database,models
from typing import List
from sqlalchemy.orm import Session
from sqlmodel import SQLModel
get_db =database.get_db
router=APIRouter()

@router.get("/crud", response_model=list[schemas.Crud],tags=["crud"])
def read_all(db: Session = Depends(database.get_db)):
    cruds = db.query(models.CRUD).all()
    return cruds

@router.post('/crud', response_model=schemas.Crud,tags=["crud"])
def create(request: schemas.CrudCreate, db: Session = Depends(get_db),tags=["crud"]):
    new_crud = models.CRUD(username=request.username, email=request.email)
    db.add(new_crud)
    db.commit()
    db.refresh(new_crud)
    return new_crud

# Read all CRUD entries
# @app.get("/crud", response_model=list[schemas.Crud])
# def read_all(db: Session = Depends(get_db)):
#     cruds = db.query(models.CRUD).all()
#     return cruds

# Read a single CRUD entry by ID
@router.get("/crud/{crud_id}", response_model=schemas.Crud,tags=["crud"])
def read_by_id(crud_id: int, db: Session = Depends(get_db)):
    crud = db.query(models.CRUD).filter(models.CRUD.id == crud_id).first()
    if crud is None:
        raise HTTPException(status_code=404, detail="CRUD entry not found")
    return crud

# Update an existing CRUD entry
@router.put("/crud/{crud_id}", response_model=schemas.Crud,tags=["crud"])
def update(crud_id: int, request: schemas.CrudCreate, db: Session = Depends(get_db)):
    crud = db.query(models.CRUD).filter(models.CRUD.id == crud_id).first()
    if crud is None:
        raise HTTPException(status_code=404, detail="CRUD entry not found")

    crud.username = request.username
    crud.email = request.email
    db.commit()
    db.refresh(crud)
    return crud

# Delete a CRUD entry by ID
@router.delete("/crud/{crud_id}", response_model=schemas.Crud,tags=["crud"])
def delete(crud_id: int, db: Session = Depends(get_db)):
    crud = db.query(models.CRUD).filter(models.CRUD.id == crud_id).first()
    if crud is None:
        raise HTTPException(status_code=404, detail="CRUD entry not found")

    db.delete(crud)
    db.commit()
    return crud
