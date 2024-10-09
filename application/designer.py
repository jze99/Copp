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

#Имя: Remedy
#Идентификатор: robertrossmann.remedy
#Описание: A dark & bright theme with orange accents with roots in Base16 - Eighties colour theme
#Версия: 5.27.0
#Издатель: Robert Rossmann