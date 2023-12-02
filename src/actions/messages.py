from aiogram import Bot, Dispatcher, types      # importing Box, Dispatcher and types from aiogram
from config.telegram import TELEGRAM_BOT_TOKEN  # importing a Telegram token from the Telegram configurator

bot = Bot(token = TELEGRAM_BOT_TOKEN)           # connecting the application to the Telegram bot
dp = Dispatcher(bot)                            # connecting to the Telegram bot dispatcher application

# Telegram Bot Launch Command
@dp.message_handler(commands = ["start"])
async def cmd_start(message: types.Message):
    await message.answer("Привет! Я бот-пересмешник! Напишите мне что-нибудь!")

# The command to respond to the text
@dp.message_handler(content_types = ["text"])
async def handle_text(message: types.Message):
    await message.reply(message.text)