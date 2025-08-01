import asyncio
import logging
from config.config import load_config, Config
from handlers import handler

from aiogram import Dispatcher, Bot, Router
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import BotCommand


async def set_commands_telegram(bot: Bot):

    main_menu_commands = [BotCommand(
        command='/start', description='запуск бота')]

    await bot.set_my_commands(main_menu_commands)


async def main():
    config: Config = load_config(
        'C:\\Users\\Амир\\Desktop\\python работы\\bot rock scissors paper\\.env')
    logger = logging.getLogger(__name__)
    logging.basicConfig(
        format=config.log.format, level=config.log.level
    )

    logger.info('Bot is Starting...')
    token = config.bot.token

    dp = Dispatcher()
    dp.startup.register(set_commands_telegram)
    bot = Bot(token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    dp.include_router(handler.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
