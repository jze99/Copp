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

            controls=[
                ft.Row(
                    expand=True,
                    controls=[
                        ft.Container(
                            expand=True,
                            padding=ft.padding.all(0),
                            bgcolor=design.color["Wafer"],
                            content=ft.Column(
                                
                                controls=[
                                    ft.Row(
                                        expand=True,
                                        controls=[
                                            ft.TextButton(# кнопка для вкладки сохранить
                                                icon=ft.icons.SAVE_AS_ROUNDED,
                                                icon_color=design.color["Nevada"],
                                                text="сохранить",
                                                style=ft.ButtonStyle(
                                                    icon_size=32,
                                                    overlay_color=design.color["Nevada Lite"],
                                                    color=design.color["Nevada"]
                                                )
                                            ),
                                            ft.TextButton(# кнопка для вкладки выгрузить
                                                icon=ft.icons.CLOUD_UPLOAD_ROUNDED,
                                                icon_color=design.color["Nevada"],
                                                text="выгрузить",
                                                style=ft.ButtonStyle(
                                                    icon_size=32,
                                                    overlay_color=design.color["Nevada Lite"],
                                                    color=design.color["Nevada"]
                                                )
                                            )
                                        ]
                                    )
                                ]
                            ),
                        ),
                        ft.Column(
                            expand=0.8,
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
                ),
            ]
        )
    
    def return_page(self):
        return self.main_page
    
    def go_to_next(self,e):
        pass