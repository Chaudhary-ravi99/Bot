from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters




TOKEN = os.getenv('TELEGRAM_BOT_API_ID')

def start(update, context):
    keyboard = [
    [InlineKeyboardButton("🌐︎ Wᴇʙsɪᴛᴇ", url="https://jinix6.github.io/Craftland"),
     InlineKeyboardButton("📷 Iɴsᴛᴀɢʀᴀᴍ", url="https://instagram.com/jinxx6_6?igshid=MzNlNGNkZWQ4Mg=="),
    InlineKeyboardButton("😺 GɪᴛHᴜʙ", url="https://github.com/jinix6")],
     [InlineKeyboardButton("🚀 Tᴇʟᴇɢʀᴀᴍ", url="https://t.me/Jinxx6_6_real"),
     InlineKeyboardButton("🚀 Tᴇʟᴇɢʀᴀᴍ 2", url="https://t.me/crystal_v1")]
]


    reply_markup = InlineKeyboardMarkup(keyboard, resize_keyboard=True)

    update.message.reply_text('🔗 Hᴇʀᴇ Aʀᴇ Sᴏᴍᴇ ʟɪɴᴋs:', reply_markup=reply_markup)

def handle_unknown(update, context):

    update.message.reply_text("Uɴᴋɴᴏᴡɴ Mᴇssᴀɢᴇ. Pʟᴇᴀsᴇ Usᴇ Tʜᴇ /start Cᴏᴍᴍᴀɴᴅ.")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    

    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_unknown))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()