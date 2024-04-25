from typing import Optional
from pydantic import BaseModel

class todo(BaseModel):
    id:int
    name: str
    description: str

class todoInput(BaseModel):
    name: str
    description: str