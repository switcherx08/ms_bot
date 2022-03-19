from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import configure
bot = Bot(token = configure.config['token'])
dp = Dispatcher(bot)
@dp.message_handler()
async def get_message(message: types.Message):
    chat_id = message.chat.id
    text = "Какой-то текст"
    sent_message = await bot.send_message(chat_id=chat_id, text=text)
    print(sent_message.to_python())
@dp.message_handler(commands=['today'])
async def send_today(message: types.Message):
    chat_id = message.chat.id


executor.start_polling(dp)

