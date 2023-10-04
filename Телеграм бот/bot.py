import telebot

bot = telebot.TeleBot("6453355482:AAHI2l6Im9wUjtzQToISxNbVATXdgMsMlyQ")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Absolute?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.infinity_polling()