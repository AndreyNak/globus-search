import config
import telebot
from telebot import types
from main import *
from controllers.controller_type import ControllerTypeGoods
from controllers.controller_categories import ControllerCategories
conn = Con.connect()
Con.m_cursor(conn)

bot = telebot.TeleBot(config.TOKEN)

# @bot.message_handler(commands=['start'])
# def wellcome(message):
#     rmk = types.ReplyKeyboardMarkup(resize_keyboard = True)
#     rmk.add(
#         types.KeyboardButton("Функции"),
#         types.KeyboardButton("Карта")
#         )
#     msg = bot.send_message(message.chat.id, 'Здарова прогеры, я крутой бот ! \nМеня создал гений.',
#      reply_markup=rmk)
#     bot.register_next_step_handler(msg, menu)


@bot.message_handler(commands=['start','help'])
def wellcome(message):
    bot.send_message(message.chat.id, """Здарова прогеры, я крутой бот ! Меня создал гений.\n
    Список команд: \n
    "Добавить" - Добавить элемен\n
    "Удалить" - Удалить элемент\n
    "Карта" - Показать карту глобуса\n
    "Здарова" - бот здоровается с тобой\n
    "<Название товара>" - показывает на карте где находится\n
    "<Фото-документ><Название>" - Добавить элемен\n
    """)




@bot.message_handler(content_types=['text'])
def menu(message):
    message_user = message.text.title()
    if (message_user == 'Добавить'):
        msg = bot.send_message(message.chat.id, 
        'Отправьте фото документом и подпишите, что бы добавить элемент')
        bot.register_next_step_handler(msg, photo_set)
    elif (message_user == 'Удалить'):
        msg = bot.send_message(message.chat.id, 
        'Напишите название типа товара, который хотите удалить')
        bot.register_next_step_handler(msg, delete)
    elif (message_user == 'Изменить'):
        msg = bot.send_message(message.chat.id, 
        'Напишите название типа товара, который хотите изменить')
        bot.register_next_step_handler(msg, update)
    elif (message_user == 'Карта'):
        bot.send_message(message.chat.id, 'Карта глобуса')
        show_map(message)
    elif (message_user == 'Здарова'):
        hello(message)
    elif (message_user == "Категория"):
        msg = bot.send_message(message.chat.id, 'Напиши название отдела')
        bot.register_next_step_handler(msg, select_type)
    elif (check_item(message_user)):
        message.text = check_item(message_user)
        show_type_goods(message)
    elif (check_item1(message_user)):
        message.text = check_item1(message_user)
        show_category_goods(message)
    #print(check_item(message))
    # else:
    #     bot.send_message(message.chat.id, 'Ничего не найдено ☹')

ControllerCategories

def select_type(message):
    message_user = message.text
    if check_item(message_user):
        print('True')
        msg = bot.send_message(message.chat.id, 'Отправьте документ и напишите название категории')
        bot.register_next_step_handler(msg, add_category, message_user)
    else:
        print('false')

def add_category(message, name_type):
    if message.document != None:
        if message.caption != None:
            print(message.caption)
            print(name_type)
            path =photo_set_category(message)
            obj = ControllerCategories(message.caption)
            obj.add_category_item(path,name_type)
            bot.send_message(message.chat.id, f'Категория с названием {message.caption} в отделение {name_type}\n - был добавлен в базу !')
        else:
            print('Нет подписи')
    else:
        print('Это не документ')
def show_map(message):
    bot.send_photo(message.chat.id,
     photo=open('photos/map/map.jpg', 'rb'))


def show_type_goods(message):
    obg = ControllerTypeGoods(message.text)
    type = obg.show_type()
    bot.send_photo(message.chat.id,
     photo=open(type.path, 'rb'))

def show_category_goods(message):
    obg = ControllerCategories(message.text)
    сategory = obg.select_category()
    obg1 = ControllerTypeGoods(сategory.name_type)
    type = obg1.show_type()
    str =f" Категория: <b>{сategory.name}</b>\n Отдел: <b>{сategory.name_type}</b>\n Крыло: <b>{type.side}</b>"
    bot.send_photo(
        message.chat.id, photo=open(сategory.path, 'rb'),
        caption=str, parse_mode="html"
        )

def check_item(message):
    obg = ControllerTypeGoods()
    return [i for i in obg.select_items() if i.find(message)!= - 1]

def check_item1(message):
    obg = ControllerCategories()
    return [i for i in obg.select_items1() if i.find(message)!= - 1]
    
    

def hello(message):
    bot.send_message(message.chat.id, f'Здарова {message.from_user.first_name}')

@bot.message_handler(content_types=['document'])
def photo_set(message):
    if (message.caption != None):
        name_type = message.caption
        raw = message.document.file_id
        path = raw+".jpg"
        file_info = bot.get_file(raw)
        downloaded_file = bot.download_file(file_info.file_path)
        with open("photos/"+path,'wb') as new_file:
            new_file.write(downloaded_file)
        msg = bot.send_message(message.chat.id, 'Какой крыло: ?')
        bot.register_next_step_handler(msg,add,name_type, path)


def photo_set_category(message):
        raw = message.document.file_id
        path = raw+".jpg"
        file_info = bot.get_file(raw)
        downloaded_file = bot.download_file(file_info.file_path)
        with open("photos/category/"+path,'wb') as new_file:
            new_file.write(downloaded_file)
        return path




def add(message,name_type, path):
    obg = ControllerTypeGoods(name_type)
    obg.add_item(path, message.text)
    print(message.text)
    bot.send_message(message.chat.id, f'Тип с названием {name_type} \n - был добавлен в базу !')
        

def delete(message):
    name_type = message.text.title()
    if (len(name_type)) < 1:
        msg = bot.send_message(message.chat.id, 'Ну напиши ты что нибудь !')
        bot.register_next_step_handler(msg, delete)
        return
    elif name_type == 'Выход':
        bot.send_message(message.chat.id, 'Вы вышлив в меню')
        return
    elif not check_item(name_type):
        msg = bot.send_message(message.chat.id, 'Товар не найден !')
        bot.register_next_step_handler(msg, delete)
        return
    obg = ControllerTypeGoods(name_type)
    obg.delete_item()
    bot.send_message(message.chat.id,'Экземпляр был успешно удален !')


def update(message):
    name_type = message.text
    if (len(name_type)) < 1:
        bot.send_message(message, 'Ну напиши ты что нибудь !')
        return
    else:
        obg = ControllerTypeGoods(name_type)
        obg.delete_item()
        msg = bot.send_message(message.chat.id, 
          'Имя нового товара')
        bot.register_next_step_handler(msg, add)



# def menu(message):
#     print(message.text)
#     msg = bot.send_message(message.chat.id, 'текст')
#     if message.text == 'Функции':
#         bot.register_next_step_handler(msg, functions)
#     elif message.text == 'Карта':
#         bot.register_next_step_handler(msg, show_map)



    #bot.send_message(message.chat.id, f'Здарова {message.from_user.first_name}')

# @bot.message_handler(content_types=['Функции'])
# def functions(message):
#     print('Метод functions !')
#     mk = types.ReplyKeyboardMarkup(resize_keyboard = True)
#     mk.add(
#         types.KeyboardButton("Добавить"),
#         types.KeyboardButton("Удалить")
#         )
#     msg = bot.send_message(message.chat.id, 'Добавить, Удалить запись. ',
#      reply_markup=mk)
#     bot.register_next_step_handler(msg, crud)





# bot.enable_save_next_step_handlers(delay=2)
# bot.load_next_step_handlers()
bot.polling()
conn.close()