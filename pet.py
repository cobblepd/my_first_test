from telebot import types
import telebot
import time 
import random 



token = "7931021196:AAE8W9bmiAJU7aZIV5SbWrNG6W0EmaHnd4Y"
bot = telebot.TeleBot(token)

name = "лягушенок Пепе"
energy = 100
health = 50
happiness = 100


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,
                     f"Привет! Тебе поручили ухаживать за лягушенком Пепе, пока его родители в отъезде! "
                     f"Ты можешь покормить его (/feed), поиграть (/play), и уложить спать (/sleep).")
    bot.send_photo(message.chat.id,
                   "https://i.pinimg.com/736x/1e/7b/9f/1e7b9f88c0f1e5328a0ccdac44aecd62.jpg",
                   caption=f"Энергия: {energy}, Здоровье: {health}, Радость: {happiness}")
    bot.send_message(message.chat.id, "Что ты хочешь сделать? /feed /play /sleep")


@bot.message_handler(commands=['feed'])
def handle_feed(message):
    global energy, health, happiness
    energy += 5
    health += 10
    happiness += 2
    check_stats(message)
    photo_url = "https://pbs.twimg.com/media/FG2R7fwXwAQa-u-.jpg"
    bot.send_photo(message.chat.id, photo_url, caption=f"{name} поел!")
    bot.send_message(message.chat.id, f"{name} накормлен! Энергия: {energy}, Здоровье: {health}, Радость: {happiness}")


@bot.message_handler(commands=['play'])
def handle_play(message):
    global energy, health, happiness
    energy -= 10
    health -= 3
    happiness += 15
    check_stats(message)
    photo_url = "https://sun9-39.userapi.com/impf/65rxzq80KbEixjgc-FZc-tyKvGE_vviRxU-tcQ/pTwvr2B2UTs.jpg"
    bot.send_photo(message.chat.id, photo_url, caption=f"{name} поиграл!")
    bot.send_message(message.chat.id, f"{name} поиграл! Энергия: {energy}, Здоровье: {health}, Радость: {happiness}")


@bot.message_handler(commands=['sleep'])
def handle_sleep(message):
    global energy, health, happiness
    energy += 20
    health += 5
    happiness -= 5
    check_stats(message)
    bot.send_message(message.chat.id, f"{name} поспал! Энергия: {energy}, Здоровье: {health}, Радость: {happiness}")


def check_stats(message):
    global energy, health, happiness
    if health <= 0:
        bot.send_message(message.chat.id, f"{name} умер от голода. Не забывайте кормить питомца!")
    elif health >= 100:
        bot.send_message(message.chat.id, f"{name} наелся и счастлив!")

    if happiness < 0:
        bot.send_message(message.chat.id, f"{name} умер от тоски. С лягушенком нужно чаще играть!")
    elif happiness > 100:
        bot.send_message(message.chat.id, f"{name} счастлив как никогда")

    if energy < 0:
        bot.send_message(message.chat.id, f"{name} умер от недостатка энергии.")
    elif energy > 100:
        bot.send_message(message.chat.id, f"{name} полон сил и энергии!!")


bot.polling()
