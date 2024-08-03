import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ParseMode
from config import token
from aiogram.contrib.middlewares.fsm import FSMContext
from aiogram.dispatcher import FSMContext, Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage

logging.basicConfig(level=logging.INFO)

bot = Bot(token=token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
    
notes = []

class NoteStates(StatesGroup):
    waiting_for_note = State()

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я бот для заметок.\n"
                        "Доступные команды:\n"
                        "/add - добавить заметку\n"
                        "/notes - показать все заметки")

@dp.message_handler(commands=['add'])
async def add_note_start(message: types.Message):
    await message.reply("Пожалуйста, введите текст заметки.")
    await NoteStates.waiting_for_note.set()

@dp.message_handler(state=NoteStates.waiting_for_note, content_types=types.ContentTypes.TEXT)
async def add_note_complete(message: types.Message, state: FSMContext):
    note = message.text
    notes.append(note)
    await message.reply("Заметка добавлена.")
    await state.finish()

@dp.message_handler(commands=['notes'])
async def list_notes(message: types.Message):
    if not notes:
        await message.reply("Список заметок пуст.")
    else:
        response = "\n".join([f"{i+1}. {note}" for i, note in enumerate(notes)])
        await message.reply(response, parse_mode=ParseMode.MARKDOWN)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
