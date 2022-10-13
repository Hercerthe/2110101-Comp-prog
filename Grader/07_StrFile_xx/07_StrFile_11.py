data = input()
if data[-1] == "x" or data[-1] == "s" or data[-2:] == "ch" :
    data += "es"
elif data[-1] == "y" :
    if data[-2] not in "aeiou" :
        data = data[0:-1] + "ies"
    else :
        data += "s"
else :
    data += "s"
print(data)