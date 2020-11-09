import mysql.connector


class connect():
    mysql = mysql.connector.connect(
        host="148.251.68.245",
        user="skole",
        database="skole"
    )
    curs = mysql.cursor()

    def ADD(self, val):
        global curs
        sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
        curs.execute(sql, val)

    def DELETE(self, name):
        sql = "DELETE FROM customers WHERE name = " + name
        curs.execute(sql)

    def MODIFY(self, input, name):
        sql = "UPDATE customers SET address = " + input + " WHERE address = " + name
        curs.execute(sql)

    def confirm(self):
        mysql.commit()
