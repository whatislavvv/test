import flet as ft
from datetime import datetime 

def main_page(page: ft.Page):
    page.title = "my first app"
    page.theme_mode = ft.ThemeMode.DARK
    hello_text = ft.Text(value='Hello world')
    greeting_history = []
    favorites = []     # для задания 2  
    time_dictionary = []   # для задания 3
    history_text = ft.Text("История приветствий:")
    favorites_text = ft.Text("Любимые имена: ") 

    def on_button_click(_):
        name = name_input.value.strip()
        if name:
            now = datetime.now()
            time_string = now.strftime("%Y:%m:%d - %H:%M:%S")
            hello_text.value = f"{time_string} - Привет, {name}!"
            hello_text.color = None
            name_input.value = None
            greeting_history.append(name) 
            time_dictionary.append({"text": hello_text.value, "hour": now.hour}) #задание 3
            history_text.value = f'ИСТОРИЯ ПРИВЕСТВИЙ \n' + ' \n - '.join(greeting_history)

        else:
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
        time_dictionary.clear()
        favorites.clear()
        history_text.value = " ИСТОРИЯ ПРИВЕТСТВИЙ"
        favorites_text.value = "Любимые имена: "
        page.update()

    #  функция для добавления любимых имён
    def add_to_favorites(_):
        if greeting_history:
            last_name = greeting_history[-1]
            if last_name not in favorites:
                favorites.append(last_name)
                favorites_text.value = 'ЛЮБИМЫЕ ИМЕНА \n' + ' \n - '.join(favorites)
                page.update()

    # функции с фильтрацией до 12:00(утро) и после 12:00(решил что будет вечер)
    def filter_morning(_):
        morning = [item["text"] for item in time_dictionary if item["hour"] < 12]
        history_text.value = "УТРЕННИЕ ПРИВЕТСТВИЯ:\n" + "\n".join(morning)
        page.update()
    def filter_evening(_):
        evening = [item["text"] for item in time_dictionary if item["hour"] >= 12]
        history_text.value = "ВЕЧЕРНИЕ ПРИВЕТСТВИЯ:\n" + "\n".join(evening)
        page.update()

    def show_all_history(_):
        history_text.value = f'ИСТОРИЯ ПРИВЕСТВИЙ \n' + ' \n - '.join(greeting_history)
        page.update()

    name_input = ft.TextField(label='Введите имя', on_submit=on_button_click)
    eleveated_button = ft.ElevatedButton('SEND', icon=ft.Icons.SEND, on_click=on_button_click)
    icon_button = ft.IconButton(icon=ft.Icons.BRIGHTNESS_6, on_click=theme_switch)
    clear_button = ft.IconButton(icon=ft.Icons.CLEAR, on_click=clear_history)
    fav_button = ft.ElevatedButton("В избранное", icon=ft.Icons.FAVORITE, on_click=add_to_favorites)
    morning_button = ft.TextButton("Утро (<12:00)", on_click=filter_morning)
    evening_button = ft.TextButton("Вечер (>12:00)", on_click=filter_evening)
    all_button = ft.TextButton("Все", on_click=show_all_history)
    page.add(hello_text, name_input, eleveated_button, icon_button, clear_button, fav_button, favorites_text, morning_button, evening_button, all_button, history_text) 
ft.app(target=main_page)