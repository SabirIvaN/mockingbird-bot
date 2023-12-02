from aiogram import Bot, Dispatcher, types      # Importing Box, Dispatcher and types from aiogram
from config.telegram import TELEGRAM_BOT_TOKEN  # Importing a Telegram token from the Telegram configurator

bot = Bot(token = TELEGRAM_BOT_TOKEN)           # Connecting the application to the Telegram bot
dp = Dispatcher(bot)                            # Connecting to the Telegram bot dispatcher application

@dp.message_handler(commands = ["start"])       # Using the function when entering the start command
async def cmd_start(message: types.Message):
    await message.answer("Привет! Я бот-пересмешник! Напишите мне что-нибудь!")

@dp.message_handler(content_types = ["text"])   # Using the function when entering the text data type
async def handle_text(message: types.Message):
    await message.reply(message.text)