import mysql.connector


class database:
    def __init__(self):
        self.mysql = mysql.connector.connect(host="148.251.68.245", user="skole", database="skole")
        self.curs = self.mysql.cursor()

        self.curs.execute("SHOW TABLES")
        tables = self.curs.fetchall()
        if ('customers',) not in tables:
            self.curs.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

    def add(self, navn, dato):
        add = "INSERT INTO customers (name, address) VALUES (%s, %s)"
        val = (navn, dato)
        self.curs.execute(add, val)
        self.mysql.commit()

    def delete(self, name):
        delete = "DELETE FROM customers WHERE name = '{0}'"
        self.curs.execute(delete.format(name))
        self.mysql.commit()

    def modify(self, oldName, newName):
        modify = "UPDATE customers SET name = '{newName}' WHERE name = '{oldName}'"
        self.curs.execute(modify.format(oldName=oldName, newName=newName))
        self.mysql.commit()

    def close(self):
        self.mysql.close()

    def connect(self):
        self.mysql.connect()
