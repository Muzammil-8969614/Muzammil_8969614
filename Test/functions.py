# Program (leap_year.py)

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


# Program (reverse_string.py)

def reverse_string(s):
    return s[::-1]
