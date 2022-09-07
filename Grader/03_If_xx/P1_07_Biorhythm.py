import math

# check func

def check_feb29(year) :
    year = year - 543
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 :
        return True
    else :
        return False

def check_same_year(by, y) :
    if by == y :
        return True
    else :
        return False

def check_same_month(bm, m) :
    if bm == m :
        return True
    else :
        return False

def check_false_date(bd, bm, by, d, m, y) :
    if by > y :
        return True
    if by == y and bm > m :
        return True
    if by == y and bm == m and bd >= d :
        return True
    if check_feb29(by) == False and bm == 2 :
        return bd == 29
    if check_feb29(y) == False and m == 2 :
        return d == 29
    else :
        return False

# main func

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

def year_to_date(year) :
    year = year*365
    return year

def redzone(bd, bm, by,) :
    day_left = (month_to_date(bm ,by) - bd) + 1
    month_left = sum([month_to_date(x, by) for x in range(bm + 1, 13)])
    return day_left + month_left

def blackzone(by, y) :
    return year_to_date((y - 1) - by)

def bluezone(d, m, y) :
    day_got = d - 1
    month_got = sum([month_to_date(x, y) for x in range(0, m)])
    return day_got + month_got

def same_year(bd, bm, by, d, m, y) :
    if check_same_month(bm, m) == True :
        return d - bd
    else :
        daybirth = sum([month_to_date(x, y) for x in range(0, bm)], bd)
        dayhave = sum([month_to_date(x, y) for x in range(0, m)], d)
        return dayhave - daybirth
        
def export_date(bd, bm, by, d, m, y) :
    if check_same_year(by ,y) == True :
        return same_year(bd, bm, by, d, m, y)
    if check_same_year(by ,y) == False :
        return redzone(bd, bm, by) + bluezone(d, m, y) + blackzone(by, y)

#exec func

def main() :
    bd, bm, by, d, m, y = [int(x) for x in input().split()]

    if check_false_date(bd, bm, by, d, m, y) == True :
        exit("Please insert valid date.")
    else :
        pass

    t = export_date(bd, bm, by, d, m, y)
    physical = math.sin((2*math.pi*t)/23)
    emotional = math.sin((2*math.pi*t)/28)
    intellectual = math.sin((2*math.pi*t)/33)

    print(t, "{:.2f}".format(physical), "{:.2f}".format(emotional), "{:.2f}".format(intellectual))

main()

# test case
# 1 1 2559 1 1 2560 --> 366 -0.52 0.43 0.54
# 1 1 2560 1 1 2561 --> 365 -0.73 0.22 0.37
# 20 11 2540 10 2 2544 --> 1177 0.89 0.22 -0.87
# 10 3 2559 3 1 2557 --> Please insert valid date.
# 29 2 2560 1 1 2561 --> Please insert valid date.