import telebot

bot = telebot.TeleBot('7161237552:AAFwmzqnQn-agiq5s_VXUDWN9qwPP5gASCw')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет!')


bot.polling(non_stop=True)