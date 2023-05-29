import os
import uvicorn

# import jwt
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db
from dotenv import load_dotenv

from models import Client
from models import Book
from schema import Book as SchemaBook
from schema import Client as SchemaClient

from fastapi.middleware.cors import CORSMiddleware

from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, status, Security
from fastapi.security import (
    OAuth2PasswordBearer,
    OAuth2PasswordRequestForm,
    HTTPAuthorizationCredentials,
    HTTPBearer,
)
from passlib.context import CryptContext
from datetime import datetime, timedelta
from pydantic import BaseModel
from schema import AuthDetails
from auth import AuthHandler

load_dotenv(".env")

users = []
auth_handler = AuthHandler()

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


class AuthHandler:
    security = HTTPBearer()
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    secret = "SECRET"

    def get_password_hash(self, password):
        return self.pwd_context.hash(password)

    def verify_password(self, plain_password, hashed_password):
        return self.pwd_context.verify(plain_password, hashed_password)

    def encode_token(self, user_id):
        payload = {
            "exp": datetime.utcnow() + timedelta(days=1, minutes=10),
            "iat": datetime.utcnow(),
            "sub": user_id,
        }
        return jwt.encode(payload, self.secret, algorithm="HS256")

    def decode_token(self, token):
        try:
            payload = jwt.decode(token, self.secret, algorithms=["HS256"])
            return payload["sub"]
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="Signature has expired")
        except jwt.InvalidTokenError as e:
            raise HTTPException(status_code=401, detail="Invalid token")

    def auth_wrapper(self, auth: HTTPAuthorizationCredentials = Security(security)):
        return self.decode_token(auth.credentials)


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
    if not token:
        return None

    user = fake_decode_token(token)
    return user


@app.post("/register", status_code=201)
def register(auth_details: AuthDetails):
    if any(x["username"] == auth_details.username for x in users):
        raise HTTPException(status_code=400, detail="Username is taken")
    hashed_password = auth_handler.get_password_hash(auth_details.password)
    users.append({"username": auth_details.username, "password": hashed_password})
    return


@app.post("/login")
def login(auth_details: AuthDetails):
    user = None
    for x in users:
        if x["username"] == auth_details.username:
            user = x
            break

    if (user is None) or (
        not auth_handler.verify_password(auth_details.password, user["password"])
    ):
        raise HTTPException(status_code=401, detail="Invalid username or password")
    token = auth_handler.encode_token(user["username"])
    return {"token": token}


@app.get("/unprotected")
def unprotected():
    return {"unprotected"}


@app.get("/protected")
def protected(username=Depends(auth_handler.auth_wrapper)):
    return {"name": username}


@app.get("/users/me")
async def read_users_me(current_user: Annotated[User, Depends(get_current_user)]):
    return current_user


@app.get("/")
async def root():
    return {"message": "Witam"}


@app.get("/items/")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}


# zmienic endpointy na protected
@app.post("/add-book/", response_model=SchemaBook)
def add_book(book: SchemaBook = Depends(auth_handler.auth_wrapper)):
    db_book = Book(title=book.title, pages=book.pages, client_id=book.client_id)
    db.session.add(db_book)
    db.session.commit()
    return db_book


@app.post("/add-client/", response_model=SchemaClient)
def add_client(client: SchemaClient):
    db_client = Client(name=client.name, age=client.age)
    # db_client = Client(name=client.name, age=client.age, client_id=book.client_id)
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


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
