import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "7877614278:AAEpCvHIBtV_tPP2j1WSdWbVNKfjAVoUaoQ"  # <-- Bot tokeningizni shu yerga qo‘ying
ADMIN_ID = 7442097952  # Admin (Call Center) ID'si

bot = telebot.TeleBot(TOKEN)

# 🏠 Asosiy menyu
def main_menu():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton("📚 Mutaxassislarimiz", callback_data="specialists"),
        InlineKeyboardButton("📖 Kurslarimiz", callback_data="courses")
    )
    markup.add(
        InlineKeyboardButton("ℹ️ Excel Masters haqida", callback_data="about"),
        InlineKeyboardButton("📞 Biz bilan bog‘lanish", callback_data="contact")
    )
    return markup

# 📖 Kurslar menyusi
def courses_menu():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton("🖥 Kompyuter Savodxonligi", callback_data="course_1"),
        InlineKeyboardButton("📊 Excel Boshlang‘ich", callback_data="course_2")
    )
    markup.add(
        InlineKeyboardButton("📈 Excel Pro", callback_data="course_3"),
        InlineKeyboardButton("📉 Excel Pro Max", callback_data="course_4")
    )
    markup.add(InlineKeyboardButton("⬅️ Orqaga", callback_data="main_menu"))
    return markup

# 📚 Mutaxassislar menyusi
def specialists_menu():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton("👨‍🏫 Shoazim", callback_data="spec_1"),
        InlineKeyboardButton("👨‍🏫 Feruzbek", callback_data="spec_2"),
        InlineKeyboardButton("👨‍🏫 Begzod", callback_data="spec_3")
    )
    markup.add(InlineKeyboardButton("⬅️ Orqaga", callback_data="main_menu"))
    return markup

# 📖 Kurslar haqida batafsil ma’lumot
course_info = {
    "course_1": "✅ **🖥 Kompyuter Savodxonligi**\n\n📌 Word va PowerPoint\n\n📌 Internet va e-mail\n\n📌 Windows va fayllar\n\n📅 1-aprel 2025\n\n⏳ 2 oy\n\n💰 500 000 so‘m/oyiga",
    "course_2": "✅ **📊 Excel Boshlang‘ich**\n\n📌 Jadval yaratish\n\n📌 Asosiy formulalar\n\n📌 Diagrammalar\n\n📅 10-aprel 2025\n\n⏳ 2,5 oy\n\n💰 600 000 so‘m/oyiga",
    "course_3": "✅ **📈 Excel Pro**\n\n📌 Murakkab formulalar\n\n📌 Filtrlash\n\n📌 Pivot jadval\n\n📅 20-aprel 2025\n⏳ 3 oy\n\n💰 750 000 so‘m/oyiga",
    "course_4": "✅ **📉 Excel Pro Max**\n\n📌 VBA dasturlash\n\n📌 Katta ma’lumotlar\n\n📌 Avtomatlashtirish\n\n📅 5-may 2025\n\n⏳ 4 oy\n\n💰 900 000 so‘m/oyiga"
}

# 📚 Mutaxassislar haqida batafsil ma’lumot
specialist_info = {
    "spec_1": "👨‍🏫 **Shoazim**\n\n📌 7 yillik tajriba\n\n📚 Excel, Power BI, SQL\n\n🎓 Microsoft sertifikati",
    "spec_2": "👨‍🏫 **Feruzbek**\n\n📌 5 yillik tajriba\n\n📚 Excel, Google Sheets\n\n🎓 Xalqaro sertifikat",
    "spec_3": "👨‍🏫 **Begzod**\n\n📌 6 yillik tajriba\n\n📚 Excel, Python, Power Query\n\n🎓 Data Science mutaxassisi"
}

# ℹ️ Excel Masters haqida
excel_masters_info = (
    "ℹ️ **Excel Masters** – Excel va Data Analysis bo‘yicha kurslar markazi.\n"
    "📍 2021-yilda tashkil etilgan\n\n"
    "👨‍💼 Asoschisi: Shahzod Sayfulla Begzod o‘g‘li\n\n"
    "‍💻 Microsoftning RASMIY hamkori\n\n"
    "🏆 3000+ muvaffaaqiyatli o‘quvchilar\n\n"
    "📌 Excel’da ishlash, VBA va Data Analysis bo‘yicha bilimlar beriladi."
)

# 📞 Bog‘lanish ma’lumotlari
contact_info_text = (
    "📞 **Biz bilan bog‘lanish:**\n"
    "📲 **Telefon:** +998 90 968 61 61\n"
    "✉️ **Telegram:** [@excelmasters_Shoazim](https://t.me/excelmasters_Shoazim)\n"
    "📍 **Manzil:** Toshkent, Chilonzor, Novza metro yonida"
)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "main_menu":
        bot.edit_message_text("🏠 Asosiy menyu:", call.message.chat.id, call.message.message_id, reply_markup=main_menu())
    elif call.data == "courses":
        bot.edit_message_text("📖 Kurslarimiz ro‘yxati:", call.message.chat.id, call.message.message_id, reply_markup=courses_menu())
    elif call.data == "specialists":
        bot.edit_message_text("📚 Bizning mutaxassislar:", call.message.chat.id, call.message.message_id, reply_markup=specialists_menu())
    elif call.data == "about":
        bot.edit_message_text(excel_masters_info, call.message.chat.id, call.message.message_id, parse_mode="Markdown", reply_markup=main_menu())
    elif call.data == "contact":
        # Telefon raqamini so‘rash tugmasi
        markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        button = KeyboardButton("📞 Raqamni yuborish", request_contact=True)
        markup.add(button)

        # Foydalanuvchiga xabar
        bot.send_message(
            call.message.chat.id,
            "📞 Biz bilan bog‘lanish uchun quyidagilardan birini tanlang:\n\n"
            "📲 **Telefon orqali:** +998909686161\n"
            "✉️ **Telegram:** [@excelmasters_Shoazim](https://t.me/excelmasters_Shoazim)\n\n"
            "📍 [Bizning manzil](https://maps.app.goo.gl/b2zbEsXbFgc4f46dA)\n\n"
            "✅ Agar biz siz bilan bog‘lanishimizni istasangiz, pastdagi tugma orqali raqamingizni yuboring.",
            reply_markup=markup,
            parse_mode="Markdown"
        )

    elif call.data in course_info:
        bot.edit_message_text(course_info[call.data], call.message.chat.id, call.message.message_id, parse_mode="Markdown", reply_markup=courses_menu())
    elif call.data in specialist_info:
        bot.edit_message_text(specialist_info[call.data], call.message.chat.id, call.message.message_id, parse_mode="Markdown", reply_markup=specialists_menu())

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(
        message.chat.id,
        text = f"Assalamu alaykum, hurmatli {message.from_user.first_name}! 👋\n\n Excel Masters o'q'uv markaziga xush kelibsiz \n\n"
        "🔽 Kerakli bo‘limni tanlang:",
        reply_markup=main_menu()
    )


# 📞 Foydalanuvchi telefon raqamini yuborganida
@bot.message_handler(content_types=['contact'])
def handle_contact(message):
    phone_number = message.contact.phone_number
    user_name = message.from_user.first_name
    username = message.from_user.username  # Username olish
    username_text = f"@{username}" if username else "Username mavjud emas"

    # Foydalanuvchiga tasdiqlovchi xabar
    bot.send_message(
        message.chat.id,
        f"📞 Raqamingiz qabul qilindi: {phone_number}\n"
        f"📢 Call center tez orada siz bilan bog‘lanadi! ✅"
    )

    # Adminga xabar yuborish
    bot.send_message(
        ADMIN_ID,
        f"📩 **Yangi ro‘yxatdan o‘tish:**\n"
        f"📲 **Telefon:** +{phone_number}\n"
        f"🔗 **Username:** {username_text}"
    )

    # Asosiy menyuga qaytarish
    bot.send_message(message.chat.id, "🏠 Asosiy menyu:", reply_markup=main_menu())


# 🔄 Botni doimiy ishlash rejimiga qo‘yish
bot.polling(none_stop=True)