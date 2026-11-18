
import asyncio
import os
from datetime import datetime
from zoneinfo import ZoneInfo

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
TIMEZONE = "Europe/Bratislava"

bot = Bot(token=TOKEN) if TOKEN else None
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "⚽ SPORT ANALYST AI 🎾\n\n"
        "Привет! Я твой спортивный аналитик.\n\n"
        "Мои направления:\n"
        "⚽ Футбол\n"
        "🎾 Теннис\n\n"
        "Я буду анализировать только события "
        "и рынки, доступные в TIPOS.\n\n"
        "Команды:\n"
        "/today — анализ на сегодня\n"
        "/football — футбол\n"
        "/tennis — теннис\n"
        "/value — поиск Value Bets\n"
        "/help — помощь\n\n"
        "Сейчас подключается аналитическая система."
    )


@dp.message(Command("help"))
async def help_command(message: Message):
    await message.answer(
        "SPORT ANALYST AI — помощь\n\n"
        "/start — главное меню\n"
        "/today — события на сегодня\n"
        "/football — футбольный анализ\n"
        "/tennis — теннисный анализ\n"
        "/value — поиск выгодных коэффициентов\n"
    )


@dp.message(Command("today"))
async def today(message: Message):
    now = datetime.now(ZoneInfo(TIMEZONE))
    await message.answer(
        f"📅 Сегодня: {now:%d.%m.%Y}\n\n"
        "Модуль получения линии TIPOS пока не подключён.\n"
        "Реальные прогнозы пока не формируются."
    )


@dp.message(Command("football"))
async def football(message: Message):
    await message.answer(
        "⚽ Футбольный модуль готовится.\n"
        "Анализ будет выполняться только для матчей TIPOS."
    )


@dp.message(Command("tennis"))
async def tennis(message: Message):
    await message.answer(
        "🎾 Теннисный модуль готовится.\n"
        "Анализ будет выполняться только для матчей TIPOS."
    )


@dp.message(Command("value"))
async def value(message: Message):
    await message.answer(
        "📊 Модуль Value Bets готовится.\n"
        "Пока реальные ставки не рекомендуются."
    )


async def main():
    if not TOKEN:
        raise RuntimeError("Не задан BOT_TOKEN")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
