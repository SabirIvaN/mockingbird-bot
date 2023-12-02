from aiogram import Bot, Dispatcher, types
from telegram import TELEGRAM_BOT_TOKEN

bot = Bot(token = TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands = ["start"])
async def cmd_start(message: types.Message):
    await message.answer("Привет! Я бот-пересмешник! Напишите мне что-нибудь!")

@dp.message_handler(content_types = ["text"])
async def handle_text(message: types.Message):
    text = message.text
    
    await message.reply(text)