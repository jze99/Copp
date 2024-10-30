from src.queries.orm import orm_data_functions
from src.models import FPM_POO_orm, Data_FPM_POO_orm
import asyncio
temp = orm_data_functions()
temp.create_table(tables=[FPM_POO_orm.__table__, Data_FPM_POO_orm.__table__])