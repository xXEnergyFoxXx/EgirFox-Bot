from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def main_menu_kb():
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Оффициальные кналы «Егерь Fox»")

             ],
            [
                KeyboardButton(text="Проекты «EGIRFoxSTUDIO»"),
                KeyboardButton(text="О студии «EGIRFoxSTUDIO»")
            ],
        ],
        resize_keyboard=True,
    )
