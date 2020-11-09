import main
import database
import unittest
import mysql.connector

ma = main

sql = database.connect()


class DatabaseTests(unittest.TestCase):

    def test_getAverage(self):
        pass


ma.win()
