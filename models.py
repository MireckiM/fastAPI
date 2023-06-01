from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import passlib.hash as _hash

Base = declarative_base()

class Book(Base):
    __tablename__ = "book"
    id = Column(Integer, primary_key=True,index=True)
    title = Column(String)
    pages = Column(Integer)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())
    client_id = Column(Integer, ForeignKey("client.id"))

    client = relationship("Client")


class Client(Base):
    __tablename__ = "client"
    id = Column(Integer,primary_key=True)
    name = Column(String)
    age = Column(Integer)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True,index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())

    def verivy_passsword(self, password: str):
        return _hash.bcrypt.verify(password, self.hashed_password)