string = input()

for e in range(0, len(string)) :
    if len(string) == 1 :
        new_string = string + " 1"

    elif e == 0 :
        new_string = string[0] + " "
        x = 1

    elif e == (len(string) - 1) :
        if string[e - 1] != string[e] :
            new_string += str(x) + " "
            new_string += string[e] + " "
            new_string += "1"
        else :
            x += 1
            new_string += str(x)

    elif string[e - 1] == string[e] :
        x += 1

    elif string[e - 1] != string[e] :
        new_string += str(x) + " "
        new_string += string[e] + " "
        x = 1


print(new_string)