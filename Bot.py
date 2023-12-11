#1
import telebot
from telebot import types
import os
#2
TOKEN = os.getenv('TELEGRAM_BOT_API_ID')
bot = telebot.TeleBot(TOKEN)
#3
user_saved_messages = {}
#4
main_menu = types.InlineKeyboardMarkup()
main_menu.row(types.InlineKeyboardButton("🙋‍♂️ Aʙᴏᴜᴛ Mᴇ", callback_data="callback_about_me"),
                (types.InlineKeyboardButton("🗃️ Oᴛʜᴇʀs", callback_data="project_button")))


about_me = types.InlineKeyboardMarkup()
about_me.row(types.InlineKeyboardButton("📷 Iɴsᴛᴀɢʀᴀᴍ", url="https://instagram.com/jinxx6_6?igshid=MzNlNGNkZWQ4Mg=="))
about_me.row(types.InlineKeyboardButton("🚀 Tᴇʟᴇɢʀᴀᴍ", url="https://t.me/Jinxx6_6_real_1"),
                          (types.InlineKeyboardButton("🚀 Tᴇʟᴇɢʀᴀᴍ 2", url="https://t.me/Crystal_Person")))
about_me.row(types.InlineKeyboardButton("🔙 Bᴀᴄᴋ", callback_data="back_button"))


project_others_menu= types.InlineKeyboardMarkup()
project_others_menu.row(types.InlineKeyboardButton("🧬 Eɴᴛɪᴛʏ Aʟʟ Bʟᴏᴄᴋ", url="https://t.me/freefirecraftlandgroup/146275"),
                    (types.InlineKeyboardButton("🔥 Aʟʟ Bʟᴏᴄᴋs", url="https://youtu.be/2C6DFikY0Bw?si=pZAEvYitBJQsYFZJ")))             
project_others_menu.row(types.InlineKeyboardButton("🛠️ Cᴏɴғɪɢ", url="https://t.me/freefirecraftlandgroup/151681"))
project_others_menu.row(types.InlineKeyboardButton("🔙 Bᴀᴄᴋ", callback_data="back_button"))


#5
@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    if chat_id not in user_saved_messages:
        user_saved_messages[chat_id] = []

    delete_all_saved_messages(chat_id)
    save_message = bot.send_message(chat_id, '/🏠 Mᴀɪɴ Mᴇɴᴜ', reply_markup=main_menu)
    user_saved_messages[chat_id].append(save_message.message_id)
    bot.delete_message(chat_id=chat_id, message_id=message.message_id)

#6
@bot.callback_query_handler(func=lambda call: call.data == "project_button")
def project_button_callback(call):
    try:
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                          text="/🗃️ Oᴛʜᴇʀs", reply_markup=project_others_menu)
    except Exception as e:
        print(f"Error {e}")
        
#7
@bot.callback_query_handler(func=lambda call: call.data == "back_button")
def back_button_callback(call):
    try:
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                          text="/🏠 Mᴀɪɴ Mᴇɴᴜ", reply_markup=main_menu)
    except Exception as e:
        print(f"Error {e}")
                               
#8                         
@bot.message_handler(func=lambda message: message.text != "/start", content_types=['text'])
def handle_unknown(message):
    try:
        chat_id = message.chat.id
        if chat_id not in user_saved_messages:
            user_saved_messages[chat_id] = []
        delete_all_saved_messages(chat_id)
        sticker_file_id = "CAACAgUAAxkBAAEn47VlY6Q_MPqgRtZnGGpc36FeN7TJJwACyQwAAmj_IFcsiFi0kiNUgDME"
        save_message = bot.send_sticker(message.chat.id, sticker_file_id)
        user_saved_messages[chat_id].append(save_message.message_id)
        bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    except Exception as e:
        print(f"Error {e}")
        
#9
@bot.callback_query_handler(func=lambda call: call.data == "callback_about_me")
def project_button_callback2(call):
    try:
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                          text="/🙋‍♂️ Aʙᴏᴜᴛ Mᴇ", reply_markup=about_me)
    except Exception as e:
        print(f"Error {e}")

#10
@bot.message_handler(func=lambda message: True)
def handle_started(message):
    try:
        bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    except Exception as e:
        print(f"Error {e}")
        
        
#11
def delete_all_saved_messages(chat_id):
    if chat_id in user_saved_messages:
        for msg_id in user_saved_messages[chat_id]:
            try:
                bot.delete_message(chat_id, msg_id)
            except Exception as e:
                print(f"Error deleting message ID {msg_id}: {e}")
        user_saved_messages[chat_id].clear()
    
#12    
bot.polling()