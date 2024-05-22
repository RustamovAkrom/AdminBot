from aiogram import types
from bot.config.settings import START_TEXT

async def start_command(message: types.Message) -> None:
    await message.reply(START_TEXT(message.from_user.first_name))
    