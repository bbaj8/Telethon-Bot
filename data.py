from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("🔥 ابدا بتوليد الجلسه 🔥", callback_data="generate")]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="🏠 رجوع 🏠", callback_data="home")]
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("✨ قناه السووس ✨", url="https://t.me/JMTHON")],
        [
            InlineKeyboardButton("How to Use ❔", callback_data="help"),
            InlineKeyboardButton("🎪 About 🎪", callback_data="about")
        ],
        [InlineKeyboardButton("اذا كنت تريد الاستخراج بنفسك ", url="https://t.me/JMTHON/988")],
    ]

    START = """
Hey {}

تم عمل هذا البوت لسهوله استخراج كود تيرمكس ملاحضه(اذا كنت لا تثق في هذا البوت يمكن الاستخراج من هنا https://t.me/JMTHON/988) 

    """

    HELP = """
✨ **Available Commands** ✨

/about - حول البوت
/help - هاي الرساله
/start - بدا البوت
/generate - بدا الاستخراج
/cancel - الغاء عملية
/restart - اعادة تشغيل
"""

    ABOUT = """
**About This Bot** 

لغه البوت - بايثون البوت معرب 
    """
