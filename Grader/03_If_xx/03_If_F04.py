def is_mobile_number(number):
    mb_nb = ["06", "08", "09"]

    if len(number) != 10 :
        return False

    number = number[:2]

    if number in mb_nb :
        return True
    else :
        return False

exec(input())