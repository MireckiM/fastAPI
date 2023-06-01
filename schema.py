from pydantic import BaseModel
import datetime as _dt

class Book(BaseModel):
    title: str
    pages: int
    client_id: int

    class Config:
        orm_mode = True


class Client(BaseModel):
    name: str
    age: int

    class Config:
        orm_mode = True


class User(BaseModel):
    username: str
    password: str

    class Config:
        orm_mode = True


class AuthDetails(BaseModel):
    username: str
    password: str


