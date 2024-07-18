from aiogram import Bot, Dispatcher, types, executor

bot = Bot(token='7424275032:AAENGmA6WWhBqFnuunYD0iOFXmfpuV5KtTQ')
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.answer("Привет студент !")
    
@dp.message_handler(commands='help')
async def help(message:types.Message):
    await message.answer("Чем могу помочь ?")
    
@dp.message_handler(commands='itpark')
async def itpark(message:types.Message):
    await message.reply("Приходи на курсы !")  
    
@dp.message_handler(lambda message: message.text.lower() == 'привет')
async def hello(message:types.Message):
    await message.reply("Привет, как дела ?")
    
@dp.message_handler(lambda message: message.text.lower() == 'фото')
async def photo(message:types.Message):
    await message.answer_photo("https://www.google.com/imgres?q=python&imgurl=https%3A%2F%2Fkrymmedia.com%2Fwp-content%2Fuploads%2F2022%2F06%2FPython-Symbol.png&imgrefurl=https%3A%2F%2Fkrymmedia.com%2Frazrabotka-web-prilozheniy%2Fpython%2F&docid=WeZxBfpcCDzbgM&tbnid=wJ_8EiJgjRaS-M&vet=12ahUKEwjGhPmV9a-HAxWoHRAIHYa-At4QM3oECGQQAA..i&w=3840&h=2160&hcb=2&ved=2ahUKEwjGhPmV9a-HAxWoHRAIHYa-At4QM3oECGQQAAw")
    await message.answer("https://datascientest.com/en/wp-content/uploads/sites/9/2024/02/python.png")
    
@dp.message_handler(commands='location')
async def location(message:types.Message):
    await message.answer_location(40.521534, 72.799456)
    
@dp.message_handler(commands='contact')
async def contact(message:types.Message):
    await message.answer_contact(last_name='Islam', first_name='itpark', phone_number=+996505180600)
      
executor.start_polling(dp)