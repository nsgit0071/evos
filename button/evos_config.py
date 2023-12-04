from aiogram.types import ReplyKeyboardMarkup, KeyboardButton





bosh = ReplyKeyboardMarkup(
    [
        [KeyboardButton("🏢 Kompaniya haqida"), KeyboardButton("📍 Fililallar")],
        [KeyboardButton("💼 Bo'sh ish o'rinlari")],
        [KeyboardButton("Menyu"), KeyboardButton("🗣 Yangiliklar")],
        [KeyboardButton("📞 Kontaktlar/Manzil"), KeyboardButton("🇺🇿/🇷🇺 Til")]
    ],
    resize_keyboard=True
)


fililallar = ReplyKeyboardMarkup(
    [
        [KeyboardButton("☕️ Yaqin filiallarni ko'rsatish")],
        [KeyboardButton("🏢 Bosh ofis"), KeyboardButton("Toshkent sh.")],
        [KeyboardButton("⬅️ Ortga")]
    ],
    resize_keyboard=True
)

yaqin_filiallar = ReplyKeyboardMarkup(
    [
        [KeyboardButton("Geolokatsiyani yuborish")],
        [KeyboardButton("⬅️ Орқага")]
    ]
)

toshkent_sh = ReplyKeyboardMarkup(
    [
        [KeyboardButton("📍 Samarqand Darvoza"), KeyboardButton("📍 Oloy bozori")],
        [KeyboardButton("📍 Malika"), KeyboardButton("📍 Yahyo G'ulomov, 94")],
        [KeyboardButton("Ortga↩️")]
    ]
)

viloyatlar_ish_urin = ReplyKeyboardMarkup(
    [
        [KeyboardButton("Toshkent"), KeyboardButton("Andijon")],
        [KeyboardButton("Quqon"), KeyboardButton("Namangan")],
        [KeyboardButton("Toshkent viloyati"), KeyboardButton("Samarqand")],
        [KeyboardButton("Farg'ona"), KeyboardButton("Xorazim")],
        [KeyboardButton("Navoi")],
        [KeyboardButton("❌ Bekor qilish ❌"), KeyboardButton("ortga ↩️")],
    ]
)

lovozim_t = ReplyKeyboardMarkup(
    [
        [KeyboardButton("Universal xodim"), KeyboardButton("Call-markaz operatori")],
        [KeyboardButton("Kuryer")],
        [KeyboardButton("❌ Bekor qilish ❌"), KeyboardButton("Ortga ↩️t")]
    ]
)