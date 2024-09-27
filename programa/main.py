from flet import *
from modulos import Inicio, PageFish, PageShop

ANCHO_PAGINA = 1300
ALTO_PAGINA = 900


def main(page: Page):
    page.title = "Kmeans by Marcos"
    page.window.width = ANCHO_PAGINA
    page.window.height = ALTO_PAGINA
    page.padding = 0
    page.window.resizable = False
    page.window.maximizable = False
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    page.vertical_alignment = MainAxisAlignment.CENTER


    def router(route):
        page.views.clear()
        if page.route == "/Inicio":
            Show = Inicio(page)
            page.views.append(Show)
        elif page.route == "/Fish":
            Show = PageFish(page)
            page.views.append(Show)
        elif page.route == "/Shop":
            Show = PageShop(page)
            page.views.append(Show)
        

        page.update()

    page.on_route_change = router
    page.go("/Inicio")


if __name__ == "__main__":
    app(target=main)

