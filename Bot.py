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
    project_button = types.InlineKeyboardButton("🗂️ Pʀᴏᴊᴇᴄᴛ", callback_data="project_button")
    keyboard.row(project_button)

    bot.send_message(message.chat.id, '🔗 Hᴇʀᴇ Aʀᴇ Sᴏᴍᴇ ʟɪɴᴋs:', reply_markup=keyboard)
    bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    
@bot.callback_query_handler(func=lambda call: call.data == "project_button")
def project_button_callback(call):
    updated_keyboard = types.InlineKeyboardMarkup()
    
    updated_keyboard.row(types.InlineKeyboardButton("🧬 Eɴᴛɪᴛʏ Aʟʟ Bʟᴏᴄᴋ", url="https://t.me/freefirecraftlandgroup/146275"),
                types.InlineKeyboardButton("🔥 Aʟʟ Bʟᴏᴄᴋs", url="https://youtu.be/2C6DFikY0Bw?si=pZAEvYitBJQsYFZJ"))
                
    updated_keyboard.row(types.InlineKeyboardButton("🔙 Bᴀᴄᴋ", callback_data="back_button"))
    
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                          text="🔗 Hᴇʀᴇ Aʀᴇ Sᴏᴍᴇ ʟɪɴᴋs:", reply_markup=updated_keyboard)



@bot.callback_query_handler(func=lambda call: call.data == "back_button")
def back_button_callback(call):
    original_keyboard = types.InlineKeyboardMarkup()
    original_keyboard.row(types.InlineKeyboardButton("🌐︎ Wᴇʙsɪᴛᴇ", url="https://jinix6.github.io/Craftland"),
                          types.InlineKeyboardButton("📷 Iɴsᴛᴀɢʀᴀᴍ", url="https://instagram.com/jinxx6_6?igshid=MzNlNGNkZWQ4Mg=="),
                          types.InlineKeyboardButton("😺 GɪᴛHᴜʙ", url="https://github.com/jinix6"))
    original_keyboard.row(types.InlineKeyboardButton("🚀 Tᴇʟᴇɢʀᴀᴍ", url="https://t.me/Jinxx6_6_real"),
                          types.InlineKeyboardButton("🚀 Tᴇʟᴇɢʀᴀᴍ 2", url="https://t.me/crystal_v1"))
    original_keyboard.row(types.InlineKeyboardButton("🗂️ Pʀᴏᴊᴇᴄᴛ", callback_data="project_button"))

    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                          text="🔗 Hᴇʀᴇ Aʀᴇ Sᴏᴍᴇ ʟɪɴᴋs:", reply_markup=original_keyboard)



@bot.message_handler(func=lambda message: message.text != "/start", content_types=['text'])
def handle_unknown(message):
    sticker_file_id = "CAACAgUAAxkBAAEn47VlY6Q_MPqgRtZnGGpc36FeN7TJJwACyQwAAmj_IFcsiFi0kiNUgDME"
    bot.send_sticker(message.chat.id, sticker_file_id)
    bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
bot.polling()