from typing import Optional
from pydantic import BaseModel

class todo(BaseModel):
    id:int
    name: str
    description: str
    completed: bool = False

class todoInput(BaseModel):
    name: str
    description: str