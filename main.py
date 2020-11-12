import datetime
import lagic

res = lagic.reservation
isstring = lagic.is_string_with_space

print(datetime.datetime.now())

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

print("Enter a time in HH:MM format")
time = input()
hour, minute = res.time(time)

print("Reservation for", navn, "til", res.final(year, month, day, hour, minute))
