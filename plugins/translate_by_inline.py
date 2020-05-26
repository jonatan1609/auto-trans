from pyrogram import InlineQuery, Client, InputTextMessageContent, InlineQueryResultArticle
from .detect_language import detect, translate
from .utils import get_native_language


@Client.on_inline_query()
async def translate_inline(_client: Client, query: InlineQuery):
    query_text = query.query
    language = await detect(query_text)
    native_language = get_native_language(query.from_user.id)
    if not native_language:
        return await query.answer(
            results=[],
            switch_pm_text="No selected language, press here.",
            switch_pm_parameter="cl"
        )
    translate_result = await translate(language, native_language, query_text)
    await query.answer(
        results=[
            InlineQueryResultArticle(
                title=f'Translated to {language}',
                description=translate_result[0],
                input_message_content=InputTextMessageContent(translate_result[0])
            )
        ]
    )
