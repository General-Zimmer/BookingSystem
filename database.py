import mysql.connector


class database:
    def __init__(self):
        self.mysql = mysql.connector.connect(host="148.251.68.245", user="skole", database="skole")
        self.curs = self.mysql.cursor()

        self.curs.execute("SHOW TABLES")
        tables = self.curs.fetchall()
        if ('customers',) not in tables:
            self.curs.execute(
                "CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

    def __do(self, cmd: str, val: tuple = None):
        if val is None:
            self.curs.execute(cmd)
        else:
            self.curs.execute(cmd, val)
        self.mysql.commit()

    def add(self, navn: str, dato: str):
        add = "INSERT INTO customers (name, address) VALUES (%s, %s)"
        val = (navn, dato)
        self.__do(add, val)


    def delete(self, name: str):
        delete = "DELETE FROM customers WHERE name = '{0}'"
        self.__do(delete.format(name))


    def modify(self, oldName: str, newName: str):
        modify = "UPDATE customers SET name = '{newName}' WHERE name = '{oldName}'"
        self.__do(modify.format(oldName=oldName, newName=newName))

    def close(self):
        self.mysql.close()

    def connect(self):
        self.mysql.connect()
