#import config
import telebot
from main import *
from controllers.controller_type import ControllerTypeGoods
conn = Con.connect()
Con.m_cursor(conn)

#bot = telebot.TeleBot(config.TOKEN)
token = "1850230832:AAED80DMUF-tcR50VP252HRaOh0mCAu02hM"

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def wellcome(message):
    bot.send_message(message.chat.id, 'Здарова прогеры, я крутой бот ! \nМеня создал гений')


@bot.message_handler(commands=['add','delete', 'update'])
def add_type(message):
    message_user = message.text
    if (message_user == '/add'):
        msg = bot.send_message(message.chat.id, 
        'Напишите название типа товара, который хотите добавить')
        bot.register_next_step_handler(msg, add)
    elif (message_user == '/delete'):
        msg = bot.send_message(message.chat.id, 
        'Напишите название типа товара, который хотите удалить')
        bot.register_next_step_handler(msg, delete)
    elif (message_user == '/update'):
        msg = bot.send_message(message.chat.id, 
        'Напишите название типа товара, который хотите изменить')
        bot.register_next_step_handler(msg, update)

def add(message):
    name_type = message.text
    if (len(name_type)) < 1:
        msg = bot.send_message(message, 'Ну напиши ты что нибудь !')
        bot.register_next_step_handler(msg, add)
        return
    else:
        obg = ControllerTypeGoods(name_type)
        obg.add_item()
        bot.send_message(message.chat.id, f'Тип с названием {name_type} \n - был добавлен в базу !')

def delete(message):
    name_type = message.text
    if (len(name_type)) < 1:
        msg = bot.send_message(message, 'Ну напиши ты что нибудь !')
        bot.register_next_step_handler(msg, delete)
        return
    else:
        obg = ControllerTypeGoods(name_type)
        log = obg.delete_item()
        bot.send_message(message.chat.id, log)   

def update(message):
    name_type = message.text
    if (len(name_type)) < 1:
        msg = bot.send_message(message, 'Ну напиши ты что нибудь !')
        bot.register_next_step_handler(msg, update)
        return
    else:
        # obg = ControllerTypeGoods(name_type)
        # #log = obg.delete_item()
        # obg.update_search_item()
        # obg.update_complite_item()
        bot.send_message(message.chat.id, '{!В разработке!}')


@bot.message_handler(content_types=['Здарова'])
def hello(message):
    bot.send_message(message.chat.id, f'Здарова {message.from_user.first_name}')

@bot.message_handler(commands=['show'])
def show(message):
    obj = ControllerTypeGoods()
    obj.show_items()
    bot.send_message(message.chat.id, )

@bot.message_handler(content_types=['text'])
def test(message):
    if 'тест222' in message.text.lower():
        bot.send_message(message.chat.id, 'Тест')

# bot.enable_save_next_step_handlers(delay=2)
# bot.load_next_step_handlers()

bot.polling()
conn.close()

