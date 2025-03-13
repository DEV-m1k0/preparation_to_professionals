import flet as ft
from components import get_container_with_navigate_btns
from news import get_block_news


"""
Файл для запуска мобильного приложения
"""


def main(page: ft.Page):
    page.adaptive = True
    page.bgcolor = ft.colors.GREEN_900

    body = ft.Container(
        content=ft.Column(
            controls=[
                get_container_with_navigate_btns(),
                get_block_news(page=page)
            ]
        )
    )
    
    

    page.add(
        body
    )


ft.app(main)

