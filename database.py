import mysql.connector


class database:
    def __init__(self):
        self.mysql = mysql.connector.connect(host="148.251.68.245", user="skole", database="skole")
        self.curs = self.mysql.cursor()

        self.dict = {
            "name": 0,
            "dato": 1
        }

        self.curs.execute("SHOW TABLES")
        tables = self.curs.fetchall()
        if ('customers',) not in tables:
            self.curs.execute(
                "CREATE TABLE customers (name VARCHAR(255), dato VARCHAR(255))")

    def _do(self, cmd: str, val: tuple = None):
        if val is None:
            self.curs.execute(cmd)
        else:
            self.curs.execute(cmd, val)

        if val != {"nocom": "yeet"}:
            self.mysql.commit()

    def add(self, navn: str, dato: str):
        add = "INSERT INTO customers (name, dato) VALUES (%s, %s)"
        val = (navn, dato)
        self._do(add, val)

    def delete(self, ting: str, place: str = "name"):
        delete = "DELETE FROM customers WHERE {place} = '{ting}'"
        self._do(delete.format(ting=ting, place=place))

    def pull(self, hvad: str, ting: str = "name"):
        pull = "SELECT * FROM customers"
        self._do(pull.format(name=ting), {"nocom": "yeet"})
        row = self.curs.fetchone()

        while row is not None:
            if row[self.dict.get(ting)] == hvad:
                return row
            else:
                row = self.curs.fetchone()

    def modify(self, search: str, replace: str, whatchange: str = "dato", whatsearch: str = "name"):
        result = self.pull(search, whatsearch)
        yeet = result[self.dict.get(whatchange)]
        modify = "UPDATE customers SET {change} = '{replace}' WHERE {change} = '{replace}'"
        self.curs.execute(modify.format(change=yeet), replace=replace)

    def close(self):
        self.mysql.close()

    def connect(self):
        self.mysql.connect()
