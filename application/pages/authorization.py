import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import flet as ft
from designer import Text, TextField, Button
from src.queries.orm import orm_data_functions
from src.models import User

class authorization:
    
    def __init__(self, page):
        self.page = page
        
        self.login = TextField(help_text="Login")
        self.password = TextField(help_text="Password")
        
        self.main_page=ft.Column(
            expand=True,
            controls=[
                ft.Row(expand=True, controls=[ft.Container(height=100)]),
                ft.Row(expand=True, controls=[Text(value="COPP",size=68)],alignment=ft.MainAxisAlignment.CENTER),
                ft.Row(expand=True, controls=[self.login],alignment=ft.MainAxisAlignment.CENTER),
                ft.Row(expand=True, controls=[self.password],alignment=ft.MainAxisAlignment.CENTER),
                ft.Row(expand=True, controls=[Button(text="Войти",meth=self.go_to_next)],alignment=ft.MainAxisAlignment.CENTER),
                ft.Row(expand=True, controls=[ft.Container(height=100)]),
            ]
        )
    
    def return_page(self):
        return self.main_page
    
    def go_to_next(self,e):
        temp = orm_data_functions()
        user = temp.select_user(tabel=User, login=self.login.value, passw=self.password.value)
        if len(user) > 0:
            self.page.go("/main")
        else:
            pass