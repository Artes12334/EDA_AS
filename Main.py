from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo
import json
import config

bot = Bot(config.BOT_TOKEN)
dp = Dispatcher(bot)

markup = types.ReplyKeyboardMarkup()
btn0 = types.KeyboardButton("🥛Молоко")
btn1 = types.KeyboardButton("🥚Яйца")
markup.row(btn0, btn1)
btn2 = types.KeyboardButton("🥕Овощи")
btn3 = types.KeyboardButton("🥝Фрукты и ягоды")
markup.row(btn2, btn3)
btn4 = types.KeyboardButton("🍭Сладости")
btn5 = types.KeyboardButton("🥓Мясо и птица")
markup.row(btn4, btn5)
btn6 = types.KeyboardButton("🐟Рыба")
btn7 = types.KeyboardButton("🥟Заморозка")
markup.row(btn6, btn7)
btn8 = types.KeyboardButton("☕Напитки")
btn9 = types.KeyboardButton("🌭Колбасные изделия")
markup.row(btn8, btn9)
btn10 = types.KeyboardButton("🥯Выпечка")
btn11 = types.KeyboardButton("🧀Сыры")
markup.row(btn10, btn11)
btn12 = types.KeyboardButton("🍝Макароны и крупы")
btn13 = types.KeyboardButton("🍞Всё для выпечки")
markup.row(btn12, btn13)
btn14 = types.KeyboardButton("🍞Масло, соусы и специи")
btn15 = types.KeyboardButton("🥫Консервы и соления")
markup.row(btn14, btn15)
btn16 = types.KeyboardButton("🌰Орехи, снеки и чипсы")
btn17 = types.KeyboardButton("🧸Для детей")
markup.row(btn16, btn17)
btn18 = types.KeyboardButton("💄Косметика")
btn19 = types.KeyboardButton("🧪Бытовая химия")
markup.row(btn18, btn19)
markup.add(types.KeyboardButton("🛒Корзина"))
markup.add(types.KeyboardButton("📝Оформить заказ", web_app=WebAppInfo(url="https://artes12334.github.io/EDA_AS/")))
markup.add(types.KeyboardButton("🆘Клиентская служба"))

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Вас приветствует служба доставки продуктов ЕДА АС")
    await message.answer("Выберите, что хотите заказать", reply_markup=markup)

@dp.message_handler(commands=['help'])
async def start(message: types.Message):
    await message.answer("Основатель - telegram: https://t.me/Russianboss228")
    await message.answer("Основатель - telegram: https://t.me/ArtSlast512")

@dp.message_handler(content_types=["text"])
async def help(message: types.Message):
    print(message.text)
    if message.text.lower().strip() == "🆘клиентская служба":
        await message.answer("Основатель - telegram: https://t.me/Russianboss228")
        await message.answer("Основатель - telegram: https://t.me/ArtSlast512")

    if message.text.lower().strip() == "🥛молоко":
        markupMilk = types.ReplyKeyboardMarkup()
        markupMilk.add(types.KeyboardButton("Молоко"))
        markupMilk.add(types.KeyboardButton("Назад"))
        await message.answer("Выберите продукт", reply_markup=markupMilk)

    if message.text.lower().strip() == "🥚яйца":
        markupEggs = types.ReplyKeyboardMarkup()
        markupEggs.add(types.KeyboardButton("Яйца"))
        markupEggs.add(types.KeyboardButton("Назад"))
        await message.answer("Выберите продукт", reply_markup=markupEggs)

    if message.text.lower().strip() == "🥕овощи":
        markupVeg = types.ReplyKeyboardMarkup()
        markupVeg.add(types.KeyboardButton("Овощи"))
        markupVeg.add(types.KeyboardButton("Назад"))
        await message.answer("Выберите продукт", reply_markup=markupVeg)

    if message.text.lower().strip() == "🥝фрукты и ягоды":
        markupBerAndFrut = types.ReplyKeyboardMarkup()
        markupBerAndFrut.add(types.KeyboardButton("Фрукты и ягоды"))
        markupBerAndFrut.add(types.KeyboardButton("Назад"))
        await message.answer("Выберите продукт", reply_markup=markupBerAndFrut)

    if message.text.lower().strip() == "🍭сладости":
        markupCandy = types.ReplyKeyboardMarkup()
        markupCandy.add(types.KeyboardButton("Сладости"))
        markupCandy.add(types.KeyboardButton("Назад"))
        await message.answer("Выберите продукт", reply_markup=markupCandy)

    if message.text.lower().strip() == "🥓мясо и птица":
        markupMeal = types.ReplyKeyboardMarkup()
        markupMeal.add(types.KeyboardButton("Мясо и птица"))
        markupMeal.add(types.KeyboardButton("Назад"))
        await message.answer("Выберите продукт", reply_markup=markupMeal)

    if message.text.lower().strip() == "🐟рыба":
        markupFish = types.ReplyKeyboardMarkup()
        markupFish.add(types.KeyboardButton("Рыба"))
        markupFish.add(types.KeyboardButton("Назад"))
        await message.answer("Выберите продукт", reply_markup=markupFish)

    if message.text.lower().strip() == "🥟заморозка":
        markupFrige = types.ReplyKeyboardMarkup()
        markupFrige.add(types.KeyboardButton("Мороженные продукты"))
        markupFrige.add(types.KeyboardButton("Назад"))
        await message.answer("Выберите продукт", reply_markup=markupFrige)

    if message.text.lower().strip() == "☕напитки":
        markupDrink = types.ReplyKeyboardMarkup()
        markupDrink.add(types.KeyboardButton("Напитки"))
        markupDrink.add(types.KeyboardButton("Назад"))
        await message.answer("Выберите продукт", reply_markup=markupDrink)

    if message.text.lower().strip() == "🌭колбасные изделия":
        markupColbas = types.ReplyKeyboardMarkup()
        markupColbas.add(types.KeyboardButton("Колбасные изделия"))
        markupColbas.add(types.KeyboardButton("Назад"))
        await message.answer("Выберите продукт", reply_markup=markupColbas)

    if message.text.lower().strip() == "🥯выпечка":
        markupBread = types.ReplyKeyboardMarkup()
        markupBread.add(types.KeyboardButton("Выпечка"))
        markupBread.add(types.KeyboardButton("Назад"))
        await message.answer("Выберите продукт", reply_markup=markupBread)

    if message.text.lower().strip() == "🧀сыры":
        markupChess = types.ReplyKeyboardMarkup()
        markupChess.add(types.KeyboardButton("Сыры"))
        markupChess.add(types.KeyboardButton("Назад"))
        await message.answer("Выберите продукт", reply_markup=markupChess)

    if message.text.lower().strip() == "🍝макароны и крупы":
        markupMakaron = types.ReplyKeyboardMarkup()
        markupMakaron.add(types.KeyboardButton("Макароны и крупы"))
        markupMakaron.add(types.KeyboardButton("Назад"))
        await message.answer("Выберите продукт", reply_markup=markupMakaron)

    if message.text.lower().strip() == "🍞всё для выпечки":
        markupForBread = types.ReplyKeyboardMarkup()
        markupForBread.add(types.KeyboardButton("Всё для выпечки"))
        markupForBread.add(types.KeyboardButton("Назад"))
        await message.answer("Выберите продукт", reply_markup=markupForBread)

    if message.text.lower().strip() == "🍞масло, соусы и специи":
        markupMaslo = types.ReplyKeyboardMarkup()
        markupMaslo.add(types.KeyboardButton("Масло, соусы и специи"))
        markupMaslo.add(types.KeyboardButton("Назад"))
        await message.answer("Выберите продукт", reply_markup=markupMaslo)

    if message.text.lower().strip() == "🥫консервы и соления":
        markupConserv = types.ReplyKeyboardMarkup()
        markupConserv.add(types.KeyboardButton("Консервы и соления"))
        markupConserv.add(types.KeyboardButton("Назад"))
        await message.answer("Выберите продукт", reply_markup=markupConserv)

    if message.text.lower().strip() == "🌰орехи, снеки и чипсы":
        markupChipsAndSnak = types.ReplyKeyboardMarkup()
        markupChipsAndSnak.add(types.KeyboardButton("Орехи, снеки и чипсы"))
        markupChipsAndSnak.add(types.KeyboardButton("Назад"))
        await message.answer("Выберите продукт", reply_markup=markupChipsAndSnak)

    if message.text.lower().strip() == "🧸для детей":
        markupForChild = types.ReplyKeyboardMarkup()
        markupForChild.add(types.KeyboardButton("Для детей"))
        markupForChild.add(types.KeyboardButton("Назад"))
        await message.answer("Выберите продукт", reply_markup=markupForChild)

    if message.text.lower().strip() == "💄косметика":
        markupCosmetic = types.ReplyKeyboardMarkup()
        markupCosmetic.add(types.KeyboardButton("Косметика"))
        markupCosmetic.add(types.KeyboardButton("Назад"))
        await message.answer("Выберите продукт", reply_markup=markupCosmetic)

    if message.text.lower().strip() == "🧪бытовая химия":
        markupChemistry = types.ReplyKeyboardMarkup()
        markupChemistry.add(types.KeyboardButton("Бытовая химия"))
        markupChemistry.add(types.KeyboardButton("Назад"))
        await message.answer("Выберите продукт", reply_markup=markupChemistry)

    if message.text.lower().strip() == "назад":
        await message.answer("Выберите, что хотите заказать", reply_markup=markup)

@dp.message_handler(content_types=["web_app_data"])
async def webData(message: types.Message):
    result = json.loads(message.web_app_data.data)
    await message.answer(f"Имя: {result['name']} \nАдрес: {result['adres']} \nТелефон: {result['phone']}")
    await bot.send_invoice(message.chat.id, "Покупка продуктов", "Покупка продуктов", "invoice", config.PAYMENT_TOKEN, "RUB", [types.LabeledPrice("Покупка продуктов", 100 * 100)])

@dp.message_handler(content_types=types.ContentType.SUCCESSFUL_PAYMENT)
async def success(message: types.Message):
    await message.answer(f"Оплата прошла успешно {message.successful_payment.order_info}")

executor.start_polling(dp)