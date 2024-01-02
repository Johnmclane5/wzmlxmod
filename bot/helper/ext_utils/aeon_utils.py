from pyshorteners import Shortener
from bot import LOGGER
from re import IGNORECASE, search, escape

from bot.helper.ext_utils.text_utils import nsfw_keywords

def tinyfy(long_url):
    s = Shortener()
    try:
        short_url = s.tinyurl.short(long_url)
        LOGGER.info(f'tinyfied {long_url} to {short_url}')
        return short_url
    except Exception:
        LOGGER.error(f'Failed to shorten URL: {long_url}')
        return long_url
