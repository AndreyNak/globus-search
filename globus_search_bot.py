from os import access
import time
import config
import telebot
from telebot import types
from main import *
from controllers.controller_type import ControllerTypeGoods
from controllers.controller_categories import ControllerCategories
from errors import *
import re
conn = Con.connect()
Con.m_cursor(conn)

bot = telebot.TeleBot(config.TOKEN)

access_list = [776211647, 130783085, 739889656]

@bot.message_handler(commands=['start','help'])
def wellcome(message):
    if message.from_user.id in access_list:
          bot.send_message(message.chat.id, """Здарова прогеры, я крутой бот ! Меня создал гений.\n
        Список команд: \n
        "Добавить" - Добавить элемен\n
        "Удалить" - Удалить тип товара\n
        "Удалить К" - Удалить категорию товара\n
        "Карта" - Показать карту глобуса\n
        "Здарова" - бот здоровается с тобой\n
        "Категория" - добавление категории\n
        "<Название товара>" - показывает на карте где находится\n
        "<Фото-документ><Название>" - Добавить элемен\n
        """)
    else:
        rmk = types.ReplyKeyboardMarkup(resize_keyboard = True)
        rmk.add(types.KeyboardButton("Карта"))
        bot.send_message(message.chat.id,"""Привет ! Я поисковой бот.\n
        Показываю тебе где находятся товары глобуса, которые ты напишешь мне.\n
        Напиши товар который ты хочешь увидеть.\n
        Например - Молоко.\n
        Используй кнопку или напиши Карта, что бы посмотреть в любой момент карту глобуса.
        """,reply_markup=rmk)




@bot.message_handler(content_types=['text'])
def menu(message):
    log(message, 'logs')
    message_user = first_char_upper(message.text.lower())
    if (message_user == 'Карта'):
        print(message_user)
        bot.send_message(message.chat.id, 'Карта глобуса')
        show_map(message)
    elif (check_category(message_user)):
        bot.send_message(message.chat.id, 'Показываю...')
        item = check_category(message_user)
        message.text = item.name
        show_category_goods(message)
    elif (check_type(message_user)):
        bot.send_message(message.chat.id, 'Показываю...')
        item = check_type(message_user)
        message.text = item.type
        show_type_goods(message)
    elif (message_user == 'Здарова'):
            hello(message)
    elif message.from_user.id in access_list:
        if (message_user == 'Добавить'):
            msg = bot.send_message(message.chat.id, 
            'Отправьте фото документом и подпишите, что бы добавить элемент')
            bot.register_next_step_handler(msg, photo_set)
        elif (message_user == 'Удалить'):
            msg = bot.send_message(message.chat.id, 
            'Напишите полностью название типа товара, который хотите удалить')
            bot.register_next_step_handler(msg, delete_type)
        elif (message_user == 'Изменить'):
            msg = bot.send_message(message.chat.id, 
            'Напишите название типа товара, который хотите изменить')
            bot.register_next_step_handler(msg, update)
        elif (message_user == 'Удалить к'):
            msg = bot.send_message(message.chat.id, 
            'Напишите полностью название категории товара, который хотите удалить')
            bot.register_next_step_handler(msg, delete_category)
        elif (message_user == "Категория"):
            msg = bot.send_message(message.chat.id, 'Напиши название отдела')
            bot.register_next_step_handler(msg, select_type)
    #     else:
    #         bot.send_message(message.chat.id, search_help(message_user))
    else:
        log(message, 'logs_not_found')
        bot.send_message(message.chat.id, search_help(message_user))
        



# def check_item(message):
#     obg = ControllerTypeGoods()
#     return [i for i in obg.select_items() if i.find(message)!= - 1]

# def check_item1(message):
#     obg = ControllerCategories()
#     return [i for i in obg.select_items1() if i.find(message)!= - 1]



def search_help(message):
    str = "Ничего не найдено ☹"
    word = message[:-2]
    obg = ControllerCategories()
    items = [i for i in obg.select_items1() if i.find(message)!= - 1]
    if len(message) > 3:
        smart_search = [i for i in obg.select_items1() if i.find(word)!= - 1]
        if(len(smart_search) > 0):
            elems = "Может вы имели ввиду: "+', '.join(smart_search)    
            return f"{str}\n {elems}" 
    elif len(message) < 3:
        items = [i for i in obg.select_items1() if i.find(message)!= - 1]
        if(len(items) > 0):
            elems = "Может вы имели ввиду: "+', '.join(items)    
            return f"{str}\n {elems}"            
    return str
 

def check_type(message):
    obg = ControllerTypeGoods(message)
    return obg.select_type()

def check_category(message):
    obg = ControllerCategories(message)
    return obg.select_category()


@bot.message_handler(content_types=['document'])
def add_set_category(message):
    if message.from_user.id in access_list:
        name = message.document.file_name
        print(name)
        if(valid_regular(name)):
            name = name.replace('+', " ")
            name_category, name_type  =  parse_name(name)
            if (check_type(name_type)):
                path = photo_set_category(message)
                obj = ControllerCategories(name_category)
                obj.add_category_item(path,name_type)
            else:
                print(f'{name_type} - Данного отдела НЕТ.')
        else:
            print(f'{name} Не прошел валидацию')

def parse_name(name):
    foudn = r'[А-Я]{1}[а-я0-9\s]+-[а-я-]+|[А-Я]{1}[а-я0-9\s]+'
    result =  re.findall(foudn, name)
    return  result[0],result[1]

def valid_regular(name):
    check = r'[А-Я]{1}[а-я0-9+]+_[А-Я]{1}[а-я+]+.png'
    result =  re.findall(check, name)
    return len(result) == 1

def first_char_upper(str):
    return str[:1].upper() + str[1:]

def show_type_goods(message):
    obg = ControllerTypeGoods(message.text)
    type = obg.select_type()
    bot.send_photo(message.chat.id,
     photo=open(type.path, 'rb'))

def show_category_goods(message):
    obg = ControllerCategories(message.text)
    сategory = obg.select_category()
    obg1 = ControllerTypeGoods(сategory.name_type)
    try:
        type = obg1.select_type()
        str =f" Категория: <b>{сategory.name}</b>\n Отдел: <b>{сategory.name_type}</b>\n Крыло: <b>{type.side}</b>"
        bot.send_photo(
            message.chat.id, photo=open(сategory.path, 'rb'),
            caption=str, parse_mode="html")
    except Exception:
         bot.send_message(
            message.chat.id, 'данный отдел еще не создан')

def photo_set_category(message):
        return ControllerCategories().load_photo(message,bot)
      

@bot.message_handler(content_types=['document'])
def photo_set(message):
    if (message.caption != None):
        name_type, path = ControllerTypeGoods().load_photo(message,bot)
        msg = bot.send_message(message.chat.id, 'Какое крыло: ?')
        bot.register_next_step_handler(msg, add_type, name_type, path)
    else:
        bot.send_message(message.chat.id, no_caption())



def add_type(message,name_type, path):
    obg = ControllerTypeGoods(name_type)
    obg.add_item(path, message.text)
    print(message.text)
    bot.send_message(message.chat.id, f'Тип с названием {name_type} \n - был добавлен в базу !')




def delete_type(message):
    user_message = message.text
    if user_message == 'Выход':
        bot.send_message(message.chat.id, 'Вы вышли в меню')
        return
    elif not check_type(user_message):
        msg = bot.send_message(message.chat.id, not_found())
        bot.register_next_step_handler(msg, delete_type)
        return
    obg = ControllerTypeGoods(user_message)
    obg.delete_item()
    bot.send_message(message.chat.id,'Экземпляр был успешно удален !')


def delete_category(message):
    message_user = message.text
    if message_user == 'Выход':
        bot.send_message(message.chat.id, 'Вы вышлив в меню')
        return
    elif not check_category(message_user):
        msg = bot.send_message(message.chat.id, not_found())
        bot.register_next_step_handler(msg, delete_category)
        return
    obg = ControllerCategories(message_user)
    obg.delete_item()
    bot.send_message(message.chat.id,'Экземпляр был успешно удален !')


def update(message):
    name_type = message.text
    obg = ControllerTypeGoods(name_type)
    obg.delete_item()
    msg = bot.send_message(message.chat.id, 
        'Имя нового товара')
    bot.register_next_step_handler(msg, add_type)




def add_category(message, name_type):
    if message.document != None:
        if message.caption != None:
            print(message.caption)
            print(name_type)
            path = photo_set_category(message)
            obj = ControllerCategories(message.caption)
            obj.add_category_item(path,name_type)
            bot.send_message(message.chat.id, f'Категория с названием {message.caption} в отделение {name_type}\n - был добавлен в базу !')
        else:
            bot.send_message(message.chat.id, no_caption())
    else:
        bot.send_message(message.chat.id, not_document())


def select_type(message):
    message_user = message.text
    if check_type(message_user):
        msg = bot.send_message(message.chat.id, 'Отправьте документ и напишите название категории')
        bot.register_next_step_handler(msg, add_category, message_user)
    else:
        bot.send_message(message.chat.id, not_found())




def show_map(message):
    bot.send_photo(message.chat.id,
     photo=open('photos/map/map.jpg', 'rb'))

def hello(message):
    bot.send_message(message.chat.id, f'Здарова {message.from_user.first_name}')

def get_time():
    seconds = time.time()
    return time.ctime(seconds)

def log(message,file_name):
    if (message.from_user.id not in access_list):
        try:
            file = open(f"logs/{file_name}.txt", "a")
            file.write(f"""
            id:{message.from_user.id}\n
            name:{message.from_user.first_name}\n
            username: {message.from_user.username}\n
            Text  : {message.text}\n
            Time: {get_time()}
            ====================================================================\n""")
            file.close()
        except UnicodeEncodeError:
            return

bot.polling()
conn.close()
