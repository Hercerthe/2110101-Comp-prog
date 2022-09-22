def read_date():
    month = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    data = input().split(" ")
    d = int(data[0])
    m = month.index(data[1][:3]) + 1
    y = int(data[2])
    return [d, m, y]

def zodiac(d,m):
    z_list = ["Capricorn", "Aquarius", "Pisces", "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn"]
    if (m == 1 or m == 2) and (d <= 20) :
        m -= 1
    elif d <= 21 and (m != 1 or m != 2) :
        m -= 1
    return z_list[m]

def days_in_feb(y):
    if (y%4 == 0 and y%100 == 0 and y%400 == 0) or (y%4 == 0 and y%100 != 0) :
        return 29
    else :
        return 28

def days_in_month(m,y):
    month = [31,28,31,30,31,30,31,31,30,31,30,31]
    if (y%4 == 0 and y%100 == 0 and y%400 == 0) or (y%4 == 0 and y%100 != 0) :
        month[1] = 29
    return month[m-1]

def days_in_between(d1,m1,y1,d2,m2,y2):
    month = [31,28,31,30,31,30,31,31,30,31,30,31]
    if y2 == y1 :
        if (y1%4 == 0 and y1%100 == 0 and y1%400 == 0) or (y1%4 == 0 and y1%100 != 0) :
            month[1] = 29
        if m2 == m1 :
            return d2 - d1
        else :
            daybirth = sum([month[i] for i in range(m1-1)], d1)
            dayhave = sum([month[i] for i in range(m2-1)], d2)
        return dayhave - daybirth
    if y2 != y1 :
        if (y1%4 == 0 and y1%100 == 0 and y1%400 == 0) or (y1%4 == 0 and y1%100 != 0) :
            month[1] = 29
        else :
            month[1] = 28
        dhave = (days_in_feb(y1) + 337 - sum([month[i] for i in range(m1-1)], d1))
        if (y2%4 == 0 and y2%100 == 0 and y2%400 == 0) or (y2%4 == 0 and y2%100 != 0) :
            month[1] = 29
        else :
            month[1] = 28
        dhave += (sum([month[i] for i in range(m2-1)], d2))
        yhave = 0
        for i in range(y1+1,y2) :
            yhave += days_in_feb(i) + 337
        return dhave+yhave - 1
    
def main():
    d1,m1,y1 = read_date()
    d2,m2,y2 = read_date()
    print(zodiac(d1,m1), zodiac(d2,m2))
    print(days_in_between(d1,m1,y1,d2,m2,y2))

exec(input().strip())