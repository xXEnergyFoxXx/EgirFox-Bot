from aiogram import Router, types, F
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton

router = Router()


@router.message(F.text == "О студии «EGIRFoxSTUDIO»")
async def info(message: types.Message):

    projects_kb = InlineKeyboardButton(text="Оффициальные кналы «Егерь Fox»", callback_data="projects_kb")




    await message.answer(
        f"Студия «EGIRFoxSTUDIO» была открыта в 2024 году \n и имеет два проекта, а именно: \n (FoxOne) FoxOne — это сборка модов для Minecraft Java Edition версии 1.20.1, направленная на увлекательный геймплей; \n (Егерь Fox - Бот) — Telegram-бот-информатор о блогерской деятельности канала Егерь Fox, а также проектах студии EGIRFoxSTUDIO.",

    )


@router.callback_query_handler(text="projects_kb", state="*")
async def projects(call: CallbackQuery):
    await call.message.answer()
