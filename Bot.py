import telebot
from telebot import types
import os
import time
import datetime

TOKEN = os.getenv('TELEGRAM_BOT_API_ID')
bot = telebot.TeleBot(TOKEN)

help_status = {}
last_message_time = {}


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.row(types.InlineKeyboardButton("🌐︎ Wᴇʙsɪᴛᴇ", url="https://jinix6.github.io/Craftland"),
                types.InlineKeyboardButton("📷 Iɴsᴛᴀɢʀᴀᴍ", url="https://instagram.com/jinxx6_6?igshid=MzNlNGNkZWQ4Mg=="),
                types.InlineKeyboardButton("😺 GɪᴛHᴜʙ", url="https://github.com/jinix6"))
    keyboard.row(types.InlineKeyboardButton("🚀 Tᴇʟᴇɢʀᴀᴍ", url="https://t.me/Jinxx6_6_real"),
                types.InlineKeyboardButton("🚀 Tᴇʟᴇɢʀᴀᴍ 2", url="https://t.me/crystal_v1"))
    keyboard.row(types.InlineKeyboardButton("🗂️ Pʀᴏᴊᴇᴄᴛ", callback_data="project_button"),
                  types.InlineKeyboardButton("💬 Hᴇʟᴘ", callback_data="help"))

    bot.send_message(message.chat.id, '🔗 Hᴇʀᴇ Aʀᴇ Sᴏᴍᴇ ʟɪɴᴋs:', reply_markup=keyboard)
    bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)

@bot.callback_query_handler(func=lambda call: call.data == "project_button")
def project_button_callback(call):
    updated_keyboard = types.InlineKeyboardMarkup()
    updated_keyboard.row(types.InlineKeyboardButton("🧬 Eɴᴛɪᴛʏ Aʟʟ Bʟᴏᴄᴋ", url="https://t.me/freefirecraftlandgroup/146275"),
                types.InlineKeyboardButton("🔥 Aʟʟ Bʟᴏᴄᴋs", url="https://youtu.be/2C6DFikY0Bw?si=pZAEvYitBJQsYFZJ"))
    updated_keyboard.row(types.InlineKeyboardButton("🔙 Bᴀᴄᴋ", callback_data="back_button"))
    
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                          text="/🗂️ Pʀᴏᴊᴇᴄᴛ", reply_markup=updated_keyboard)

@bot.callback_query_handler(func=lambda call: call.data == "help")
def help_callback(call):
    user_id = call.from_user.id
    help_status[user_id] = True
    
    updated_keyboard = types.InlineKeyboardMarkup()
    updated_keyboard.row(types.InlineKeyboardButton("🔙 Bᴀᴄᴋ", callback_data="back_button"))
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                          text="💬 Sᴇɴᴅ Mᴇssᴀɢᴇ !", reply_markup=updated_keyboard)
                          
   
                                                                        
@bot.callback_query_handler(func=lambda call: call.data == "back_button")
def back_button_callback(call):
    user_id = call.from_user.id
    help_status[user_id] = False
    original_keyboard = types.InlineKeyboardMarkup()
    original_keyboard.row(types.InlineKeyboardButton("🌐︎ Wᴇʙsɪᴛᴇ", url="https://jinix6.github.io/Craftland"),
                          types.InlineKeyboardButton("📷 Iɴsᴛᴀɢʀᴀᴍ", url="https://instagram.com/jinxx6_6?igshid=MzNlNGNkZWQ4Mg=="),
                          types.InlineKeyboardButton("😺 GɪᴛHᴜʙ", url="https://github.com/jinix6"))
    original_keyboard.row(types.InlineKeyboardButton("🚀 Tᴇʟᴇɢʀᴀᴍ", url="https://t.me/Jinxx6_6_real"),
                          types.InlineKeyboardButton("🚀 Tᴇʟᴇɢʀᴀᴍ 2", url="https://t.me/crystal_v1"))
    original_keyboard.row(types.InlineKeyboardButton("🗂️ Pʀᴏᴊᴇᴄᴛ", callback_data="project_button"),
                            types.InlineKeyboardButton("💬 Hᴇʟᴘ", callback_data="help"))

    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                          text="🔗 Hᴇʀᴇ Aʀᴇ Sᴏᴍᴇ ʟɪɴᴋs:", reply_markup=original_keyboard)
                          
@bot.message_handler(func=lambda message: True)
def respond_to_all_messages(message):
    bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    user_id = message.from_user.id
    if help_status.get(user_id, False):
    
        current_time = datetime.datetime.now()
        last_time = last_message_time.get(user_id)
        if last_time is not None and (current_time - last_time).seconds < 20:
            bot.send_message(message.chat.id, f"✋ Kɪɴᴅʟʏ Wᴀɪᴛ Fᴏʀ 20 Sᴇᴄᴏɴᴅs Bᴇғᴏʀᴇ Sᴇɴᴅɪɴɢ Aɴᴏᴛʜᴇʀ Mᴇssᴀɢᴇ. Tʜɪs Hᴇʟᴘs Mᴀɪɴᴛᴀɪɴ A Sᴍᴏᴏᴛʜ Cᴏɴᴠᴇʀsᴀᴛɪᴏɴ Fʟᴏᴡ Aɴᴅ Eɴsᴜʀᴇs Oᴘᴛɪᴍᴀʟ Rᴇsᴘᴏɴsɪᴠᴇɴᴇss. Tʜᴀɴᴋ Yᴏᴜ Fᴏʀ Yᴏᴜʀ Pᴀᴛɪᴇɴᴄᴇ.\n\n⏳ Cᴜʀʀᴇɴᴛ Sᴇᴄᴏɴᴅ:{(current_time - last_time).seconds}")
            return
        last_message_time[user_id] = current_time
        mmm = f"""```Message
{message.text}```"""
        sent_message = bot.send_message(message.chat.id, f"📬 Mᴇssᴀɢᴇ Sᴜᴄᴄᴇssғᴜʟ Sᴇɴᴅᴇᴅ {mmm}", parse_mode='Markdown')
        
        user = "6903011562"
        mm = f"""Id: [{message.from_user.first_name}](tg://user?id={message.chat.id})
Message: {message.text}
"""
        bot.send_message(user, mm, parse_mode='Markdown')
        time.sleep(3)
        bot.delete_message(chat_id=message.chat.id, message_id=sent_message.message_id)
    else:
        if not message.text == "/start":
            sticker_file_id = "CAACAgUAAxkBAAEn47VlY6Q_MPqgRtZnGGpc36FeN7TJJwACyQwAAmj_IFcsiFi0kiNUgDME"
            bot.send_sticker(message.chat.id, sticker_file_id)
bot.polling()