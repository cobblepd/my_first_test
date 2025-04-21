# my_first_test
я впервые пользуюсь гитхабом
### flofllf
## flpsdaklpof[sa
# kdlogk;ldfg
#### xml;gkd;lx
##### jgfkljdglik
```
import telebot

bot = telebot.TeleBot('YOUR_BOT_TOKEN')  # 👉 сюда вставь свой токен

# Характеристики питомца
name = 'Капибара'
energy = 70
satiety = 10
happiness = 100

# 👉 TODO: Напиши функцию кормления питомца
def feed():
    global satiety, energy
    # Увеличь сытость и энергию питомца
    return f'Вы покормили {name}!'

# 👉 TODO: Напиши функцию игры с питомцем
def play():
    global satiety, energy, happiness
    # Измени характеристики питомца после игры
    return f'Вы поиграли с {name}!'

# 👉 TODO: Напиши функцию сна питомца
def sleep():
    global satiety, energy, happiness
    # Обнови характеристики питомца после сна
    return f'{name} поспал.'

# 👉 TODO: Напиши обработку команды /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Привет! Это твой питомец {name}.')

# 👉 TODO: Добавь обработку команд /feed, /play, /sleep
# Пример:
# @bot.message_handler(commands=['feed'])
# def handle_feed(message):
#     bot.send_message(message.chat.id, feed())

# Запуск бота
bot.polling()

```
