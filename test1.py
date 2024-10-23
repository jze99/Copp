from src.queries.orm import orm_data_functions
from src.models import User, Post
import asyncio
temp = orm_data_functions()
temp.create_table(tables=[User.__table__, Post.__table__])