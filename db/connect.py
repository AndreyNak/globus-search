from peewee import *
import os

def connect():
    conn = 'db/globus_database.db'
    if os.path.isfile(conn):
        print('good')
        return SqliteDatabase(conn)
    else:
        print('bad')
        exit()
