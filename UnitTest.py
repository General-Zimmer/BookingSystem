import database
import unittest





class DatabaseTests(unittest.TestCase):
    def setUp(self):
        self.sql = database.connect()

    def test_add_remove(self):
        self.sql.add("Yes", "test")
        self.sql.confirm()
        self.sql.modify("Yes", "no")
        self.sql.confirm()
        self.sql.delete("no")
        self.sql.confirm()



    def tearDown(self):
        pass
