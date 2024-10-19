from flet import View
from designer import design
from pages.authorization import authorization
from application.pages.main_page import main_page

def ViewsHendler(page):
    return{
        "/login":View(
            route="/login",
            controls=[
                authorization(page=page).return_page()
            ],
            bgcolor=design.color["Rodeo Dust"],
            scroll=True,
        ),
        "/main":View(
            route="/main",
            controls=[
                main_page(page=page).return_page(),
            ],
            bgcolor=design.color["Rodeo Dust"],
            scroll=True,
        ),
        
    }