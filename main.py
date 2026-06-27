import asyncio

from aiogram.types import Message
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command


BOT_TOKEN = "" 

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()       # обработчик входящих обновлений


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        f'Привет {message.from_user.first_name}! Я твой первый бот.'
        )
    print(f"Пользователь {message.from_user.full_name} отправил {message.text} в {message.date}")


@dp.message(Command('жардам'))
async def cmd_help(message: Message):
    await message.answer(
        '/start - приветствие\n'
        '/help - список команд'
    )

async def main():
    await dp.start_polling(bot)     # отправляет запросы на тг-сервер


if __name__ == "__main__":
    asyncio.run(main())     # для запуска асинк функции
