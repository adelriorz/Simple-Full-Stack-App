from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Person(BaseModel):
    id: int
    name: str
    age: int

DB: List[Person] = [
    Person(id=1, name="Jamila", age=21),
    Person(id=2, name="John", age=23),
    Person(id=3, name="Juanito", age=26)
]

@app.get("/api")
async def read_root():
    return DB