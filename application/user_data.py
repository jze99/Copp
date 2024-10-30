import flet as ft
from designer import logic_base
import asyncio

class data(logic_base):
    
    fresh_data_time_employment = []
    fresh_data_time_opk_poo = []
    user_name:str="123"
    def __init__(self,page:ft.Page):
        self.page = page
        self.load_data_time()
        
    def load_employment_data_time(self):
        from src.queries.orm import orm_data_functions
        from src.models import Data_employment_orm
        temp = orm_data_functions().select_data(table=Data_employment_orm)
        temp_data = []
        for t in temp:
            temp_data.append(t.data)
        sorted_dates = sorted(temp_data, key=self.parse_date)
        for s in sorted_dates:
            data.fresh_data_time_employment.append(ft.dropdown.Option(text=s))
            
    def load_opk_poo_data_time(self):
        from src.queries.orm import orm_data_functions
        from src.models import Data_FPM_POO_orm
        temp = orm_data_functions().select_data(table=Data_FPM_POO_orm)
        temp_data = []
        for t in temp:
            temp_data.append(t.data)
        sorted_dates = sorted(temp_data, key=self.parse_date)
        for s in sorted_dates:
            data.fresh_data_time_opk_poo.append(ft.dropdown.Option(text=s))
            
    def load_data_time(self):
        data.fresh_data_time_opk_poo.clear()
        data.fresh_data_time_employment.clear()
        self.load_employment_data_time()
        self.load_opk_poo_data_time()
        self.page.update()


