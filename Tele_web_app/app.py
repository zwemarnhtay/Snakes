from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CallbackContext, CommandHandler, MessageHandler, filters
from credentials import BOT_TOKEN, BOT_USERNAME
import json

async def launch_web_ui(update: Update, callback: CallbackContext):
    kb = [
        [KeyboardButton("Shopping here!", web_app=WebAppInfo("https://zwemarnhtay.github.io/Mini_Shopping/"))]
    ]
    await update.message.reply_text("Let's do this...", reply_markup=ReplyKeyboardMarkup(kb))
 
 #rf3

if __name__ == '__main__':
    # create the bot from the token:
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    # set a command listener for /start to trigger our Web UI
    application.add_handler(CommandHandler('start', launch_web_ui))

    print(f"Your bot is listening! Navigate to http://t.me/{BOT_USERNAME} to interact with it!")
    application.run_polling()
