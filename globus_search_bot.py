#import config
import telebot
from main import *
from controllers.controller_type import ControllerTypeGoods
conn = Con.connect()
Con.m_cursor(conn)
from db.models.base_model import *

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


firstTime = []

def update(message):
    name_type = message.text
    firstTime.append(name_type)
    try:
       artistId = Types.get(Types.type == firstTime[0])
    except:
        firstTime.pop()
        bot.send_message(message.chat.id, f'Тип с названием {name_type} \n - не существует !')
        return
    try: 
       ("key" == firstTime[1])
    except Exception:
     firstTime.append("key")
     bot.send_message(message.chat.id, 
         'Имя нового товара')
     bot.register_next_step_handler(message, update)
    else:
        firstTime.clear()
        artist = Types(type=name_type)
        artist.id = artistId.id
        artist.save()
        bot.send_message(message.chat.id, f'Тип с названием {name_type} \n - был добавлен в базу !')
     

# bot.enable_save_next_step_handlers(delay=2)
# bot.load_next_step_handlers()

bot.polling()
conn.close()

