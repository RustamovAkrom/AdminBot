from aiogram import types, Router
from aiogram.filters.command import Command
from bot.config.settings import START, HELP, SEND_ME

TEXT_HELP = f"""
\t
\n/{ " ".join(START) } - boshlash.
\n/{ " ".join(SEND_ME) } - habar, murojat qoldirish.
\n/{ " ".join(HELP) } - buyruqlar
\t
"""

async def send_help(message: types.Message):
    await message.answer(TEXT_HELP)