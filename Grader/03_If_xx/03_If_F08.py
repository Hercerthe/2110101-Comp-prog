def day_of_year(d, m, y):
    day_got = d
    month_got = sum([month_to_date(x, y) for x in range(0, m)])
    return day_got + month_got

def check_feb29(y) :
    y -= 543
    if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0 :
        return True
    else :
        return False

def month_to_date(m, y) :
    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12 :
        return 31
    if m == 4 or m == 6 or m == 9 or m == 11 :
        return 30
    if check_feb29(y) == True and m == 2 :
        return 29
    if check_feb29(y) == False and m == 2 :
        return 28
    else :
        return 0

exec(input())