import datetime
import mysql.connector
import database


class test:
    def add_something(self):
        sql = database.connect()

        sql.add("weee", "yeet")


test().add_something()
