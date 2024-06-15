import flet as ft
import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))

sys.path.insert(0, parent_dir)

from db.orm import Orm


orm = Orm()

def main(page: ft.Page):
    page.title = 'Админ-панель'
    page.theme_mode = 'dark'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    brand_name = ft.TextField(label='Введите название бренда', width=300, focused_border_color='#015900', cursor_color='#015900')
    model_name = ft.TextField(label='Введите модель бренда', width=300, focused_border_color='#015900', cursor_color='#015900')
    item = ft.TextField(label='Введите какая это вещь', width=300, focused_border_color='#015900', cursor_color='#015900')
    price = ft.TextField(label='Введите цену в долларах', width=300, focused_border_color='#015900', cursor_color='#015900')
    sizes = ft.TextField(label='Введите размеры вещи через кому', width=300, focused_border_color='#015900', cursor_color='#015900')

    def route_change(e: ft.RouteChangeEvent):
        page.views.clear()
        if page.route == '/add_brand':
            page.views.append(
                ft.View(
                    '/add_brand',
                    [
                        ft.AppBar(title=ft.Text('Добавить бренд'), bgcolor='#034701', center_title=True, color='black'),
                        ft.Column(
                            [
                                
                                brand_name,
                                ft.Row(
                                    [
                                        ft.ElevatedButton('Добавить', bgcolor='#015900', color='black', on_click=add_brand),
                                        ft.ElevatedButton('Отмена', on_click=lambda e: page.go('/'), bgcolor='#015900',color='black')
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER
                                )
                            ],
                            alignment=ft.MainAxisAlignment.CENTER
                        )
                    ]
                )
            )
        elif page.route == '/delete_brand':
            page.views.append(
                ft.View(
                    '/delete_brand',
                    [
                        ft.AppBar(title=ft.Text('Удалить бренд'), bgcolor='#034701', center_title=True, color='black'),
                        ft.Text('Here you can delete a brand.'),
                    ],
                )
            )
        elif page.route == '/add_item':
            page.views.append(
                ft.View(
                    '/add_item',
                    [
                        ft.AppBar(title=ft.Text('Добавить новую вещь'), bgcolor='#034701', center_title=True, color='black'),
                        ft.Column(
                            [
                                brand_name,
                                model_name,
                                item,
                                price,
                                sizes,
                                ft.Row(
                                    [
                                        ft.ElevatedButton('Добавить', on_click=add_item, bgcolor='#015900',color='black'),
                                        ft.ElevatedButton('Отмена', on_click=lambda e: page.go('/'), bgcolor='#015900',color='black')
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER
                                )
                            ],
                            alignment=ft.MainAxisAlignment.CENTER
                        )
                    ],
                )
            )
        elif page.route == '/':
            page.views.append(
                ft.View(
                    '/',
                    [
                        ft.AppBar(title=ft.Text('Главная страница'), bgcolor='#034701', center_title=True, color='black'),
                        ft.Column(
                            [
                                ft.Row(
                                    [
                                        ft.ElevatedButton('Добавить бренд', on_click=add_brand_route, bgcolor='#015900',color='black'),
                                        ft.ElevatedButton('Удалить бренд', on_click=delete_brand_route, bgcolor='#015900',color='black'),
                                        ft.ElevatedButton('Добавить новую вещь', on_click=add_item_route, bgcolor='#015900',color='black'),
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER
                                ),
                                ft.Row(
                                    [
                                        ft.IconButton(ft.icons.SUNNY, on_click=change_theme, icon_color='yellow'),
                                        ft.Text('Тема'),
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER
                                ),
                            ]
                        )
                    ]
                )
            )
            
        page.update()

    def change_theme(e):
        page.theme_mode = 'light' if page.theme_mode == 'dark' else 'dark'
        page.update()

    def add_brand_route(e):
        page.go('/add_brand')
    
    def main_page_route(e):
        page.go('/')
    
    def delete_brand_route(e):
        page.go('/delete_brand')

    def add_item_route(e):
        page.go('/add_item')
    
    def add_item(e):
        orm.add_item(item.value, brand_name.value, model_name.value, sizes.value, 'asd', price.value)
        brand_name.value = ''
        item.value = ''
        model_name.value = ''
        sizes.value = ''
        price.value = ''
        main_page_route(e)
    
    def add_brand(e):
        orm.add_brand(brand_name.value)
        brand_name.value = ''
        main_page_route(e)

    page.on_route_change = route_change

    page.go('/')

ft.app(target=main, view=ft.WEB_BROWSER, port=8000)