from pyrogram import Client, Message, Filters
from .detect_language import detect, translate
from .utils import get_native_language


@Client.on_message(Filters.private & Filters.text)
async def translate_in_private(_client: Client, message: Message):
    language = await detect(message.text)
    native_language = get_native_language(message.from_user.id)
    if not native_language:
        return await message.reply("You didn't choose the language"
                                   " that you want to translate to!\n"
                                   f"[press here to choose]"
                                   f"(t.me/{(await _client.get_me()).username}?start=cl)")
    result = await translate(language, native_language, message.text)
    await message.reply(result[0])
