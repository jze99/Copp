from typing import Callable, Any
import flet as ft

class design:
    color = {
            "White Rock":"#f0ece2",
            "Wafer":"#dfd3c3",
            "Rodeo Dust":"#c7b198",
            "Nevada":"#596e79",
            "Nevada Lite":"#7E93A0FF"
        }
        
class Text(ft.Text):
    def __init__(self, size:int=24, value:str=""):
        super().__init__(
            size=size,
            color=design.color["White Rock"],
            value=value
        )
        
class TextField(ft.TextField):
    def __init__(self, text_size:int=40, help_text:str=""):
        super().__init__(
            color=design.color["White Rock"],
            border_color=design.color["Nevada"],
            text_size=text_size,
            cursor_color=design.color["Nevada"],
            hint_text=help_text,
            text_style=ft.TextStyle(
                color=design.color["White Rock"]
            )
        )
        
class Button(ft.ElevatedButton):
    def __init__(self, text, meth, size:int=40):
        super().__init__(
            text=text,
            color=design.color["White Rock"],
            on_click=meth,
            style=ft.ButtonStyle(
                shadow_color=design.color["Nevada"],
                overlay_color=design.color["Nevada Lite"],
                bgcolor=design.color["Nevada"],
                text_style=ft.TextStyle(
                    size=size
                )
            )
        )

class text_button(ft.TextButton):
   
   def __init__(self, on_clic: Callable[[Any], None], icon:ft.Icon, size:int=40, text:str=""):
       super().__init__(
            on_click=on_clic,
            icon=icon,
            icon_color=design.color["Nevada"],
            text=text,
            style=ft.ButtonStyle(
                icon_size=size,
                shape=ft.RoundedRectangleBorder(radius=10),
                overlay_color=design.color["Nevada Lite"],
                color=design.color["Nevada"],
            ),
       )
   
class TextFieldFilePicer(ft.TextField):
    def __init__(self, value:str=""):
        super().__init__(
            expand=True,
            #width=500,
            dense=True,
            value=value,
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
        
class IconButton(ft.IconButton):
    def __init__(self, icon:ft.Icon, on_clic: Callable[[Any], None], size:int=40):
        super().__init__(
            icon=icon,
                icon_color=design.color["Nevada"],
                icon_size=size,
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=10),
                    overlay_color=design.color["Nevada Lite"]
                ),
                on_click=on_clic
            )
        
class DropDown(ft.Dropdown):
    def __init__(self):
        super().__init__(
            border_color=design.color["Nevada"],
            color=design.color["White Rock"],
            #height=100,
            #width=200,
        )

class logic_base():
    
    def read_sheet_file(self,path):
        import openpyxl
        wb = openpyxl.load_workbook(path)
        data=[]
        for shet in wb.sheetnames:
            data.append(ft.dropdown.Option(str(shet)))
        return data
    
    def file_picer_result_derictory(self,e):
        if e.path:
            self.text_file_picer.value=e.path
            self.text_file_picer.update()
    
    def file_picer_result(self,e):
        if e.files:
            self.text_file_picer.value=e.files[0].path
            self.text_file_picer.update()
            self.drop_down.options=self.read_sheet_file(e.files[0].path)
            self.drop_down.value=self.drop_down.options[0].key
            self.drop_down.update()
   
class time_picer(ft.TimePicker):
    def __init__(self):
        super().__init__(
            confirm_text="Confirm",
            error_invalid_text="Time out of range",
            help_text="Pick your time slot",

        )
   
class save_OPK_POO(ft.Column, logic_base):
    def __init__(self, text:str="", file_picer:ft.FilePicker=ft.FilePicker()):
        
        self.text_file_picer = TextFieldFilePicer()
        self.drop_down = DropDown()
        
        file_picer.on_result = self.file_picer_result
        
        super().__init__(
            expand=True,
            controls=[
                ft.Row(
                    expand=True,
                    controls=[
                        Text(value=text)
                    ]
                ),
                ft.Row(
                    expand=True,
                    controls=[
                        self.text_file_picer,
                        IconButton(
                            icon=ft.icons.TABLE_ROWS_ROUNDED,
                            size=40,
                            on_clic=lambda _: file_picer.pick_files(
                                allowed_extensions=["xlsx"],
                                file_type=ft.FilePickerFileType.CUSTOM,
                                allow_multiple=False,
                            ),
                        )
                    ]
                ),
                ft.Row(
                    controls=[
                        self.drop_down
                    ]
                ),
                ft.Row(
                    alignment=ft.MainAxisAlignment.END,
                    controls=[
                        text_button(
                            icon=ft.icons.NOT_STARTED_ROUNDED,
                            on_clic=self.logic,
                            text="Старт",
                        )
                    ]
                )
            ]
        )
        
    def logic(self,e):
        from work_xlsx.load_xlsx import craete_data_base_xlsx
        temp = craete_data_base_xlsx()
        temp.add_FPM_POO(path=str(self.text_file_picer.value),sheet=self.drop_down.value)
    
class save_Employment(ft.Column, logic_base):
    def __init__(self, text:str="", file_picer:ft.FilePicker=ft.FilePicker()):
        
        self.text_file_picer = TextFieldFilePicer()
        self.drop_down = DropDown()
        
        file_picer.on_result = self.file_picer_result
        
        super().__init__(
            expand=True,
            controls=[
                ft.Row(
                    expand=True,
                    controls=[
                        Text(value=text)
                    ]
                ),
                ft.Row(
                    expand=True,
                    controls=[
                        self.text_file_picer,
                        IconButton(
                            icon=ft.icons.TABLE_ROWS_ROUNDED,
                            size=40,
                            on_clic=lambda _: file_picer.pick_files(
                                allowed_extensions=["xlsx"],
                                file_type=ft.FilePickerFileType.CUSTOM,
                                allow_multiple=False,
                            ),
                        )
                    ]
                ),
                ft.Row(
                    controls=[
                        self.drop_down
                    ]
                ),
                ft.Row(
                    alignment=ft.MainAxisAlignment.END,
                    controls=[
                        text_button(
                            icon=ft.icons.NOT_STARTED_ROUNDED,
                            on_clic=self.logic,
                            text="Старт",
                        )
                    ]
                )
            ]
        )
        
    def logic(self,e):
        from work_xlsx.load_xlsx import craete_data_base_xlsx
        temp = craete_data_base_xlsx()
        temp.add_Employment(path=str(self.text_file_picer.value),sheet=self.drop_down.value)
        
class load_Employment(ft.Column, logic_base):
    def __init__(self, text:str="", file_picer_derictory:ft.FilePicker=ft.FilePicker()):
        
        self.text_file_picer = TextFieldFilePicer()
        #self.drop_down = DropDown()
        
        file_picer_derictory.on_result = self.file_picer_result_derictory
        
        super().__init__(
            expand=True,
            controls=[
                ft.Row(
                    expand=True,
                    controls=[
                        Text(value=text)
                    ]
                ),
                ft.Row(
                    expand=True,
                    controls=[
                        self.text_file_picer,
                        IconButton(
                            icon=ft.icons.TABLE_ROWS_ROUNDED,
                            size=40,
                            on_clic=lambda _: file_picer_derictory.get_directory_path()
                        )
                    ]
                ),
                ft.Row(
                    controls=[
                        time_picer()
                    ]
                ),
                ft.Row(
                    alignment=ft.MainAxisAlignment.END,
                    controls=[
                        text_button(
                            icon=ft.icons.NOT_STARTED_ROUNDED,
                            on_clic=self.logic,
                            text="Старт",
                        )
                    ]
                )
            ]
        )
        
    def logic(self,e):
        from work_xlsx.craeter_xlsx import create_xlsx_Employment
        temp = create_xlsx_Employment()
        temp.create_file(path=str(self.text_file_picer.value))

class load_OPK_POO(ft.Column, logic_base):
    def __init__(self, text:str="", file_picer_derictory:ft.FilePicker=ft.FilePicker()):
        
        self.text_file_picer = TextFieldFilePicer()
        #self.drop_down = DropDown()
        
        file_picer_derictory.on_result = self.file_picer_result_derictory
        
        super().__init__(
            expand=True,
            controls=[
                ft.Row(
                    expand=True,
                    controls=[
                        Text(value=text)
                    ]
                ),
                ft.Row(
                    expand=True,
                    controls=[
                        self.text_file_picer,
                        IconButton(
                            icon=ft.icons.TABLE_ROWS_ROUNDED,
                            size=40,
                            on_clic=lambda _: file_picer_derictory.get_directory_path()
                        )
                    ]
                ),
                ft.Row(
                    controls=[

                    ]
                ),
                ft.Row(
                    alignment=ft.MainAxisAlignment.END,
                    controls=[
                        text_button(
                            icon=ft.icons.NOT_STARTED_ROUNDED,
                            on_clic=self.logic,
                            text="Старт",
                        )
                    ]
                )
            ]
        )
        
    def logic(self,e):
        from work_xlsx.craeter_xlsx import create_xlsx_OPK_POO
        temp = create_xlsx_OPK_POO()
        temp.create_file(path=str(self.text_file_picer.value))
        
#on_hover: type[Callable[[Any], Any]]
#Имя: Remedy
#Идентификатор: robertrossmann.remedy
#Описание: A dark & bright theme with orange accents with roots in Base16 - Eighties colour theme
#Версия: 5.27.0
#Издатель: Robert Rossmann