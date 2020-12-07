import database
import lagic as lo
import datetime
import unittest



class LogicTests(unittest.TestCase):
    def setUp(self):
        self.res = lo.reservation("General Zimmer")

    def test_dato(self):
        self.assertEqual(self.res.dato("2000-12-20"), (2000, 12, 20))

    def test_time(self):
        self.assertEqual(self.res.time("12:45"), (12, 45))

    def test_final(self):
        self.assertEqual(self.res.final(2000, 12, 20, 12, 45), datetime.datetime(2000, 12, 20, 12, 45))

    def test_datetest(self):
        self.assertFalse(self.res.datetest(40, 21, "40", "21", "2000"))
        self.assertFalse(self.res.datetest(0.22, 0.512, "0.22", "0.512", "0.2000"))

    def test_timetest(self):
        self.assertFalse(self.res.timetest(16, 68, "12", "60"))
        self.assertFalse(self.res.timetest(0.12, 0.60, "0.12", "0.60"))

    def test_isspace(self):
        self.assertFalse(lo.is_string_with_space("weeeeee"))
        self.assertTrue(lo.is_string_with_space("weeeeee with space"))


    def tearDown(self):
        pass


class DatabaseTests(unittest.TestCase):
    def setUp(self):
        self.sql = database.database()

    #Da vi ikke ved hvordan vi kan teste hver database handling uden brugen af en add og delete, så valgte vi at lave
    #det hele i en test modul
    def test_all(self):
        self.sql.add("testing da test test", "yeet")
        self.sql.modify("testing da test test", "meat")
        row = self.sql.pull("testing da test test")
        self.assertEqual(row[1], "meat")

        self.sql.delete("testing da test test")

    def tearDown(self):
        self.sql.close()
