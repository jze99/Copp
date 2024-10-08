import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import flet as ft
from designer import Text, TextField, Button, design
from src.queries.orm import orm_data_functions
from src.models import User

class main_page:
    
    def __init__(self, page):        
        self.page = page
        
        self.login = TextField(help_text="Login")
        self.password = TextField(help_text="Password")
        
        
        
        self.main_page=ft.Column(
            #expand=True,
            controls=[
                ft.Row(
                    #expand=True,
                    controls=[
                        ft.Column(
                            expand=True,
                            controls=[
                                ft.Container(
                                    bgcolor="#FFFFFF",
                                    width=100,
                                    height=100,
                                )
                            ]
                        ),
                        ft.Column(
                            expand=True,
                            controls=[
                                ft.IconButton(
                                    icon=ft.icons.TABLE_ROWS_ROUNDED,
                                    icon_size=24,
                                    icon_color=design.color["Nevada"],
                                    #on_click=self.open_drawer,
                                    style=ft.ButtonStyle(
                                        #shadow_color=design.color["Nevada"],
                                        overlay_color=design.color["Nevada Lite"],
                                        #bgcolor=design.color["Nevada"],
                                    ),
                                )
                            ]
                        )
                    ]
                )
            ]
        )
    
    def return_page(self):
        return self.main_page
    
    def go_to_next(self,e):
        pass