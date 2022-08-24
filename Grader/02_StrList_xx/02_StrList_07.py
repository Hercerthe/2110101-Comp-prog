data = input()
a = data[3::7]
b = data[7::5]
c = 10000 + int(a) + int(b)
c = str(c)[-4:-1]
d = list(c)
d = int(d[0])+int(d[1])+int(d[2])
d = str(d)[-1:]
d = int(d)+1

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

e = alphabet[int(d)-1]
print(str(c)+e)