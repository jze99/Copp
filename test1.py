import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.models import User,Post
from src.queries.orm import orm_data_functions



temp = orm_data_functions()
temp.create_user(tables=[User.__table__ , Post.__table__])
pass