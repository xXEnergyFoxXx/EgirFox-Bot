from aiogram import Router, types
from aiogram.filters import Command

from keyboards.menu import main_menu_kb


router = Router()

@router.message(Command("start"))
async def start_bot(message: types.Message):
    await message.answer(
        f"Привет, {message.from_user.full_name} \nЯ бот, созданный для информирования о новых видео канала «Егерь Fox», а также проектах студии «EGIRFoxSTUDIO». Выбери нужное меню снизу:",
        reply_markup=main_menu_kb()
    )
