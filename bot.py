import pandas
from telebot import TeleBot, types
import threading   #потоки
from datetime import datetime
import time


BOTTOKEN = "8252586102:AAGW-X7uB83bIFJpUbm0QwmAO4hNYKfL6FE"

bot = TeleBot(BOTTOKEN) #связь с ботом

users = set() # множество id подписавшихся на уведомления


days_of_week = {
    1: "Понедельник",
    2: "Вторник",
    3: "Среда",
    4: "Четверг",
    5: "Пятница"
}



@bot.message_handler(commands=['start'])
def cmdStart(m):
    bot.send_sticker(m.chat.id, "CAACAgIAAxkBAAEPwBdpEqiSxlRd_H20g8brjTsUU9nWFAACBQADwDZPE_lqX5qCa011NgQ")
    bot.send_message(m.chat.id, "Приветсвую, я бот Колева Сергея \n"
                                "Используй команду /info для продолжения")


@bot.message_handler(commands=['info'])
def cmdInfo(m):
    klava1 = types.InlineKeyboardMarkup()
    klava2 = types.ReplyKeyboardMarkup()

    btn1 = types.InlineKeyboardButton("/notice", callback_data="notice")
    btn2 = types.InlineKeyboardButton("/unsub", callback_data="unsub")
    btn3 = types.InlineKeyboardButton("/image", callback_data="image")
    btn4 = types.InlineKeyboardButton("/parser", callback_data="parser")

    btn5 = types.KeyboardButton("/notice")
    btn6 = types.KeyboardButton("/unsub")
    btn7 = types.KeyboardButton("/image")
    btn8 = types.KeyboardButton("/parser")

    klava1.add(btn1, btn2, btn3, btn4)
    klava2.add(btn5, btn6, btn7, btn8)

    bot.send_message(m.chat.id, "Список команд 📎", reply_markup=klava1)
    bot.send_message(m.chat.id, "/start - приветственное сообщение\n"
                                "/info   - меню бота\n"
                                "/notice - подписаться на уведомления\n"
                                "/unsub  - отписаться от уведомлений\n"
                                "/image  - генератор изображений\n"
                                "/parser - подборка товаров электроники", reply_markup=klava2)


@bot.message_handler(commands=['notice'])
def cmdNotice(m):
    users.add(m.chat.id) #записали id в список на подписку уведомлений
    bot.send_message(m.chat.id, "Вы подписались на уведомления ✅")



@bot.message_handler(commands=['unsub'])
def cmdUnsub(m):
    users.discard(m.chat.id) #удаляете подписку на уведомления
    bot.send_message(m.chat.id, "Вы отписались на уведомления ❌")



def setNotification(user):
    today_weekday = datetime.today().weekday() + 1 #день недели в цифре 1-7

    if today_weekday == 6 or today_weekday == 7:
        bot.send_message(user, "Сегодня выходной. Занятий - НЕТ")

    df = pandas.read_excel("shedule.xlsx") #Эксель файл

    #все строки с расписанием на today weekday
    today_schedule = df[df['День'] == today_weekday]
    responce = f"Расписание на {days_of_week[today_weekday]}"

    for _, row in today_schedule.iterrows():
        responce += "▫️" * 20 + "\n"

        for column, value in row.items():
            if column != 'День' and pandas.notna(value) and str(value).strip() != '':
                column_name = column
                responce += f"{column_name}: {value}\n"

        responce += "\n" + "═" * 30 + "\n\n"

    total_lessons = len(today_schedule)
    responce += f"📊 Всего уроков: {total_lessons}"

    bot.send_message(user, responce)




def check_time():

    while True:
        now = datetime.now()
        # когда высылать уведомления
        if now.hour == 7 and now.minute == 30 or now.hour == 7 and now.minute == 0:
            for user in list(users):
                #отсылка в бота
                setNotification(user)
            time.sleep(65)
        else:
            time.sleep(10)


def notification():
    scheduler_thread = threading.Thread(target=check_time)
    scheduler_thread.daemon = True  # фоновый поток
    scheduler_thread.start()




if __name__ == "__main__":
    print("Бот запущен...")
    notification()          # Запуск фоновых уведомлений
    bot.infinity_polling()


#----------------------------------------------------------
#
# def isBtn2(c):
#     return c.data == 'btn2'
#
# @bot.callback_query_handler(func=lambda c: c.data == 'btn1')
# def doBtn1(c):
#     bot.send_message(c.message.chat.id, "Ответ на inline кнопку 1")
#
# @bot.callback_query_handler(func=isBtn2)
# def doBtn2(c):
#     bot.send_message(c.message.chat.id, "Ответ на inline кнопку 2")


#
# @bot.message_handler(commands=['start'])
# def cmdStart(m):
#     inlineKlava = types.InlineKeyboardMarkup()  #создает клаву
#
#     btn1 = types.InlineKeyboardButton("Test1", url="google.com")
#     btn2 = types.InlineKeyboardButton("Test2", callback_data='btn2')
#     btn3 = types.InlineKeyboardButton("Test3", callback_data='btn3')
#     btn4 = types.InlineKeyboardButton("Test4", callback_data='btn4')
#     inlineKlava.row(btn1,btn2)
#     inlineKlava.row(btn3, btn4)
#
#     bot.send_message(m.chat.id, "Бот стартовал", reply_markup=inlineKlava)





# @bot.message_handler(commands=['info'])
# def cmdInfo(m):
#     kl = types.ReplyKeyboardMarkup()
#     btn1 = types.KeyboardButton("Test1")
#     btn2 = types.KeyboardButton("Test2")
#     btn3 = types.KeyboardButton("Test3")
#     btn4 = types.KeyboardButton("Test4")
#     kl.add(btn1,btn2)
#     kl.add(btn3, btn4)
#     bot.send_message(m.chat.id, "Ответ", reply_markup=kl)


# !m.chat.id
#m.form_user.id - id пользователя
# !m.form_user.username - username в tg
#m.form_user.first_name -
#m.form_user.last_name
#m.form_user.language_code - язык
#m.location
#m.sticker
# !m.text
# photo
# document
#c!m.contact



