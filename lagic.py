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
