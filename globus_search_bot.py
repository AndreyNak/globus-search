import config
import telebot
from telebot import types
from main import *
from controllers.controller_type import ControllerTypeGoods
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
    elif (check_item(message_user)):
        message.text = check_item(message_user)
        show_type_goods(message)
    #print(check_item(message))
    # else:
    #     bot.send_message(message.chat.id, 'Ничего не найдено ☹')


def show_map(message):
    bot.send_photo(message.chat.id,
     photo=open('photos/map/map.jpg', 'rb'))


def show_type_goods(message):
    obg = ControllerTypeGoods(message.text)
    bot.send_photo(message.chat.id,
     photo=open(obg.show_item(), 'rb'))

def check_item(message):
    obg = ControllerTypeGoods()
    return [i for i in obg.select_items() if i.find(message)!= - 1]   
    

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
        add(message, name_type, path)






def add(message,name_type, path):
    obg = ControllerTypeGoods(name_type)
    obg.add_item(path)
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
        msg = bot.send_message(message.chat.id, 'Ну напиши ты что нибудь !')
        bot.register_next_step_handler(msg, update)
        return
    else:
        # obg = ControllerTypeGoods(name_type)
        # #log = obg.delete_item()
        # obg.update_search_item()
        # obg.update_complite_item()
        bot.send_message(message.chat.id, '{!В разработке!}')



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

