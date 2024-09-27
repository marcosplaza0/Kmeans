from flet import *
from modulos.texts import PAGE1_TEXT, PAGEFISH_TEXT, PAGEFISH2_TEXT, PAGESHOP_TEXT, PAGESHOP2_TEXT
from modulos.fish import fish_canva
from modulos.shop import shop_canva

class Menu_drawer(NavigationDrawer):
    def __init__(self, view):
        super().__init__()
        self.view = view
        self.on_change = lambda e: self.cambiar_pagina(e)
        self.controls = [
            Container(height=12),
            NavigationDrawerDestination(
                label="Inicio",
                icon=icons.DOOR_BACK_DOOR_OUTLINED,
                selected_icon_content=Icon(icons.DOOR_BACK_DOOR),
            ),
            Container(height=12),
            Container(height=2, bgcolor=colors.BLACK),
            Container(height=12),
            NavigationDrawerDestination(
                label="Peces",
                icon=icons.FLOOD,
                selected_icon_content=Icon(icons.FLOOD_OUTLINED),
            ),
            Container(height=12),
            NavigationDrawerDestination(
                label="Shop",
                icon=icons.PERSON_OUTLINED,
                selected_icon_content=Icon(icons.PERSON),
            ),
        ]

    def cambiar_pagina(self, e):
        index = e.control.selected_index
        if index == 0:
            self.view.page.go("/Inicio")
        elif index == 1:
            self.view.page.go("/Fish")
        elif index == 2:
            self.view.page.go("/Shop")

    def show_drawer(self, e):
        self.view.drawer.open = True
        self.view.update()



class Header(Container):
    def __init__(self, titulo, function):
        super().__init__()
        self.vertical_alignment = CrossAxisAlignment.CENTER
        self.padding = padding.only(top=10, bottom=12)
        self.margin = margin.only(bottom=10)
        self.bgcolor = colors.GREY_200
        self.shadow = BoxShadow(
            spread_radius=1,
            blur_radius=15,
            color=colors.BLUE_GREY_300,
            offset=Offset(0, 0),
            blur_style=ShadowBlurStyle.OUTER,
        )
        self.content = Row(
            [
                Container(width=12),
                IconButton(
                    icons.MENU,
                    on_click=lambda e: function(e),
                ),
                Text(
                    "  " + titulo,
                    color=colors.BLACK,
                    size=30,
                    weight=FontWeight.BOLD,
                ),
            ]
        )



class Inicio(View):
    def __init__(self, pg):
        super(Inicio, self).__init__(
            route="/Inicio",
            horizontal_alignment=CrossAxisAlignment.CENTER,
            vertical_alignment=MainAxisAlignment.CENTER,
            padding=0,
        )
        self.drawer: NavigationDrawer = Menu_drawer(self)
        self.page: Page = pg
        self.controls = [
            Container(
                bgcolor=colors.WHITE,
                margin=0,
                height=self.page.window.height,
                content=Column(
                    scroll= ScrollMode.AUTO,
                    controls=[
                        Header("Inicio", self.drawer.show_drawer),
                        Container(
                            padding = padding.only(30,20,30,60),
                            content =Column(
                                scroll= ScrollMode.AUTO,
                                controls= [
                                    Text("Bienvenido a la aplicación de Kmeans!!!", size=40, weight=FontWeight.BOLD),
                                    Divider(height=10,opacity=0.5),
                                    Markdown(
                                        PAGE1_TEXT,
                                        selectable=True,
                                        extension_set=MarkdownExtensionSet.GITHUB_WEB,
                                        on_tap_link=lambda e: self.page.launch_url(e.data),
                                    ),
                                    Row(
                                        [
                                            Image(
                                                src=f"../resources/images/Tabla_peces.png",
                                                width=500,
                                                height=500,
                                                fit=ImageFit.CONTAIN,
                                            ),
                                            Image(
                                                src=f"../resources/images/Tabla_shop.png",
                                                width=500,
                                                height=500,
                                                fit=ImageFit.CONTAIN,
                                            ),
                                        ]
                                    )
                                ],
                            ),
                        )
                    ],
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                ),
            )
        ]




class PageFish(View):
    def __init__(self, pg):
        super(PageFish, self).__init__(
            route="/Fish",
            horizontal_alignment=CrossAxisAlignment.CENTER,
            vertical_alignment=MainAxisAlignment.CENTER,
            padding=0,
        )
        self.drawer: NavigationDrawer = Menu_drawer(self)
        self.page: Page = pg
        self.controls = [
            Container(
                bgcolor=colors.WHITE,
                margin=0,
                height=self.page.window.height,
                content=Column(
                    scroll= ScrollMode.AUTO,
                    controls=[
                        Header("Fish", self.drawer.show_drawer),
                        Container(
                            padding = padding.only(30,20,30,60),
                            content =Column(
                                scroll= ScrollMode.AUTO,
                                controls= [
                                    Text("Aplicacion de Kmeans para juntar peces", size=40, weight=FontWeight.BOLD),
                                    Divider(height=10,opacity=0.5),
                                    Markdown(
                                        PAGEFISH_TEXT,
                                        selectable=True,
                                        extension_set=MarkdownExtensionSet.GITHUB_WEB,
                                        on_tap_link=lambda e: self.page.launch_url(e.data),
                                    ),
                                    Divider(height=20,opacity=0.5),
                                    fish_canva,
                                    Markdown(
                                        PAGEFISH2_TEXT,
                                        selectable=True,
                                        extension_set=MarkdownExtensionSet.GITHUB_WEB,
                                        on_tap_link=lambda e: self.page.launch_url(e.data),
                                    ),
                                ],
                            ),
                        )
                    ],
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                ),
            )
        ]



class PageShop(View):
    def __init__(self, pg):
        super(PageShop, self).__init__(
            route="/Shop",
            horizontal_alignment=CrossAxisAlignment.CENTER,
            vertical_alignment=MainAxisAlignment.CENTER,
            padding=0,
        )
        self.drawer: NavigationDrawer = Menu_drawer(self)
        self.page: Page = pg
        self.controls = [
            Container(
                bgcolor=colors.WHITE,
                margin=0,
                height=self.page.window.height,
                content=Column(
                    scroll= ScrollMode.AUTO,
                    controls=[
                        Header("Shop", self.drawer.show_drawer),
                        Container(
                            padding = padding.only(30,20,30,60),
                            content =Column(
                                scroll= ScrollMode.AUTO,
                                controls= [
                                    Text("Aplicacion de Kmeans para una tienda", size=40, weight=FontWeight.BOLD),
                                    Divider(height=10,opacity=0.5),
                                    Markdown(
                                        PAGESHOP_TEXT,
                                        selectable=True,
                                        extension_set=MarkdownExtensionSet.GITHUB_WEB,
                                        on_tap_link=lambda e: self.page.launch_url(e.data),
                                    ),
                                    Divider(height=20,opacity=0.5),
                                    shop_canva,
                                    Markdown(
                                        PAGESHOP2_TEXT,
                                        selectable=True,
                                        extension_set=MarkdownExtensionSet.GITHUB_WEB,
                                        on_tap_link=lambda e: self.page.launch_url(e.data),
                                    ),
                                ],
                            ),
                        )
                    ],
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                ),
            )
        ]
