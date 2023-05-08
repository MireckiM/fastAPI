import os
import uvicorn
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db
from dotenv import load_dotenv

from models import Client
from models import Book
from schema import Book as SchemaBook
from schema import Client as SchemaClient

from fastapi.middleware.cors import CORSMiddleware

from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

load_dotenv(".env")

fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "fakehashedsecret",
        "disabled": False,
    },
    "alice": {
        "username": "alice",
        "full_name": "Alice Wonderson",
        "email": "alice@example.com",
        "hashed_password": "fakehashedsecret2",
        "disabled": True,
    },
}

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None

def fake_decode_token(token):
    return User(
        username=token + "fakedecoded", email="john@example.com", full_name="John Doe"
    )


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = fake_decode_token(token)
    return user


@app.get("/users/me")
async def read_users_me(current_user: Annotated[User, Depends(get_current_user)]):
    return current_user

@app.get("/")
async def root():
    return {"message": "Witam"}

@app.get("/items/")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}

@app.post("/add-book/", response_model=SchemaBook)
def add_book(book: SchemaBook):
    db_book = Book(title=book.title, pages=book.pages, client_id=book.client_id)
    db.session.add(db_book)
    db.session.commit()
    return db_book

@app.post("/add-client/", response_model=SchemaClient)
def add_client(client: SchemaClient):
    db_client = Client(name=client.name, age=client.age)
    #db_client = Client(name=client.name, age=client.age, client_id=book.client_id)
    db.session.add(db_client)
    db.session.commit()
    return db_client

@app.get("/books/")
def get_books():
    books = db.session.query(Book).all()
    return books

@app.get("/clients/")
def get_clients():
    clients = db.session.query(Client).all()
    return clients

if __name__== "__main__":
    uvicorn.run(app, host = "0.0.0.0", port=8001)