import mysql.connector


class database:
    #Starter en forbindelse til mysql databasen og opretter tabellen der er bruges.
    def __init__(self):
        self.mysql = mysql.connector.connect(host="148.251.68.245", user="skole", database="skole")
        self.curs = self.mysql.cursor(buffered=True)

        self.dict = {
            "name": 0,
            "dato": 1
        }

        self.curs.execute("SHOW TABLES")
        tables = self.curs.fetchall()
        if ('customers',) not in tables:
            self.curs.execute(
                "CREATE TABLE customers (name VARCHAR(255), dato VARCHAR(255))")

        #Udfør en database interaktion og "commit"er den.
    def _do(self, cmd: str, val: tuple = None):
        if val is None:
            self.curs.execute(cmd)
        else:
            self.curs.execute(cmd, val)

        if val != {"nocom": "yeet"}:
            self.mysql.commit()
        #Tilføjer en række til tabellen med navn og dato
    def add(self, navn: str, dato: str):
        add = "INSERT INTO customers (name, dato) VALUES (%s, %s)"
        val = (navn, dato)
        self._do(add, val)

        #Sletter en række fra tabellen, her kan du vælge hvilken data i rækken du søger efter med place variablen
    def delete(self, ting: str, place: str = "name"):
        delete = "DELETE FROM customers WHERE {place} = '{ting}'"
        self._do(delete.format(ting=ting, place=place))

        #Henter en række fra tabellen, her kan du vælge hvilken data i rækken du søger efter med place variablen
    def pull(self, hvad: str, ting: str = "name"):
        pull = "SELECT * FROM customers"
        self._do(pull.format(name=ting), {"nocom": "yeet"})
        row = self.curs.fetchone()

        while row is not None:
            if row[self.dict.get(ting)] == hvad:
                return row
            else:
                row = self.curs.fetchone()

        #Henter alle rækker i tabellen
    def pullall(self):
        pull = "SELECT * FROM customers"
        self._do(pull)
        all = self.curs.fetchall()
        return all

        #Ændre en værdi i en bestemt række.
        # Er data'en du søger efter.
        # replace er det som du godt vil ændre den gamle værdi til.
        # whatchange bestemmer hvilken værdi i rækken du ændre.
        # whatsearch bestemmer hvilken værdi i rækken du søger efter.
    def modify(self, search: str, replace: str, whatchange: str = "dato", whatsearch: str = "name"):
        result = self.pull(search, whatsearch)
        yeet = "" + result[self.dict.get(whatchange)]
        modify = "UPDATE customers SET {change} = '{replace}' WHERE {change} = '{ree}'"
        self._do(modify.format(change=whatchange, replace=replace, ree=yeet))

        #Lukker forbindelsen til databasen
    def close(self):
        self.mysql.close()

        #Genåbner forbindelsen til databasen
    def connect(self):
        self.mysql.connect()
