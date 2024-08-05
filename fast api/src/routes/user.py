from fastapi import APIRouter
from pydantic import BaseModel
router=APIRouter()

class Item(BaseModel):
 pass

router.get('/',tags=['user'])
def index():
 return {'data':{'name':'philipo'}}
@router.post("/items/",tags=["user"])
async def create_item(item: Item):
    return "item"

@router.post('/',tags=['user'])
def create ():
    return "me"