from telebot import TeleBot, types
import random
import requests
from urllib.parse import quote_plus


BOTTOKEN = "8204900068:AAGlF9MqLAK4xgBgKZxtG4GE6aM87FhLD2U"

bot = TeleBot(BOTTOKEN) #связь с ботом

@bot.message_handler(commands=['img'])
def sendImg(m):
    prompt = m.text.partition(' ')[2].strip() #чисты запрос после пробела
    bot.send_message(m.chat.id, "Ищу...")
    #генерим рандомное число
    seed = random.randint(0, 2_000_000_000)
    print(seed)
    # улучшение запроса
    q = quote_plus(f"{prompt}, high quality, very detailed, soft light")

    url = f"https://image.pollinations.ai/prompt/{q}?width=500&height=500&seed={seed}&n=1"
    res = requests.get(url, timeout=90, allow_redirects=True)
    bot.send_photo(m.chat.id, res.content)

bot.infinity_polling()