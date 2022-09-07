d = int(input())
m = int(input())
y = int(input())

def check_feb29(year) :
    year -= 543
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 :
        return True
    else :
        return False

def month_to_date(month, year) :
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12 :
        return 31
    if month == 4 or month == 6 or month == 9 or month == 11 :
        return 30
    if check_feb29(year) == True and month == 2 :
        return 29
    if check_feb29(year) == False and month == 2 :
        return 28
    else :
        return 0

def calculate(d, m, y) :
    day_got = d
    month_got = sum([month_to_date(x, y) for x in range(0, m)])
    return day_got + month_got

print(calculate(d, m, y))