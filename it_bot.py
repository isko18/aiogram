from aiogram import Bot, Dispatcher, types, executor
from config import token
from logging import basicConfig, INFO

bot = Bot(token=token)
dp = Dispatcher(bot)
basicConfig(level=INFO)

start_buttons = [
    types.KeyboardButton('О нас'),
    types.KeyboardButton('Курсы'),
    types.KeyboardButton('Адрес'),
    types.KeyboardButton('Контакты'),
]

start_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*start_buttons)

@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.answer(f'Здравствуйте, {message.from_user.full_name}!', reply_markup=start_keyboard)

@dp.message_handler(text='О нас')
async def about_us(message:types.Message):
    await message.reply("Itpark - это IT-курсы в Оше по разным направлениям")
    
@dp.message_handler(text='Адрес')
async def send_adress(message:types.Message):
    await message.reply("Наш адрес: Город Ош, 194-224 Курманжан-Датка ул ")    
    await message.reply_location(40.521534, 72.799456)
    
@dp.message_handler(text='Контакты')
async def contact(message:types.Message):
    await message.answer(f'{message.from_user.full_name}, вот нащи контакты: ')
    await message.answer_contact("+996505180600", "Islam", "Bolsunbekovich")
    await message.answer_contact("+996222226070", "Eliza", "Erkinbek kyzy")
    
course = [
    types.KeyboardButton("Backend"),
    types.KeyboardButton("Frontend"),
    types.KeyboardButton("Android"),
    types.KeyboardButton("IOS"),
    types.KeyboardButton("UX/UI"),  
    types.KeyboardButton("Оставить заявку"),
    types.KeyboardButton("Назад")    
]

courses_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*course)

@dp.message_handler(text='Курсы')
async def about_us(message:types.Message):
    await message.answer("Вот наши курсы: ", reply_markup=courses_keyboard)
    
@dp.message_handler(text='Backend')
async def back(message:types.Message):
    await message.reply("Backend - это серверная сторона сайта или приложения. В основном код вам не виден")
    
@dp.message_handler(text='Frontend')
async def front(message:types.Message):
    await message.reply("Frontend - это лицевая сторона сайта или приложения. Эту часть вы можете видеть")
    
@dp.message_handler(text='IOS')
async def ios(message:types.Message):
    await message.reply("IOS - это разработка мобильного приложения. С IOS")

@dp.message_handler(text='Android')
async def android(message:types.Message):
    await message.reply("Android - это разработка мобильного приложения. С ОС Android")

@dp.message_handler(text='UX/UI')
async def uxui(message:types.Message):
    await message.reply("UX/UI - это дизайн сайта или приложения.")
    
@dp.message_handler(text="Назад")
async def back_start(message:types.Message):
    await start(message)
    
@dp.message_handler(text="Оставить заявку")
async def application(message:types.Message):
    button = types.KeyboardButton("Отправить контакт", request_contact=True)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(button)
    await message.answer("Пожалуйста отправьте свой контакт", reply_markup=keyboard)
    
@dp.message_handler(content_types=types.ContentType.CONTACT)
async def get_contact(message:types.Message):
    # await message.answer(message)
    await bot.send_message(-4267715696, f'Новая заявка на курсы:\nИмя: {message.contact.first_name}\nФамилия: {message.contact.last_name}\nUsername пользователя: {message.from_user.username}\nТелефон: {message.contact.phone_number}\n')
    await message.answer("Спасибо что оставили заявку\nМы свяжемся с вами в скором времени!")
    await start(message)
    
executor.start_polling(dp, skip_updates=True)
