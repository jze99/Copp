from sqlalchemy import text, insert
from database import sync_engine, async_engine, sync_sassion, Base
from models import metadata_obj, user_orm

def create_user():
    Base.metadata.drop_all(sync_engine)
    Base.metadata.create_all(sync_engine)
    
def insert_data():
    with sync_sassion() as session:
        test=user_orm(username="123")
        session.add_all([test])
        session.commit()