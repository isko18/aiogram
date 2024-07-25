from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import Message
from aiogram.dispatcher.storage import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import BotCommand

from config import token
from database import Database
import logging

bot = Bot(token=token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
db = Database('sql.db')
db.create_table()
logging.basicConfig(level=logging.INFO)

class Form(StatesGroup):
    username = State() 

@dp.message_handler(commands='start')
async def start(message:Message):
    await Form.username.set()
    await message.reply("Привет! Как тебя зовут ?")
    
@dp.message_handler(state=Form.username)
async def process_username(message:Message, state: FSMContext):
    username = message.text
    db.add_user(message.from_user.id, username)
    await state.finish()
    await message.reply(f'Приятно познакомиться, {username}')
    
@dp.message_handler(commands='me')
async def get_me(message:Message):
    user = db.get_user(message.from_user.id)
    if user:
        await message.reply(f'Ты зарегистрирован как {user[2]}')
    else:
        await message.reply("Ты еще не зарегистрирован")
    
async def on_startup(dp):
    await bot.set_my_commands([
        BotCommand(command='/start', description='Start bot'),
        BotCommand(command='/me', description='Info me')
    ])
    logging.info("Настройки базы данных")
    db.create_table()
    logging.info("База загружена")
    
executor.start_polling(dp, on_startup=on_startup, skip_updates=True)


