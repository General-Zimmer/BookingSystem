import database
import unittest
import main


class LogicTests(unittest.TestCase):
    def setUp(self):
        pass

    def test_main(self):
        pass

    def tearDown(self):
        pass


class DatabaseTests(unittest.TestCase):
    def setUp(self):
        self.sql = database.connect()

    def test_add_remove(self):
        self.sql.add("Yes", "test")
        self.sql.modify("Yes", "no")
        self.sql.delete("no")
        self.sql.confirm()

    def tearDown(self):
        self.sql.close()
