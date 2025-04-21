import telebot
import requests
import random

token = "7931021196:AAE8W9bmiAJU7aZIV5SbWrNG6W0EmaHnd4Y"


bot = telebot.TeleBot(token)

poke_api_url = "https://pokeapi.co/api/v2/pokemon/"

@bot.message_handler(commands=['start'])
def start_mes(message):
    bot.send_message(message.chat.id, f'Этот сервис позволяет легко получить информацию о покемонах, их способностях и типах')

@bot.message_handler(commands=['pokemon'])
def pokemon(message):
    pokemon_id = random.randint(1,1302) #898
    main_url = poke_api_url + str(pokemon_id)
    res = requests.get(url=main_url)
    data = res.json()
    if 'sprites' in data and 'front_default' in data['sprites']:
        poke_img = data['sprites']['front_default']
        poke_name = data['name']
        popke_id = data['id']
        poke_lvl = data['base_experience']
        poke_types = f''
        for i in data['types']:
            poke_types += f'{i['type']['name']} '
        poke_info = f'''Имя покемона: {poke_name},
Id: {popke_id},
Lvl: {poke_lvl}
Типы: {poke_types}
'''
        bot.send_photo(message.chat.id, poke_img, caption=poke_info)
    else:
        bot.send_message(message.chat.id, text="Я не могу найти информацию о покемоне")

@bot.message_handler(func=lambda message: True)
def pokemon_poisk(message):
    pokemon_name = message.text.lower()
    main_url = poke_api_url + pokemon_name + '/'
    res = requests.get(url=main_url)
    if res.status_code == 200:
        data = res.json()
        if 'sprites' in data and 'front_default' in data['sprites']:
            poke_img = data['sprites']['front_default']
            poke_name = data['name']
            popke_id = data['id']
            poke_lvl = data['base_experience']
            poke_types = f''
            for i in data['types']:
                poke_types += f'{i['type']['name']} '
            poke_info = f'''
Имя покемона: {poke_name},
Id: {popke_id},
Lvl: {poke_lvl}
Типы: {poke_types}
'''
        bot.send_photo(message.chat.id, poke_img, caption=poke_info)
    else:
        bot.send_message(message.chat.id, text="Я не могу найти информацию о покемоне")

bot.polling()