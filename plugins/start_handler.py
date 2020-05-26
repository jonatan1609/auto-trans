from pyrogram import Client, Filters, Message, InlineKeyboardMarkup
from .utils import exist_in_db, add_to_db
from .detect_language import keyboard


@Client.on_message(Filters.private & Filters.command('start'))
async def start_handler(_client: Client, message: Message):
    if exist_in_db(message.from_user.id):
        await message.reply(
            "Welcome, \ni can translate messages into your language!\n"
        )
    else:
        await message.reply(
            "What's your native language? [The one that you want translate to?]",
            reply_markup=InlineKeyboardMarkup(keyboard[0])
        )
        add_to_db(message.from_user.id)
