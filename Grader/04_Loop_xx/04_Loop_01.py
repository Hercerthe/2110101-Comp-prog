i = 0
data = []

while i != "q" :
    i = input()
    if i == "q" and data == [] :
        print("No Data")
        break
    if i == "q" :
        data = sum(data)/len(data)
        print(round(data, 2))
        break
    data += [float(i)]