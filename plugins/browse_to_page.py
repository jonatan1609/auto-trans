from pyrogram import Client, CallbackQuery, Filters, InlineKeyboardMarkup
from .detect_language import keyboard


@Client.on_callback_query(Filters.create(lambda _, c: c.data.startswith('page')))
async def browse_to_page(_client: Client, callback: CallbackQuery):
    page = int(callback.data.split('|')[1])
    await callback.edit_message_reply_markup(InlineKeyboardMarkup(keyboard[page]))
