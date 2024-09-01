from datetime import datetime, timedelta
from aiogram.types import FSInputFile
from gtts import gTTS
import asyncio
import random
import shutil
import os

from config import ADMIN_ID as IDs


async def send_random_words(bot, words):
    while True:
        now = datetime.now()
        next_run = now + timedelta(minutes=random.randint(18*60, 30*60))

        if not (7 <= now.hour <= 22):
            await asyncio.sleep(600)
            continue

        random_words = random.sample(words, 5)

        for ADMIN_ID in IDs:
            await bot.send_message(ADMIN_ID, "НОВЫЕ 5 СЛОВ:")

            for i, (word, transcription, translation) in enumerate(random_words):
                message = f"{i+1}. {word} {transcription} - {translation}"
                await bot.send_message(ADMIN_ID, message)

                filename = await save_tts(word, lang='en')
                voice = FSInputFile(filename)
                await bot.send_voice(ADMIN_ID, voice)
            shutil.rmtree('temp')
            os.makedirs('temp')
        await asyncio.sleep((next_run - now).total_seconds())


async def save_tts(text, lang='en'):
    tts = gTTS(text=text, lang=lang)

    filename = f'temp/{str(random.randint(0, 100000))}.mp3'
    tts.save(filename)

    return filename
