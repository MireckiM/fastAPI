#import database as _db
import models as _models
import sqlalchemy.orm as _orm
import schema as _schema

#def get_db():
#    db = _database.SessionLocal()
#    try:
#        yield db
#    finally:
#        db.close()

async def get_user_by_username(username: str, db: _orm.Session):
    return db.query(_models.User).filter(_models.User.username == username).first()

async def register_user(user: _schema.User, db=_orm.Session):
    return 0