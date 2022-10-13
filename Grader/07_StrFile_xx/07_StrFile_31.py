def check_invalid(data) :
    for i in data :
        if i not in "ATCG" :
            return True
            break
    return False

def reverse(data) :
    newList = ""
    for i in data[::-1] :
        if i in "AC" :
            newList += i.replace("A", "T").replace("C", "G")
        elif i in "TG" :
            newList += i.replace("T", "A").replace("G", "C")
    return newList

def frequency(data) :
    a = data.count("A")
    t = data.count("T")
    g = data.count("G")
    c = data.count("C")
    return "A={}, T={}, G={}, C={}".format(a,t,g,c)

def duo(data) :
    look = input()
    count = 0
    for i in range(len(data)-1) :
        if data[i:i+2] == look :
            count += 1
    return count

dna = input().upper().strip()
mode = input()
if  check_invalid(dna) == True :
    print("Invalid DNA")
elif mode == "R" :
    print(reverse(dna))
elif mode == "F" :
    print(frequency(dna))
elif mode == "D" :
    print(duo(dna))