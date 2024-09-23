from sqlalchemy import text, insert, select, func
from database import sync_engine, async_engine, sync_sassion, Base
from models import FPM_POO_orm
import openpyxl

def create_user():
    with sync_sassion() as session:
        Base.metadata.drop_all(sync_engine)
        Base.metadata.create_all(sync_engine)
        session.commit()

def read_xlsx_file(file_path):
    # Load the xlsx file
    wb = openpyxl.load_workbook(file_path)
    sheet = wb["ФПМ ПОО"]

    # Initialize an empty list to store the data
    data = []

    # Iterate over the rows in the sheet
    for row in sheet.iter_rows(values_only=True):
        # Append each row to the data list
        data.append(list(row))

    return data
    

def insert_data(data):
    with sync_sassion() as session:
        session.add_all(data)
        session.commit()

def date_between(date_column, start, end):
    start_month, start_year = map(int, start.split('.'))
    end_month, end_year = map(int, end.split('.'))
    return (date_column >= f'{start_month}.{start_year}') & (date_column <= f'{end_month}.{end_year}')

def select_data():
    with sync_sassion() as session:
        query = session.query(FPM_POO_orm).filter(date_between(FPM_POO_orm.data, '7.2024', '9.2024'))
        result = session.execute(query)
        return result.scalars().all()
    
        