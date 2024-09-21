from sqlalchemy import text, insert
from database import sync_engine, async_engine, sync_sassion, Base
from models import FPM_POO_orm
import openpyxl

def create_user():
    Base.metadata.drop_all(sync_engine)
    Base.metadata.create_all(sync_engine)

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

        