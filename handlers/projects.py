from aiogram import F, Router, types
from aiogram.filters import Command, callback_data

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, callback_query

from keyboards.projects import generate_projects_kb

router = Router()


@router.message(F.text == "Проекты «EGIRFoxSTUDIO»")
async def channels_command(message: types.Message):
    foxone_btn = InlineKeyboardButton(
        text="FoxOne",
        url="https://modrinth.com/modpack/fox-one"
    )


    row_first = [foxone_btn]
    rows = [row_first]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await message.answer(
        text="Проекты «EGIRFoxSTUDIO»:",
        reply_markup=markup,
    )





#PROJECTS = {
#    "FoxOne": {"text": "FoxOne", "description":"Сборка модов для Minecraft Java Edition", "img": "/sources/FoxOne.png"},
#
#}
#
#@router.callback_query(F.data == "projects")
#@router.message(F.text == "Проекты «EGIRFoxSTUDIO»")
#async def projects(update: types.Message | types.CallbackQuery):
# if isinstance(update, types.Message):
#    await update.answer(
#        "Проекты «EGIRFoxSTUDIO»:",
#        reply_markup=generate_projects_kb(PROJECTS),
#    )
# else:
#    await update.message.edit_text(
#        "Проекты «EGIRFoxSTUDIO»:",
#        reply_markup=generate_projects_kb(PROJECTS),
#    )
#
#@router.callback_query(F.data.startswith("category:"))
#async def category_info(callback: types.callback_query):
#    category_key = callback.data.split(":")[-1]
#    category = PROJECTS.get(category_key)
#
#
#    await callback.message.edit_text(
#        text=category["description"],
#        reply_markup=types.InlineKeyboardMarkup(
#            inline_keyboard=[
#                [InlineKeyboardButton(
#                    text="Назад",
#                    callback_data="projects"
#                    )
#                ],
#            ]
#        )
#    )

