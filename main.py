import asyncio
import logging
import keyboard
from config import BOT_TOKEN
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram import F
from aiogram.filters.state import State, StatesGroup
from aiogram.types import Contact

bot = Bot(token=BOT_TOKEN, parse_mode='HTML')
dp = Dispatcher()


class Auth(StatesGroup):
    name = State()
    location = State()
    lang = State()


# Start
@dp.message(CommandStart())
async def handler_start(message: types.Message):
    text = f"EVOS | Доставка botiga xush kelibsiz!{message.from_user.full_name}"

    await message.answer(text=text, reply_markup=keyboard.main)


# Start End

# Menu
@dp.message(F.text == '🍴 Меню')
async def menu(message: types.Message):

    await message.answer(text="Отправьте 📍 геолокацию или выберите адрес доставки", reply_markup=keyboard.menu)


# Menu End In
# Menu > Address
@dp.message(F.text == '🗺 Мои адреса')
async def myAddress(message: types.Message):

    await message.answer(text="Пусто", reply_markup=keyboard.myAddress)


# Menu > Address End


# Menu End

# MY Cart
@dp.message(F.text == '🛍 Мои заказы')
async def myCart(message: types.MenuButton):
    # Navigate back to the initial menu (handler_start)
    await message.answer(text="Вы совсем ничего не заказали.")


# MY Cart End

# help
@dp.message(F.text == '✍️Оставить отзыв')
async def help(message: types.MenuButton):
    # Navigate back to the initial menu (handler_start)
    await message.answer(text="Поделитесь контактом для дальнейшего связи с Вами", reply_markup=keyboard.help)


# my number
# @dp.message(F.is_(Contact))
# async def cotact(message: types.Contact):
#     # Navigate back to the initial menu (handler_start)
#     await message.answer(text="Поделитесь контактом для дальнейшего связи с Вами")


# help End

# Settings
@dp.message(F.text == '⚙️Настройки')
async def setting(message: types.MenuButton):

    await message.answer(text="Выберите действие:", reply_markup=keyboard.setting)


# Lang
@dp.message(F.text == 'Изменить язык')
async def settingLan(message: types.MenuButton):

    await message.answer(text="Выберите язык:", reply_markup=keyboard.settingLan)


# EndLang
# Settings End


# Back button
@dp.message(F.text == '⬅️ Назад')
async def back_button(message: types.MenuButton):
    # Navigate back to the initial menu (handler_start)
    await handler_start(message)


# Back button End
async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
