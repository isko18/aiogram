from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import Message
from config import token
import sqlite3, time, logging

from aiogram.dispatcher.storage import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot = Bot(token=token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
logging.basicConfig(level=logging.INFO)

ADMIN_ID = 1649228320

connection = sqlite3.connect('users.db')
cursor = connection.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS users(
    id INT ,
    firs_name VARCHAR(100),
    last_name VARCHAR(100),
    username VARCHAR(100),
    created VARCHAR(100)
);   
""")

@dp.message_handler(commands='start')
async def start(message:Message):
    cursor.execute(f'SELECT id FROM users WHERE id = {message.from_user.id};')
    users_result = cursor.fetchall()
    print(users_result)
    if users_result == []:
        cursor.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?); ",
                    (message.from_user.id, message.from_user.first_name, message.from_user.last_name, message.from_user.username, time.ctime()))
        cursor.connection.commit()
    await message.answer(f"Привет {message.from_user.full_name}")
    # logging.info("Бот запущен")
    
class MailingState(StatesGroup):
    text = State()
    
@dp.message_handler(commands='mailing')
async def start_mailing(message:types.Message):
    if message.from_user.id != ADMIN_ID:
        await message.answer("У вас нет прав для использования этой команды!")
        return
    await message.answer("Напишите текст для рассылки: ")
    await MailingState.text.set()
    
    
@dp.message_handler(state=MailingState.text)
async def send_mailing(message:types.Message, state:FSMContext):
    if message.from_user.id != ADMIN_ID:
        await message.answer("У вас нет прав для использования этой команды!")
        await state.finish()
        return
    await message.answer("Начинаю рассылку...")
    cursor.execute('SELECT id FROM users;')
    users_id = cursor.fetchall()
    for user_id in users_id:
        await bot.send_message(user_id[0], message.text)
    await message.answer("Рассылка окончена...")
    await state.finish()
    
@dp.message_handler()
async def not_found(message:Message):
    await message.reply("Я вас не понял")

executor.start_polling(dp, skip_updates=True)

