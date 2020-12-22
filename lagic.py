import datetime

class reservation():
    def __init__(self, navn):
        self.navn = navn

    def is_string_with_space(self):
        valid = False
        if ' ' in self.navn:
            for char in self.navn:
                if char.isdigit():
                    valid = False
                elif char.isalpha() or char.isspace():
                    valid = True
        return valid

    def dato(self, dato):
        year, month, day = map(int, dato.split('-'))
        return year, month, day

    def time(self, time):
        hour, minute = map(int, time.split(':'))
        return hour, minute

    def final(self, year, month, day, hour, minute):
        finaldate = datetime.datetime(year, month, day, hour, minute)
        return finaldate

    def datetest(self, month, day, strmonth, strday, stryear):
        if month < 13 and day < 32 and len(strmonth) < 3 and len(strday) < 3 and len(stryear) < 5:
            return True
        else:
            return False

    def timetest(self, hour, minute, strhour, strmin):
        if hour < 24 and minute < 61 and len(strhour) < 3 and len(strmin) < 3:
            return True
        else:
            return False



