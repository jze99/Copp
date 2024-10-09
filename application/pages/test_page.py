import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import flet as ft
from designer import Text, TextField, Button, design
from src.queries.orm import orm_data_functions
from src.models import User

class test_page:
    
    def __init__(self, page):        
        self.page = page
        
        self.login = TextField(help_text="Login")
        self.password = TextField(help_text="Password")
        
        self.main_page=ft.View(
            route="/test",
            controls=[
                ft.Row(
                    expand=True,
                    alignment=ft.MainAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.START,
                    controls=[
                        ft.Column(
                               expand=True,
                               scroll=ft.ScrollMode.ADAPTIVE,
                               horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                               controls=[
                                   ft.Container(
                                       height=100,
                                       width=100,
                                       bgcolor=design.color["Nevada"]
                                   )
                               ]
                           ),
                    ]
                ),
                ft.Row(
                    
                    controls=[
                        ft.Container(
                            expand=True,
                            height=10,
                            bgcolor=design.color["Nevada"]
                        )
                    ]
                )
            ],
            bgcolor=design.color["Rodeo Dust"],
            scroll=True,
            
        )
    
    def return_page(self):
        return self.main_page
    
    def go_to_next(self,e):
        pass