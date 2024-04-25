from fastapi import APIRouter # type: ignore
from models.mongodb_todo import list_serial,individual_serial
from databases.mongodb import collection
from schemas.mongodb_schema import Todo
from bson import ObjectId

router=APIRouter()

@router.get("/todos")
async def get_todos():
    todos=list_serial(collection.find())
    return todos

@router.post("/todos")
async def post_todos(todo:Todo):
    collection.insert_one(dict(todo))
     
@router.put("/todos/{id}")
async def put_todo(id:str, todo:Todo):
    collection.find_one_and_update({"_id":ObjectId(id)},{"$set":dict(todo)})

@router.delete("/todos/{id}")
async def delete_todos(id :str ):
    collection.find_one_and_delete({"_id":ObjectId(id)})



