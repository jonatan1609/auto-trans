from pyrogram import Client, Filters, Message, InlineKeyboardMarkup
from .detect_language import keyboard


@Client.on_message((Filters.command('start') & Filters.create(lambda _, m: len(m.command) > 1))
                   | Filters.command('changelang'))
async def select_language_by_link(_client: Client, message: Message):
    await message.reply("Choose your language:",
                        reply_markup=InlineKeyboardMarkup(keyboard[0]))
