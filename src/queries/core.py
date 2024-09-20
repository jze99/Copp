from sqlalchemy import text
from src.database import async_engine, sync_engine
from src.models import metadata_obj

def create_table_user():
    metadata_obj.create_all(sync_engine)
    
    