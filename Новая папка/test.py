import telebot
import requests
import random

token = "7931021196:AAE8W9bmiAJU7aZIV5SbWrNG6W0EmaHnd4Y"

bot = telebot.TeleBot(token)

poke_api_url = "https://pokeapi.co/api/v2/pokemon/"

@bot.message_handler(commands=['start'])
def send_welcome(message):
   bot.reply_to(message,
                "Привет! Я бот, который отправляет картинку и информацию о случайном покемоне. Напиши мне /pokemon, чтобы получить информацию о покемоне.")

@bot.message_handler(commands=['pokemon'])
def send_pokemon_info(message):
    # получаем случайный номер покемона
    poke_id = random.randint(1, 898)
    url = poke_api_url + str(poke_id)
    response = requests.get(url)
    data = response.json()
    if "sprites" in data and "front_default" in data["sprites"]:
        poke_name = data["name"].capitalize()
        poke_image_url = data["sprites"]["front_default"]
        poke_info = f"{poke_name}\n\n"
        poke_info += f"Типы: "
        for poke_type in data["types"]:
            poke_info += f"{poke_type['type']['name'].capitalize()} "
        bot.send_photo(message.chat.id, poke_image_url, caption=poke_info)
    else:
        bot.reply_to(message, "Извините, я не могу найти информацию о покемоне.")

@bot.message_handler(func=lambda message: True)
def send_pokemon_info_by_name(message):
    pokemon_name = message.text.lower()
    url = poke_api_url+f'{pokemon_name}/'
    response = requests.get(url)
    if response.status_code == 200:
        pokemon_info = response.json()
        pokemon_image_url = pokemon_info['sprites']['front_default']
        pokemon_types = [type_info['type']['name']for type_info in pokemon_info['types']]
        message_text = f"Имя покемона: {pokemon_name}\nТипы: {', '.join(pokemon_types)}"
        bot.send_photo(chat_id=message.chat.id, photo=pokemon_image_url,    caption=message_text)
    else:
        bot.reply_to(message, f'Покемон с именем "{pokemon_name}" не найден')

bot.polling()