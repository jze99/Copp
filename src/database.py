from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import text, create_engine
from config import settings

# Create the async engine
async_engine = create_async_engine(settings.DATABASE_URL_asyncpg, echo=True)
sync_engine = create_engine(url=settings.DATABASE_URL_psyncopg)

async_sassion = async_sessionmaker(async_engine)
sync_sassion = sessionmaker(sync_engine)

class Base(DeclarativeBase):
    pass