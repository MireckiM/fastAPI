#import database as _db
import models as _models
import sqlalchemy.orm as _orm
import schema as _schema
import passlib.hash as _hash
import jwt as _jwt


#def get_db():
#    db = _database.SessionLocal()
#    try:
#        yield db
#    finally:
#        db.close()

async def get_user_by_username(username: str, db: _orm.Session):
    return db.query(_models.User).filter(_models.User.username == username).first()

async def register_user(user: _schema.User, db=_orm.Session):

    hashed_password = _hash.bcrypt.hash(user.password)
    user_obj = _models.User(username=username, hashed_password=hashed_password)
    db.add(user_obj)
    db.commit()
    db.refresh(user_obj)
    return user_obj

async def create_token(user: _models.User):
    user_schema_obj = _schema.User.from_orm(user)
    user_dict = user_schema_obj.dict()
    del user_dict["date_created"]

    token = _jwt.encode(user_dict, _JWT_SECRET)

    return dict(access_token = token, token_type="bearer")

