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
    newstartdate = startdate.replace("-", "")
    newstarttime = starttime.replace(":", "")
    start = newstartdate+newstarttime
    newslutdate = slutdate.replace("-", "")
    newsluttime = sluttime.replace(":", "")
    slut = newslutdate+newsluttime

    reslist = sql.pullall()
    intervallist = []
    resamount = len(reslist)
    for i in range(resamount):
        res = str(reslist[i])
        resname, resfulldate = res.split(",")
        blank, resdate, restime = resfulldate.split(" ")
        resdate = resdate.replace("'", " ")
        newresdate = resdate.replace("-", "")

        restime = restime.replace(")", " ")
        restime = restime.replace("'", " ")
        newrestime = restime.replace(":", "")
        #print("før", newrestime)
        newrestime = newrestime.strip()
        newrestime = newrestime[:-2]
        #print("efter", newrestime)
        #print(newrestime)
        newresdate = newresdate[1:]
        searchres = newresdate+newrestime
        #print(start, searchres, slut)
        #print(len(start), len(searchres), len(slut))
        if int(start) < int(searchres) < int(slut):
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
