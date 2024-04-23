import telebot

bot = telebot.TeleBot('7161237552:AAFwmzqnQn-agiq5s_VXUDWN9qwPP5gASCw')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет! Ван Цзыхао')

@bot.message_handler(commands=['main'])
def main(message):
    bot.send_message(message.chat.id, 'Привет! На Лунпу') #ikhjgjklhiko

bot.polling(non_stop=True)  # kihohoirtwegujgh