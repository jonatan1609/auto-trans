from configparser import ConfigParser
from xml.etree.ElementTree import parse
from pyrogram import InlineKeyboardButton
from aiohttp import ClientSession
import numpy

config = ConfigParser()
config.read('./config.ini')


async def detect(query: str) -> str:
    async with ClientSession() as session:
        async with session.get(
                "https://translate.yandex.net/api/v1.5/tr.json/detect",
                params={
                    'key': config['bot']['api_key'],
                    'text': query
                }
        ) as response:
            response = await response.json()
            try:
                return response['lang']
            except KeyError:
                return ''


async def translate(from_lang: str, to_lang: str, query: str) -> str:
    async with ClientSession() as session:
        async with session.get(
                "https://translate.yandex.net/api/v1.5/tr.json/translate",
                params={
                    'key': config['bot']['api_key'],
                    'text': query,
                    'lang': "{}-{}".format(from_lang, to_lang)
                }
        ) as response:
            text = await response.json()
            return text['text']


def _languages() -> list:
    xml = parse('languages.xml')
    return [
               x.text for x in xml.iter('string')
           ] + [  # noqa
               x.get('key') + '-' + x.get('value') for x in xml.iter('Item')
           ]


languages = _languages()


def create_buttons_keyboard():
    splitted_by_page = numpy.array_split(languages, 10)
    pages = [x.tolist() for x in splitted_by_page]
    keyboard = {}
    for p_num, i in enumerate(numpy.array_split(x, 7) for x in pages):
        page = []
        nums = iter(range(7))
        for j in i:
            num = next(nums)
            page.append([])
            for btn in j:
                page[num].append(InlineKeyboardButton(btn.replace('-', '_'), 'lang|' + btn.replace('-', '_'))) # noqa
        bottom = []
        if p_num != 9:
            bottom.append(InlineKeyboardButton('next page ->', 'page|' + str(p_num + 1)))
        if p_num != 0:
            bottom.insert(0, InlineKeyboardButton('<- previous page', 'page|' + str(p_num - 1))) # noqa
        page.append(bottom)
        keyboard[p_num] = page
    return keyboard


keyboard = create_buttons_keyboard()
