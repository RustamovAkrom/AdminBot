import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.client.session.aiohttp import AiohttpSession
from bot.handlers import start, help, send_admin_group
from bot.config import settings
from keep_alive import keep_alive


keep_alive()

# Initialize sesions proxy
session = AiohttpSession(proxy="http://proxy.server:3128")

# Initialize bot and dispatcher
bot = Bot(token = settings.BOT_TOKEN, session = session)
dp = Dispatcher()  


# Registrations routers
dp.include_routers(send_admin_group.router)

# Registerion handlers
dp.message.register(help.send_help, Command(commands=settings.HELP))
dp.message.register(start.start_command, Command(commands=settings.START))


async def main() -> None:
    """Starting bot...
    """

    try:
        await dp.start_polling(bot)

    except Exception as _ex:
        print(f"There is an exception - {_ex}")


if __name__=='__main__':
    
    if settings.DEBUG:
        # Configure logging
        logging.basicConfig(level=logging.INFO)

    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")
