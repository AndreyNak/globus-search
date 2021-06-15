from peewee import *
import os


class Con:
    def connect():
        db = 'db/globus_database.sqlite'
        if os.path.isfile(db):
            print('good')
            return SqliteDatabase(db)
        else:
            print('bad')
            exit()

    def m_cursor(conn):
        return conn.cursor()
