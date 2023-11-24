import telebot
from telebot import types
import os

TOKEN = os.getenv('TELEGRAM_BOT_API_ID')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.row(types.InlineKeyboardButton("🌐︎ Wᴇʙsɪᴛᴇ", url="https://jinix6.github.io/Craftland"),
                types.InlineKeyboardButton("📷 Iɴsᴛᴀɢʀᴀᴍ", url="https://instagram.com/jinxx6_6?igshid=MzNlNGNkZWQ4Mg=="),
                types.InlineKeyboardButton("😺 GɪᴛHᴜʙ", url="https://github.com/jinix6"))
    keyboard.row(types.InlineKeyboardButton("🚀 Tᴇʟᴇɢʀᴀᴍ", url="https://t.me/Jinxx6_6_real"),
                types.InlineKeyboardButton("🚀 Tᴇʟᴇɢʀᴀᴍ 2", url="https://t.me/crystal_v1"))

    bot.send_message(message.chat.id, '🔗 Hᴇʀᴇ Aʀᴇ Sᴏᴍᴇ ʟɪɴᴋs:', reply_markup=keyboard)

@bot.message_handler(func=lambda message: True, content_types=['text'])
def handle_unknown(message):
    bot.send_message(message.chat.id, "Uɴᴋɴᴏᴡɴ Mᴇssᴀɢᴇ. Pʟᴇᴀsᴇ Usᴇ Tʜᴇ /start Cᴏᴍᴍᴀɴᴅ.")

bot.polling()
