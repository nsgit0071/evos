from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton)

main = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🍴 Меню"),
        ],
        [
            KeyboardButton(text="🛍 Мои заказы"),
        ],
        [
            KeyboardButton(text="✍️Оставить отзыв"),
            KeyboardButton(text="⚙️Настройки"),
        ],
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите способ подачи"

)

help = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📞Мой номер", request_contact=True),
        ],

        [
            KeyboardButton(text="⬅️ Назад"),
        ],
    ],

    resize_keyboard=True,
    input_field_placeholder="Выберите способ подачи"

)
#

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🗺 Мои адреса"),
        ],

        [
            KeyboardButton(text="Отправьте 📍 геолокацию ", request_location=True),
            KeyboardButton(text="⬅️ Назад"),
        ],
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите способ подачи"

)
#

myAddress = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🗺 Мои адреса"),
        ],

        [
            KeyboardButton(text="Отправьте 📍 геолокацию ", request_location=True),
            KeyboardButton(text="⬅️ Назад"),
        ],
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите способ подачи"

)
#

setting = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Изменить язык"),
        ],

        [
            KeyboardButton(text="⬅️ Назад"),
        ],
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите способ подачи"

)
#

settingLan = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🇷🇺 Русский"),
            KeyboardButton(text="🇺🇿 O'zbekcha"),
        ],

        [
            KeyboardButton(text="⬅️ Назад"),
        ],
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите способ подачи"

)
