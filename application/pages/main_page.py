import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))


import flet as ft
from designer import Text, TextField, Button, design #page_load_FPM_POO
from src.queries.orm import orm_data_functions
from src.models import User
from work_xlsx.load_xlsx import craete_data_base_xlsx

class main_page:
    
    def __init__(self, page):    
        self.page = page      

        self.file_picer = ft.FilePicker()
        self.page.overlay.append(self.file_picer)     
        self.file_picer.on_result = self.file_picer_result

        self.state_left_page:bool=True
        
        
        """
        дробдавн для отображения страницы
        """
        self.drop_down_sheet = ft.Dropdown(
            border_color=design.color["Nevada"],
            color=design.color["White Rock"],
            #height=100,
            #width=200,
            
        )
        
        """
        поле для отображения пути
        """
        self.text_fild_loder_file = ft.TextField(
            expand=True,
            #width=500,
            dense=True,
            read_only=True,
            color=design.color["White Rock"],
            border_color=design.color["Nevada"],
            text_size=40,
            cursor_color=design.color["Nevada"],
            hint_text="File Load",
            text_style=ft.TextStyle(
                color=design.color["White Rock"]
            ),
        )



        """
        блок с FPM_POO
        """
        self.page_load_FPM_POO = ft.Column(
            spacing=30,
            controls=[
                ft.Row(
                    controls=[
                        ft.Text(
                            value="Загрузить ОПК ПОО",
                            size=24,
                            color=design.color["Nevada"]
                        )
                    ]
                ),
                ft.Row(
                    controls=[
                        self.text_fild_loder_file,
                        ft.IconButton(#кнопка згарузки файла
                            icon=ft.icons.DRIVE_FILE_MOVE_RTL_ROUNDED,
                            icon_color=design.color["Nevada"],
                            icon_size=40,
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=10),
                                overlay_color=design.color["Nevada Lite"]
                            ),
                            on_click=lambda _: self.file_picer.pick_files(
                                allow_multiple=False
                            ),
                        ),
                    ]
                ),
                ft.Row(
                    controls=[
                        self.drop_down_sheet
                    ]
                ),
                ft.Row(
                    alignment=ft.MainAxisAlignment.END,
                    controls=[
                        ft.TextButton(# кнопка запуска алгоритма 
                            icon=ft.icons.SAVE_AS_ROUNDED,
                            icon_color=design.color["Nevada"],
                            text="Загрузить",
                            style=ft.ButtonStyle(
                                icon_size=40,
                                overlay_color=design.color["Nevada Lite"],
                                color=design.color["Nevada"]
                            ),
                            on_click=self.go_to_load_FPM_POO
                        ),
                    ]
                ),
            ]
        )

        """
        главное пространство для интерактивных элементов
        """
        self.main_viwe=ft.Container(
            #expand=True,
            content=self.page_load_FPM_POO
        )
        
        """
        калонка с кнопками выгруза данных
        """
        self.column_upload_left = ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.TextButton(# кнопка для вкладки сохранить
                            icon=ft.icons.SAVE_AS_ROUNDED,
                            icon_color=design.color["Nevada"],
                            text="сохранить OPC_POO",
                            style=ft.ButtonStyle(
                                icon_size=32,
                                overlay_color=design.color["Nevada Lite"],
                                color=design.color["Nevada"]
                            ),
                            on_click=self.main_to_load_OPC_POO
                        ),
                    ]
                )
            ]
        )
        
        
        """
        калонка с кнопкаим загрузки данных
        """
        self.column_load_left = ft.Column(
            controls=[
                ft.Container(bgcolor="#000000",height=100,width=100)
            ]
        )
        
        """
        левая интерактивная часть какя кнопка активна для левой колонки 
        """
        self.interactiv_left_column=ft.Container(
            content=self.column_load_left
        )
        
        """
        колонка в левой части
        """
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
        
        """
        анимация открытия закрытия колонки
        """
        self.anim_swetcher=ft.Container(
            content=self.left_page_on
        )
        
        """
        весь дизайн который мы возвращаем 
        """
        self.main_page=ft.Row(
            expand=True,
            controls=[
                self.anim_swetcher,
                ft.Column(
                    expand=True,
                    controls=[
                        ft.Row(
                            expand=True,
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
                        self.main_viwe
                    ]
                ),
            ]
        )
        
    def file_picer_result(self,e):
        if e.files:
            self.text_fild_loder_file.value=e.files[0].path
            self.text_fild_loder_file.update()
            self.drop_down_sheet.options=self.read_sheet_file(e.files[0].path)
            self.drop_down_sheet.value=self.drop_down_sheet.options[0].key
            self.drop_down_sheet.update()
        else:
            "Cancelled!"
    
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
    
    def read_sheet_file(self,path):
        import openpyxl
        wb = openpyxl.load_workbook(path)
        data=[]
        for shet in wb.sheetnames:
            data.append(ft.dropdown.Option(str(shet)))
        return data
    
    def main_to_load_OPC_POO(self):
        self.main_viwe.content = self.page_load_FPM_POO
        self.main_viwe.update()
        
    def main_to_load_Employment(self):
        self.main_viwe.content = self.page_load_FPM_POO
        self.main_viwe.update()
    
    def go_to_load_FPM_POO(self,e):
        temp = craete_data_base_xlsx()
        temp.add_FPM_POO(path=str(self.text_fild_loder_file.value),sheet=self.drop_down_sheet.value)