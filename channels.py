from aiogram import dispatcher, types

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup



@dp.message_handler(commands="Оффициальные кналы «Егерь Fox»", state="*")
async def inline_cb(message: types.Message):
    channels_kb = InlineKeyboardMarkup()
    channels_kb_2 = InlineKeyboardButton(text="Канал в Telegram", url="https://t.me/ZoneEgirGamer")
    channels_kb.add(channels_kb_2)
    await message.answer("Оффициальные кналы «Егерь Fox»:", reply_markup=channels_kb)






#def generate_channels_kb(channels):
#    keyboard = InlineKeyboardMarkup(inline_keyboard=[])
#
#    for channels_cb, channels in channels.items():
#        keyboard.inline_keyboard.append(
#            [
#                InlineKeyboardButton(
#                    text=channels["text"],
#                    callback_data=f"channels:{channels_cb}"
#                )
#             ]
#        )
#
#    return keyboard
