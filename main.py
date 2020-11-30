import datetime
import lagic as la
import database

res = la.reservation
isstring = la.is_string_with_space
sql = database.database()

print(datetime.datetime.now())
def navndef():
    global res, isstring
    navnset = False
    while navnset == False:
        print("Skriv navn")
        navn = str(input())
        print(isstring(navn))
        if isstring(navn) == True:
            res = res(navn)
            navnset = True
    return navn
def datedef():
    global res, sql
    datoset = False
    while datoset == False:
        print("Enter a date in YYYY-MM-DD format")
        datoin = input()
        try:
            year, month, day, = res.dato(datoin)
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
        #try:
        hour, minute = res.time(time)
        strmin = str(minute)
        strhour = str(hour)
        timeset = res.timetest(hour, minute, strhour, strmin)
        print(timeset)
        #except:
            #pass
    finaldate = str(res.final(year, month, day, hour, minute))
    return finaldate


print("Hvad vil du? "
      "1: Tilføj"
      "2: Ændrer"
      "3: Slet")
valg = int(input())

if valg == 1:
    navn = navndef()
    finaldate = datedef()
    print("Reservation for", navn, "til", finaldate)
    sql.add(navn, finaldate)

elif valg == 2:
    navn = str(navndef())
    newdate = str(datedef())
    print("New date is:", newdate, type(newdate))
    print(navn)
    print(navn, newdate)
    sql.modify(navn, newdate)

elif valg == 3:
    print("Hvem skal slettes?")
    valgnavn = input()
    sql.delete(valgnavn)


