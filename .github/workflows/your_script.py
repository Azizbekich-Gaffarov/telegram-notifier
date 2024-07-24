import telebot

# Bot token
TOKEN = '6990013831:AAHGmV1TnIN6SrfEb6nR6SiQ57bfg4SHmBc'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Xush kelibsiz! Bu bot har kuni ishga tushiriladi.")

# Other bot handlers...

bot.polling()
