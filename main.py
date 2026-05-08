import flet as ft
from datetime import datetime 

def main_page(page: ft.Page):
    page.title = "my first app"
    page.theme_mode = ft.ThemeMode.DARK
    hello_text = ft.Text(value='Hello world')
    greeting_history = []
    history_text = ft.Text("История приветствий:")
    
    def on_button_click(_):
        # print(name_input.value)
        # pass
        name = name_input.value.strip()

        if name:
             # print(name)
            # hello_text = 'sdfsdfsdf'
            now = datetime.now()
            time_string = now.strftime("%Y:%m:%d - %H:%M:%S")
            hello_text.value = f"{time_string} - Привет, {name}!"
            hello_text.color = None
            name_input.value = None
            greeting_history.append(name) 
            print(greeting_history)
            history_text.value = f'ИСТОРИЯ ПРИВЕСТВИЙ \n' + ' \n - '.join(greeting_history)
        else:
            # print('Error')
            hello_text.value = 'ОШИБКА: Введите имя'
            hello_text.color = ft.Colors.RED
        page.update()

    def theme_switch(e):
        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
        else:
            page.theme_mode = ft.ThemeMode.DARK
        page.update()

    def clear_history():
        greeting_history.clear()
        history_text.value = " ИСТОРИЯ ПРИВЕТСТВИЙ"
        page.update()

    name_input = ft.TextField(label='Введите имя', on_submit=on_button_click)
    eleveated_button = ft.ElevatedButton('SEND', icon=ft.Icons.SEND,on_click=on_button_click)
    icon_button = ft.IconButton(icon=ft.Icons.BRIGHTNESS_6,on_click=theme_switch)
    clear_button = ft.IconButton(icon=ft.Icons.CLEAR,on_click=clear_history)
    page.add( hello_text,name_input,eleveated_button, icon_button,history_text,clear_button)

ft.app(target=main_page)
