import flet as ft
from constants import PATH
from components import (get_news_photo, get_label_for_news, get_description_for_news,
                        get_footer_news)


"""
Файл для отображения блока с новостями
"""

def get_block_news(page: ft.Page):
    return ft.Container(
        bgcolor=ft.colors.GREEN,
        adaptive=True,
        border_radius=15,
        content=ft.Column(
            controls=[
                get_news_photo(),
                get_label_for_news(),
                get_description_for_news(),
                get_footer_news()
            ],
        ),
        padding=10,
        height=300
    )