from aiogram import Bot, Dispatcher, types, executor
from config import token
import random

bot = Bot(token=token)
dp = Dispatcher(bot)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                              


random_word = random.randint(1,3)
@dp.message_handler(commands='start')
async def start(message: types.Message):
   await message.answer("Я загадал число от 1,3")
 
   

@dp.message_handler()
async def num(message: types.Message):
 
    if int(message.text) == random_word:
      await message.answer("Поздравляю,вы выиграли!")
    
      await message.answer_photo("https://media.makeameme.org/created/you-win-nothing-b744e1771f.jpg")
    else:
      await message.answer_photo("https://media.makeameme.org/created/sorry-you-lose.jpg")
      

executor.start_polling(dp)
