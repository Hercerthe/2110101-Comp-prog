def missing_digits(t):
    digit = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    data = t
    result = []
    for e in range(10) :
        if digit[e] not in data :
            result += [e]
    return result

exec(input())