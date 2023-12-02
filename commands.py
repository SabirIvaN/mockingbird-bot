from aiogram import types
from config.telegram import dp

@dp.message_handler(commands = ["start"])
async def cmd_start(message: types.Message):
    await message.answer("Привет! Я бот-пересмешник! Напишите мне что-нибудь!")

@dp.message_handler(content_types = ["text"])
async def handle_text(message: types.Message):
    text = message.text
    
    await message.reply(text)
    