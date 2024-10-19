import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import flet as ft
from designer import text_button, design
from src.queries.orm import orm_data_functions
from src.models import User

class main_page:
    
    def __init__(self, page):        
        self.page = page
        self.file_picer = ft.FilePicker()
        self.page.overlay.append(self.file_picer)     
        
        
        self.view_work =  ft.Container(expand=True)
        
        self.load_buttons = ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        text_button(
                            on_clic=self.button_load_opk_poo,
                            icon=ft.icons.OTHER_HOUSES_ROUNDED,
                            text="загрузить опк поо"
                        )
                    ]
                ),
                ft.Row(
                    controls=[
                        text_button(
                            on_clic=self.button_load_employment,
                            icon=ft.icons.PEOPLE_ALT_ROUNDED,
                            text="загрузить рабочих"
                        )
                    ]
                )
            ]
        )
        
        self.upload_buttons = ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        text_button(
                            on_clic=self.button_save_opk_poo,
                            icon=ft.icons.OTHER_HOUSES_ROUNDED,
                            text="сохранить опк поо"
                        )
                    ]
                ),
                ft.Row(
                    controls=[
                        text_button(
                            on_clic=self.button_save_employment,
                            icon=ft.icons.PEOPLE_ALT_ROUNDED,
                            text="сохранить рабочих"
                        )
                    ]
                )
            ]
        )
        
        self.container_left_column = ft.Container()
        
        self.left_column = ft.Column(
            alignment=ft.MainAxisAlignment.START,
            controls=[
                ft.Row(
                    controls=[
                        text_button(
                            on_clic=self.button_upload,
                            icon=ft.icons.SAVE_AS_ROUNDED,
                            text="Сохранить"
                        ),
                        text_button(
                            on_clic=self.button_load,
                            icon=ft.icons.CLOUD_UPLOAD_ROUNDED,
                            text="Загрузить"
                        ),
                    ]
                ),
                self.container_left_column
            ]
        )
        
        self.right_column = ft.Column(
            expand=True,
            controls=[
                ft.Row(
                    expand=True,
                    controls=[
                        self.view_work
                    ]
                )
            ]
        )
        
        self.main_page = ft.Row(
            vertical_alignment=ft.CrossAxisAlignment.START,
            controls=[
                self.left_column,
                self.right_column
            ]
        )
    
    def button_save_employment(self,e):
        from designer import save_Employment
        self.view_work.content=save_Employment(
                text="сохранить рабочих",
                file_picer=self.file_picer,
            )
        self.view_work.update()
        
    def button_save_opk_poo(self,e):
        from designer import save_OPK_POO
        self.view_work.content=save_OPK_POO(
                text="сохранить опк поо",
                file_picer=self.file_picer,
            )
        self.view_work.update()
        pass
    
    
    def button_load_employment(self,e):
        from designer import load_Employment
        self.view_work.content=load_Employment(
                text="загрузить рабочих",
                file_picer_derictory=self.file_picer,
            )
        self.view_work.update()
        
    def button_load_opk_poo(self,e):
        from designer import load_OPK_POO
        self.view_work.content=load_OPK_POO(
                text="загрузить опк поо",
                file_picer_derictory=self.file_picer,
            )
        self.view_work.update()
    
    def button_upload(self,e):
        self.container_left_column.content = self.upload_buttons
        self.container_left_column.update()
    
    def button_load(self,e):
        self.container_left_column.content = self.load_buttons
        self.container_left_column.update()
    
    def return_page(self):
        return self.main_page
        