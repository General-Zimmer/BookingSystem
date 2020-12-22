from datetime import date, timedelta
import datetime
import lagic as la
import database

res = la.reservation
sql = database.database()

print(datetime.datetime.now())


def navndef():
    global res, isstring
    navnset = False
    while navnset == False:
        print("Skriv navn")
        navn = str(input())
        res2 = la.reservation(navn)
        print(res2.is_string_with_space())
        navnset = res2.is_string_with_space()
    return navn


def datedef():
    global sql, navn
    try:
        navn
    except NameError:
        navn = None

    res2 = res(navn)
    datoset = False
    while datoset == False:
        print("Enter a date in YYYY-MM-DD format")
        datoin = input()
        try:
            year, month, day, = res2.dato(datoin)
            stryear = str(year)
            strmonth = str(month)
            strday = str(day)
            datoset = res2.datetest(month, day, strmonth, strday, stryear)
            print(res2.datetest(month, day, strmonth, strday, stryear))

        except:
            pass

    timeset = False
    while timeset == False:
        print("Enter a time in HH:MM format")
        time = input()
        try:
            hour, minute = res2.time(time)
            strmin = str(minute)
            strhour = str(hour)
            timeset = res2.timetest(hour, minute, strhour, strmin)
            print(timeset)
        except:
            pass
    finaldate = str(res2.final(year, month, day, hour, minute))
    return finaldate


def search(startdate, starttime, slutdate, sluttime):
    startyear, startmonth, startday = startdate.split("-")
    starthour, startmin = starttime.split(":")
    slutyear, slutmonth, slutday = slutdate.split("-")
    sluthour, slutmin = sluttime.split(":")

    reslist = sql.pullall()
    intervallist = []
    resamount = len(reslist)
    for i in range(resamount):
        res = str(reslist[i])
        resname, resfulldate = res.split(",")
        blank, resdate, restime = resfulldate.split(" ")
        resdate = resdate.replace("'", " ")
        restime = restime.replace(")", " ")
        restime = restime.replace("'", " ")
        # print("før", res)
        resyear, resmonth, resday = resdate.split("-")
        reshour, resmin, ressec = restime.split(":")
        # print("testyear", 0 <= int(slutyear)-int(resyear) <= int(slutyear)-int(startyear))
        # print("testmonth", 0 <= int(slutmonth)-int(resmonth) <= int(slutmonth)-int(startmonth))
        # print("testday", 0 <= int(slutday) - int(resday) <= int(slutday) - int(startday))
        # print("testhour", 0 <= int(sluthour) - int(reshour) <= int(sluthour) - int(starthour))
        # print("testmin", 0 <= int(slutmin) - int(resmin) <= int(slutmin) - int(startmin))
        if 0 < int(slutyear) - int(resyear) <= int(slutyear) - int(startyear):
            intervallist.append(res)
        elif 0 == int(slutyear) - int(resyear):
            if 0 < int(slutmonth) - int(resmonth) <= int(slutmonth) - int(startmonth):
                intervallist.append(res)
            elif 0 == int(slutday) - int(resday):
                if 0 < int(slutday) - int(resday) <= int(slutday) - int(startday):
                    intervallist.append(res)
                elif 0 == int(slutday) - int(resday):
                    if 0 <= int(sluthour) - int(reshour) <= int(sluthour) - int(starthour):
                        intervallist.append(res)
                    elif 0 == int(sluthour) - int(reshour):
                        if 0 <= int(slutmin) - int(resmin) <= int(slutmin) - int(startmin):
                            intervallist.append(res)
    return intervallist


while True:
    print("Hvad vil du?\n"
          "1: Tilføj\n"
          "2: Ændrer\n"
          "3: Slet\n"
          "4: Se alle reservationer\n"
          "5: Søg i interval")
    valg = int(input())

    if valg == 1:
        navn = navndef()
        finaldate = datedef()
        print("Reservation for", navn, "til", finaldate)
        sql.add(navn, finaldate)

    elif valg == 2:
        navn = str(navndef())
        newdate = str(datedef())
        sql.modify(navn, newdate)

    elif valg == 3:
        print("Hvem skal slettes?")
        valgnavn = str(navndef())
        sql.delete(valgnavn)

    elif valg == 4:
        allres = sql.pullall()
        print(allres)

    elif valg == 5:
        print("Enter a start date in YYYY-MM-DD format")
        startdate = str(input())
        print("Enter a start time in HH:MM format")
        starttime = str(input())
        print("Enter a end date in YYYY-MM-DD format")
        slutdate = str(input())
        print("Enter a end time in HH:MM format")
        sluttime = str(input())
        print(search(startdate, starttime, slutdate, sluttime))


    elif valg == 6:
        datedef()
