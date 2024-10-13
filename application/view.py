from flet import View
from designer import design
from pages.authorization import authorization
from pages.main_page import main_page
from pages.test_page import test_page
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
        "/test":View(
            route="/test",
            controls=[
                test_page(page=page).return_page(),
            ],
            bgcolor=design.color["Rodeo Dust"],
            scroll=True,
        ),
    }