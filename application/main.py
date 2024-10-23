import flet as ft
from view import ViewsHendler

def main(page: ft.Page):
    page.title = "COPP"
        
    def PageLoading(route):
        print(page.route)
        page.views.clear()
        page.views.append(ViewsHendler(page=page)[page.route])
        page.update()
    page.on_route_change = PageLoading
    page.go("/login")
    
ft.app(target=main, assets_dir="assets")