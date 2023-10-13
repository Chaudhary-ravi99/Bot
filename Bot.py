
import logging
import time

from telegram import ForceReply, Update, InlineKeyboardButton, InlineKeyboardMarkup, Bot, helpers
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters, Updater
# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)
SO_COOL = "so-cool"

# Define a few command handlers. These usually take the two arguments update and
# context.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
    '𝗜𝗗𝗦 𝗕𝗬 𝗗𝗘𝗠𝗢𝗡 𝗦𝗨𝗕𝗗𝗨𝗘𝗥 𝗬𝗧',
    reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton(text='Aʟʟ Bᴜɴᴅʟᴇ/ᴏᴜᴛғɪᴛ Iᴅ', url='https://t.me/freefirecraftland/71')],
        [InlineKeyboardButton(text='Gᴜɴ Sᴋɪɴ Iᴅ/ᴡᴇᴀᴘᴏɴ Iᴅ', url='https://t.me/freefirecraftland/14')],
        [InlineKeyboardButton(text='Aʟʟ Eᴍᴏᴛᴇ Iᴅ', url='https://t.me/freefirecraftland/7')],
        [InlineKeyboardButton(text='Oʙᴊᴇᴄᴛ Iᴅ', url='https://t.me/freefirecraftland/11')],
    ])
)
    chat_id = update.message.chat_id
    message_id = update.message.message_id - 1
    await context.bot.delete_message(chat_id=chat_id, message_id=message_id)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("I AM JARVIS")
    chat_id = update.message.chat_id
    message_id = update.message.message_id - 1
    await context.bot.delete_message(chat_id=chat_id, message_id=message_id)
    
    



async def id(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None: 
  
    chat_id = update.message.chat_id
    user_message1 = update.message.text.lower()
    user = update.message.from_user
    username = user.username
    user_name = user.first_name
    keywords = ["id", "skin", "weapon", "gun skin", "emote", "object", "bundle", "outfit"]
    if any(keyword in user_message1 for keyword in keywords):
        # Build the message text
        message_text = f"@{username}:\n\n" if username else f"@{user_name}: "
        message_text += "IDs By Demon Subduer YT(@cloudxyz69)\r\nAll Bundle/Outfit ID\r\nhttps://t.me/freefirecraftland/71\r\nGun Skin ID/Weapon ID\r\nhttps://t.me/freefirecraftland/14\r\nAll Emote ID\r\nhttps://t.me/freefirecraftland/7\r\nObject ID\r\nhttps://t.me/freefirecraftland/11"
        await update.message.reply_text(
    '𝗜𝗗𝗦 𝗕𝗬 𝗗𝗘𝗠𝗢𝗡 𝗦𝗨𝗕𝗗𝗨𝗘𝗥 𝗬𝗧',
    reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton(text='Aʟʟ Bᴜɴᴅʟᴇ/ᴏᴜᴛғɪᴛ Iᴅ', url='https://t.me/freefirecraftland/71')],
        [InlineKeyboardButton(text='Gᴜɴ Sᴋɪɴ Iᴅ/ᴡᴇᴀᴘᴏɴ Iᴅ', url='https://t.me/freefirecraftland/14')],
        [InlineKeyboardButton(text='Aʟʟ Eᴍᴏᴛᴇ Iᴅ', url='https://t.me/freefirecraftland/7')],
        [InlineKeyboardButton(text='Oʙᴊᴇᴄᴛ Iᴅ', url='https://t.me/freefirecraftland/11')],
    ])
)
        chat_id = update.message.chat_id
        message_id = update.message.message_id + -1
        await context.bot.delete_message(chat_id=chat_id, message_id=message_id)
        
        
        
           
            
      
      
    chat_id = update.message.chat_id
    user_message1 = update.message.text.lower()
    user = update.message.from_user
    username = user.username
    user_name = user.first_name
    keywords2 = ["hello"]
    if any(keyword in user_message1 for keyword in keywords2):
        # Build the message text
        message_text = f"@{username}:\n\n" if username else f"@{user_name}: "
        message_text += "Hi!"

        # Send the message
        await context.bot.send_message(chat_id=chat_id, text=message_text)
        chat_id = update.message.chat_id
        message_id = update.message.message_id - 1
        await context.bot.delete_message(chat_id=chat_id, message_id=message_id)     
        
        chat_id = update.message.chat_id
    user_message1 = update.message.text.lower()
    user = update.message.from_user
    username = user.username
    user_name = user.first_name
    keywords2 = ["love"]
    if any(keyword in user_message1 for keyword in keywords2):
        # Build the message text
        message_text = f"@{username}:\n\n" if username else f"@{user_name}: "
        # Send the message
        chat_id = update.effective_chat.id
        sticker_id = 'CAACAgUAAxkBAAEmk0FlHjFhcUKErRxH30VaXH2PMQ5fgAACcQoAAlDfeVRa-woE0sm4XDAE'
        await context.bot.send_sticker(chat_id=chat_id, sticker=sticker_id, reply_to_message_id=update.message.message_id)
        chat_id = update.message.chat_id
        message_id = update.message.message_id - 1
        await context.bot.delete_message(chat_id=chat_id, message_id=message_id)     
        
        

        

    
def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token("6649947167:AAE3STTAdoZ8Gp5neg8HNLm-I5oIe84YPBM").build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("clear", id))
    application.add_handler(CommandHandler("id", id))

    
    
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, id))
    
 
    
    


    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
