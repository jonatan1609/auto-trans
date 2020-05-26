from pyrogram import Client, CallbackQuery, Filters
from .utils import change_language, exist_in_db, add_to_db


@Client.on_callback_query(Filters.create(lambda _, c: c.data.startswith('lang')))
async def select_language(_client: Client, callback: CallbackQuery):
    language = callback.data.split('|')[1].split('_')[0]
    if not exist_in_db(callback.from_user.id):
        add_to_db(callback.from_user.id)
    change_language(callback.from_user.id, language)
    await callback.edit_message_text('Success! now you can translate!')
