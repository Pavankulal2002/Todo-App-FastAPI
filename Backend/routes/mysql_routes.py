# todo_router.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select,update
from sqlalchemy.orm import Session
from databases.mysql import engine
from schemas.mysql_schema import todo
from models.mysql_todo import todos

router = APIRouter()

# Dependency to get the database session
def get_db():
    db = Session(bind=engine)
    try:
        yield db
    finally:
        db.close()

# CRUD operations
@router.post("/todos", response_model=todo)
def create_todo(todo: todo, db: Session = Depends(get_db)):
    new_todo = todos.insert().values(name=todo.name, description=todo.description)
    db.execute(new_todo)
    db.commit()
    return todo

# @router.get("/todos/", response_model=list[todo])
# def read_todos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
#     query = todos.select().offset(skip).limit(limit)
#     return db.execute(query).fetchall()

@router.get("/todos", response_model=list[todo])
def read_todos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    query = todos.select().offset(skip).limit(limit)
    result = db.execute(query).fetchall()
    todos_list = [{"id": row.id, "name": row.name, "description": row.description,"completed":row.completed} for row in result]
    return todos_list


# @router.get("/todos/", response_model=list[todo])
# def read_todos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
#     query = select([todos.c.id, todos.c.name, todos.c.description]).offset(skip).limit(limit)
#     return db.execute(query).fetchall()

# @router.get("/todos/{todo_id}", response_model=todo)
# def read_todo(todo_id: int, db: Session = Depends(get_db)):
#     query = select([todos]).where(todos.c.id == todo_id)
#     result = db.execute(query).fetchone()
#     if result is None:
#         raise HTTPException(status_code=404, detail="Todo not found")
#     return result

@router.get("/todos/{todo_id}", response_model=todo)
def read_todo(todo_id: int, db: Session = Depends(get_db)):
    query = todos.select().where(todos.c.id == todo_id)
    result = db.execute(query).fetchone()
    if result is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    # Manually convert result to dictionary
    todo_dict = {
        "id": result[0],
        "name": result[1],
        "description": result[2]
    }
    
    return todo(**todo_dict)



@router.put("/todos/{todo_id}", response_model=todo)
def update_todo(todo: todo, db: Session = Depends(get_db)):
    update_query = todos.update().where(todos.c.id == todo.id).values(
        name=todo.name, description=todo.description
    )
    db.execute(update_query)
    db.commit()
    return todo

@router.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    delete_query = todos.delete().where(todos.c.id == todo_id)
    db.execute(delete_query)
    db.commit()
    return {"message": "Todo deleted successfully"}


@router.patch("/todos/{todo_id}", response_model=todo)
def patch_todo(todo: todo, db: Session = Depends(get_db)):
    update_query = update(todos).where(todos.c.id == todo.id)
    update_query_1 = update_query.values(completed=todo.completed)
    db.execute(update_query_1)
    db.commit()
    return todo


