from aiogram import Bot, Dispatcher
import asyncio
import logging

from config import API_TOKEN
from handlers import router
import utils
import send


async def main():
    words = utils.extract_words_from_pdf('words_dictionary.pdf')

    bot = Bot(token=API_TOKEN)
    dp = Dispatcher()
    dp.include_router(router)

    logging.basicConfig(level=logging.INFO)

    asyncio.create_task(send.send_random_words(bot, words))
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
