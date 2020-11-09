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


print(datetime.datetime.now())

print("Navn")
navn = str(input())
res = reservation(navn)

print("Enter a date in YYYY-MM-DD format")
dato = input()
year, month, day, = res.dato(dato)

print("Enter a time in HH:MM format")
time = input()
hour, minute = res.time(time)

print("Reservation for", navn, "til", res.final(year, month, day, hour, minute))
