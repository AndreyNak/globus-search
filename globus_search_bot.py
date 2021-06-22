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


def update(message):
    name_type = message.text
    ogb = ControllerTypeGoods(name_type)
    
    firstTime = []
    
    firstTime.append(name_type)
    

    if (len(firstTime) > 2):
    
    
     print(firstTime)
     firstTime.append(name_type) #добавляет приходящее имя в массив
     artistId = Types.get(Types.type == firstTime[0])
     new_word = firstTime[1]
     artist = Types(type=new_word)
     artist.id = artistId.id
     artist.save()
     bot.send_message(message.chat.id, f'Тип с названием {name_type} \n - не существует !')

     return
     
   # elif (firstTime == []): #если пустой массив
  #   firstTime.append(name_type) #добавляет приходящее имя в массив
     

    
#    if (firstTime != []): # если не пустой массив
   # firstTimeIn = firstTime.index(name_type) #получает индекс
#    if (type(firstTimeIn) != int): #если тип индекса = не инт
#          input("no")
#        
#    try:
#
#        artist = Types.get(Types.type == name_type )
#    except:
#        
#        bot.send_message(message.chat.id, f'Тип с названием {name_type} \n - не существует !')
#        return
  #  try:
#
 #      artistID = Types.get(Types.type == name_type )
  #  except Exception:
        
  #      artist = Types(type=name_type)
  #      artist.save()
 #       bot.send_message(message.chat.id, f'Тип с названием {name_type} \n - был добавлен в базу !')
        
  #  else:
       # delete = Types.get(Types.type == name_type )
       # delete.delete_instance()
  #  ogb.update_search_item(firstTime[1], firstTime[0])
    msg = bot.send_message(message.chat.id, 
         'Имя нового товара')
    bot.register_next_step_handler(msg, update)

# bot.enable_save_next_step_handlers(delay=2)
# bot.load_next_step_handlers()

bot.polling()
conn.close()

