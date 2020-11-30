import database
import lagic as lo
import unittest



class LogicTests(unittest.TestCase):
    def setUp(self):
        self.res = lo.reservation("General Zimmer")

    def test_dato(self):
        self.assertEqual(self.res.dato("2000-12-20"), (2000, 12, 20))

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

    def test_modify(self):

        self.sql.add("yeeta", "test")

        self.sql.modify("yeeta", "efgea")


    def tearDown(self):
        self.sql.close()
