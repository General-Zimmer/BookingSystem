import datetime
import lagic as la
import database

res = la.reservation
isstring = la.is_string_with_space
sql = database.database()

print(datetime.datetime.now())
def data():
    navnset = False
    while navnset == False:
        print("Skriv navn")
        navn = str(input())
        print(isstring(navn))
        if isstring(navn) == True:
            res = res(navn)
            navnset = True

    datoset = False
    while datoset == False:
        print("Enter a date in YYYY-MM-DD format")
        dato = input()
        try:
            year, month, day, = res.dato(dato)
            stryear = str(year)
            strmonth = str(month)
            strday = str(day)
            datoset = res.datetest(month, day, strmonth, strday, stryear)
        except:
            pass

    timeset = False
    while timeset == False:
        print("Enter a time in HH:MM format")
        time = input()
        try:
            hour, minute = res.time(time)
            strmin = str(minute)
            strhour = str(hour)
            timeset = res.timetest(hour, minute, strhour, strmin)
        except:
            pass
    finaldate = str(res.final(year, month, day, hour, minute))



