import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import flet as ft
from designer import Text, TextField, Button, design, TextFielDirectory
from src.queries.orm import orm_data_functions
from src.models import User

class main_page:
    
    def __init__(self, page):        
        self.page = page
        self.state_left_page:bool=True
        
        self.page_load_FPM_POO = ft.Column(
            controls=[
                ft.Row(
                    #expand=True,
                    controls=[
                        TextFielDirectory(),
                        ft.IconButton(
                            icon=ft.icons.DRIVE_FILE_MOVE_RTL_ROUNDED,
                            icon_color=design.color["Nevada"],
                            icon_size=40,
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=10),
                                overlay_color=design.color["Nevada Lite"]
                            ),
                        )
                    ]
                )
            ]
        )
        
        self.main_viwe=ft.Container(
            expand=True,
            content=self.page_load_FPM_POO
        )
        
        self.column_upload_left = ft.Column(
            controls=[
                ft.Container(bgcolor="#ffffff",height=100,width=100)
            ]
        )
        
        self.column_load_left = ft.Column(
            controls=[
                ft.Container(bgcolor="#000000",height=100,width=100)
            ]
        )
        
        self.interactiv_left_column=ft.Container(
            content=self.column_load_left
        )
        
        self.left_page_on=ft.Column(
            controls=[
                ft.Row(  
                    controls=[
                        ft.TextButton(# кнопка для вкладки сохранить
                            icon=ft.icons.SAVE_AS_ROUNDED,
                            icon_color=design.color["Nevada"],
                            text="сохранить",
                            style=ft.ButtonStyle(
                                icon_size=32,
                                overlay_color=design.color["Nevada Lite"],
                                color=design.color["Nevada"]
                            ),
                            on_click=self.column_upload
                        ),
                        ft.TextButton(# кнопка для вкладки выгрузить
                            icon=ft.icons.CLOUD_UPLOAD_ROUNDED,
                            icon_color=design.color["Nevada"],
                            text="выгрузить",
                            style=ft.ButtonStyle(
                                icon_size=32,
                                overlay_color=design.color["Nevada Lite"],
                                color=design.color["Nevada"]
                            ),
                            on_click=self.column_load
                        )
                    ]
                ),
                self.interactiv_left_column
            ]
        )
        self.anim_swetcher=ft.Container(
            content=self.left_page_on
        )
        
        self.main_page=ft.Row(
            expand=True,
            controls=[
                self.anim_swetcher,
                ft.Column(
                    #expand=True,
                    controls=[
                        ft.Row(
                            #expand=True,
                            controls=[
                                ft.IconButton(
                                    icon=ft.icons.TABLE_ROWS_ROUNDED,
                                    icon_color=design.color["Nevada"],
                                    icon_size=32,
                                    style=ft.ButtonStyle(
                                        shape=ft.RoundedRectangleBorder(radius=10),
                                        overlay_color=design.color["Nevada Lite"]
                                    ),
                                    on_click=self.anim_left_column
                                )
                            ]
                        ),
                        ft.Row(
                            controls=[self.main_viwe]
                        )
                    ]
                ),
            ]
        )
    
    def return_page(self):
        return self.main_page
    
    def column_upload(self,e):
            self.interactiv_left_column.content=self.column_upload_left
            self.interactiv_left_column.update()
    def column_load(self,e):
            self.interactiv_left_column.content=self.column_load_left
            self.interactiv_left_column.update()
    
    def anim_left_column(self,e):
        if self.state_left_page:
            self.state_left_page=False
            self.anim_swetcher.content=ft.Container().content
        else:
            self.state_left_page=True
            self.anim_swetcher.content=self.left_page_on
        self.anim_swetcher.update()
        
    
    def go_to_next(self,e):
        pass