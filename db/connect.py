from peewee import *

def connect(path):
    connect = SqliteDatabase(path)
    if (connect):
        print('good')
        return connect
    else:
        print('bad')
        return

        
conn = connect('Chinook_Sqlite.sqlite')