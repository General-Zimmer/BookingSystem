import datetime

class reservation():
    def __init__(self, navn):
        self.navn = navn

    def dato(self, dato):
        year, month, day = map(int, dato.split('-'))
        return year, month, day

    def time(self, time):
        hour, minute = map(int, time.split(':'))
        return hour, minute

    def final(self, year, month, day, hour, minute):
        finaldate = datetime.datetime(year, month, day, hour, minute)
        return finaldate

def is_string_with_space(check_input):
    valid = False
    if ' ' in check_input:
        for char in check_input:
            if char.isdigit():
                valid = False
            elif char.isalpha() or char.isspace():
                valid = True
    return valid

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
