import datetime
import lagic as res


print(datetime.datetime.now())

navnset = False
while navnset == False:
    print("Skriv navn")
    navn = str(input())
    print(is_string_with_space(navn))
    if is_string_with_space(navn) == True:
        res = reservation(navn)
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
    except:
        print("Du skrev noget jank")

    try:
        if month < 13 and day < 32 and len(strmonth) < 3 and len(strday) < 3 and len(stryear) < 5:
            datoset = True
            print("Det lykkedes")
        else:
            print("Error in your date, remember to write it like YYYY-MM-DD")
    except:
        print("Din far")




print("Enter a time in HH:MM format")
time = input()
hour, minute = res.time(time)

print("Reservation for", navn, "til", res.final(year, month, day, hour, minute))
