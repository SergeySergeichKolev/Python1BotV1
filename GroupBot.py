from telebot import TeleBot, types


BOTTOKEN = "8204900068:AAGlF9MqLAK4xgBgKZxtG4GE6aM87FhLD2U"


badword = "марк кирилл матвей арсений Марк Кирилл Матвей"

bot = TeleBot(BOTTOKEN) #связь с ботом


@bot.message_handler(func=lambda m: True, content_types=['text'])
def control(m: types.Message):
    if m.text == "а чо чо э":
       bot.send_message(m.chat.id, 'ничо')


bot.infinity_polling()