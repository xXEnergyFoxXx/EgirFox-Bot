from aiogram import F, Router, types
from aiogram.filters import Command

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

router = Router()



@router.message(F.text == "Оффициальные кналы «Егерь Fox»")
async def channels_command(message: types.Message):
    telegram_btn = InlineKeyboardButton(
        text="📣Канал в Telegram",
        url="https://t.me/ZoneEgirGamer",
    )
    vk_video_btn = InlineKeyboardButton(
        text="Канал в ВК Видео",
        url="https://vkvideo.ru/@egirgamer"
    )
    youtube_btn = InlineKeyboardButton(
        text="Канал на YouTube",
        url="https://www.youtube.com/@egirgamer",
    )
    dzen_btn = InlineKeyboardButton(
        text="Канал в Дзен",
        url="https://dzen.ru/egir_fox"
    )


    row_first = [telegram_btn, vk_video_btn]
    row_second = [dzen_btn, youtube_btn]
    rows = [row_first, row_second]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await message.answer(
        text="Соцсети «Егерь Fox»:",
        reply_markup=markup,
    )






#@router.message_handler(commands="Оффициальные кналы «Егерь Fox»", state="*")
#async def inline_cb(message: types.Message):
#    channels_kb = InlineKeyboardMarkup()
#    channels_kb_2 = InlineKeyboardButton(text="Канал в Telegram", url="https://t.me/ZoneEgirGamer")
#    channels_kb.add(channels_kb_2)
#    await message.answer("Оффициальные кналы «Егерь Fox»:", reply_markup=channels_kb)
#



#CHANNELS = {
#    "telegram": {"text": "Канал в Telegram", "description": "Вы открыли канал в Telegram", "url": "https://t.me/ZoneEgirGamer"},
#    "vk_video": {"text": "Канал в ВК Видео", "description": "Вы открыли канал в ВК Видео"},
#    "youtube": {"text": "Канал на YouTube", "description": "Вы отрыли канал на YouTube"},
#    "dzen": {"text": "Канал в Дзен", "description": "Вы открыли канал в дзен"},
#}
#
#
#@router.callback_query(F.data == "channels")
#@router.message(F.text == "Оффициальные кналы «Егерь Fox»")
#async def channels(update: types.Message | types.CallbackQuery):
#    if isinstance(update, types.Message):
#        await update.answer(
#            "Оффициальные кналы «Егерь Fox»:",
#            reply_markup=generate_channels_kb(CHANNELS)
#        )
#
#    else:
#        await update.message.edit_text(
#            "Оффициальные кналы «Егерь Fox»:",
#            reply_markup=generate_channels_kb(CHANNELS)
#        )
#
#@router.callback_query(F.data.startswich("channels:"))
#async def channels_info(callback: types.CallbackQuery):
#    channels_key = callback.data.split(":")[-1]
#    channels = CHANNELS.get(channels_key)
#
#    await callback.message.edit_text(
#        text=channels["description"],
#        reply_markup=types.InlineKeyboardMarkup(
#            inline_keyboard=[
#                [
#                    types.InlineKeyboardButton(
#                        text="Назад",
#                        callback_data="channels",
#                        url=channels["url"]
#
#                    )
#                 ]
#            ]
#        )
#    )
#