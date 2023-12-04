from aiogram import Bot, Dispatcher, executor, types
from button.evos_config import (
    # Bot_Token,
    bosh,
    fililallar,
    yaqin_filiallar,
    toshkent_sh,
    viloyatlar_ish_urin,
    lovozim_t
)

from button.caption import (
Kampaniya_xaqida_text,
Filiall_txt,
Bosh_ofis_text,
samarqand_darvoza_text,
oloy_bozori_text,
malika_text,
yahyo_gulomov_text,
orqaga_f
)


API_TOKEN = BOT_TOKEN

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def satrt_evos(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id,
                         photo="AgACAgIAAxkBAANCZWXtSOOkesDwoll86ZXCZhLSJsUAAorSMRtpOjFLd-4IIZi2kG0BAAMCAANtAAMzBA",
                         reply_markup=bosh)



@dp.message_handler(text="🏢 Kompaniya haqida")
async def Kompaniya_haqida(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id,
                         photo='AgACAgIAAxkBAAM8ZWXraEOj7eFDmK1h9QyohBQbiqsAAofSMRtpOjFLxwuz6dEwVx0BAAMCAANtAAMzBA',
                         caption=Kampaniya_xaqida_text)


@dp.message_handler(text="📍 Fililallar")
async def filial_uz(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id,
                         photo="AgACAgIAAxkBAANUZWXui6Qf8GppWLvwLJ5mJJdHlIwAAozSMRtpOjFLvkLIOVPug6IBAAMCAAN4AAMzBA",
                         caption=Filiall_txt,
                         reply_markup=fililallar)


@dp.message_handler(text="☕️ Yaqin filiallarni ko'rsatish")
async def yaqin_filiallar(message: types.Message):
    await message.answer(text=message.text,
                         reply_markup=yaqin_filiallar)


@dp.message_handler(content_types=types.ContentType.LOCATION)
async def Geolokatsiyani_yuborish(message: types.Message):
    await message.location(text=message.text)


@dp.message_handler(text="🏢 Bosh ofis")
async def Bosh_ofis(message: types.Message):
    await bot.send_photo(chat_id = message.from_user.id,
                         photo = "AgACAgIAAxkBAAOHZWmqQYLYr2IGD70bFkqnNZwf0WcAAr7WMRuLiFFLNTCahp_-0D8BAAMCAAN5AAMzBA",
                         caption = Bosh_ofis_text,
                         reply_markup = fililallar)

@dp.message_handler(text="Toshkent sh.")
async def Toshkent_sh(message: types.Message):
    await message.answer(text=message.text, reply_markup=toshkent_sh)

@dp.message_handler(text="⬅️ Ortga")
async def Orqaga_b(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id,
                         photo="AgACAgIAAxkBAAPdZWm3X2uRzzEeYIPfZUxpleAAATBoAAIJ1zEbi4hRS4gPboyFOx28AQADAgADbQADMwQ",
                         reply_markup=bosh
                         )


@dp.message_handler(text="📍 Samarqand Darvoza")
async def Toshkent_sh(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id,
                         photo="AgACAgIAAxkBAAOZZWmuKbM0NE93tXRPqX8vyu-dkE0AAtbWMRuLiFFLnT5nBDWEN3MBAAMCAAN5AAMzBA",
                         caption=samarqand_darvoza_text,
                         )



@dp.message_handler(text="📍 Oloy bozori")
async def Oloy_bozori(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id,
                         photo="AgACAgIAAxkBAAOhZWmv19AXGitYBCdezvMZBPM2v0wAAuPWMRuLiFFL44PCO5KvWSsBAAMCAAN4AAMzBA",
                         caption=oloy_bozori_text,
                         )


@dp.message_handler(text="📍 Malika")
async def Malika(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id,
                         photo="AgACAgIAAxkBAAOjZWmwpUW82One2RAzlAdTW3jps4gAAufWMRuLiFFL1Oonboo-jtEBAAMCAAN5AAMzBA",
                         caption=malika_text,)



@dp.message_handler(text="📍 Yahyo G'ulomov, 94")
async def Yahyo_Gulomov_94(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id,
                         photo="AgACAgIAAxkBAAOqZWmxhCzeH-bFpmaeUqIDmC_NlVMAAuvWMRuLiFFLAAGqTl8019xOAQADAgADeQADMwQ",
                         caption=yahyo_gulomov_text,)



@dp.message_handler(text="Ortga↩️")
async def Ortga_f(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id,
                         photo="AgACAgIAAxkBAAPAZWmyle4QveuoVEpOSmyvD83ymOkAAvHWMRuLiFFL6b5Tl5cMTx0BAAMCAAN4AAMzBA",
                         caption=orqaga_f,
                         reply_markup=fililallar,
                         )



@dp.message_handler(text="💼 Bo'sh ish o'rinlari")
async def Bush_ish_urinlari(message: types.Message):
    await message.answer(text=f"EVOS jamoasiga qo'shiling!n/📍 Shaharni tanlang.",
                         reply_markup=viloyatlar_ish_urin)


@dp.message_handler(text="Toshkent")
async def Toshkenti(message: types.Message):
    await message.answer(text=f"💼 Sizni qiziqtirgan lavozimni tanlang",
                         reply_markup=lovozim_t)




@dp.message_handler(content_types="photo")
async def satrt_evos(message: types.Message):
    file_id = message.photo[-1].file_id
    print(file_id)
    await message.answer_photo(photo=file_id, caption=file_id, reply_markup=bosh)



if __name__ == '__main__':
    print("bot ishga tushdi")
    executor.start_polling(dp, skip_updates=False)
