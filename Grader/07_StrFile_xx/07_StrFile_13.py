data = input().replace("'", " ").replace('"', " ").replace("-", " ").replace("(", " ").replace(")", " ").replace(".", " ").replace(">", " ").replace("<", " ").replace(";", " ").split(" ")
for i in range(1,len(data)) :
    data[i] = data[i].capitalize()
for i in range(len(data)) :
    if data[i] != "" :
        data[i] = data[i].lower()
        break
print("".join(data))