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

load_dotenv(".env")

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello"}

@app.post("/add-book/", response_model=SchemaBook)
def add_book(book: SchemaBook):
    db_book = Book(title=book.title, pages=book.pages, client_id=book.client_id)
    db.session.add(db_book)
    db.session.commit()
    return db_book

@app.post("/add-client/", response_model=SchemaClient)
def add_client(client: SchemaClient):
    db_client = Client(name=client.name, age=client.age, client_id=book.client_id)
    db.session.add(db_client)
    db.session.commit()
    return db_client

@app.get("/books/")
def get_books():
    books = db.session.query(Book).all()
    return books

if __name__== "__main__":
    uvicorn.run(app, host = "0.0.0.0", port=8001)