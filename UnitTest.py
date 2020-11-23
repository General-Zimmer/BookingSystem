import database
import unittest



class LogicTests(unittest.TestCase):
    def setUp(self):
        pass

    def test_main(self):
        pass

    def tearDown(self):
        pass


class DatabaseTests(unittest.TestCase):
    def setUp(self):
        self.sql = database.database()


    def test_add(self):
        self.sql.add("Yes", "test")

        self.sql.modify("Yes", "no")


    def test_pull(self):
        self.sql.add("testing da test test", "yeet")
        row = self.sql.pull("testing da test test")
        self.assertEqual(row[2], "yeet")
        self.sql.delete("testing da test test")


    def tearDown(self):
        self.sql.close()
