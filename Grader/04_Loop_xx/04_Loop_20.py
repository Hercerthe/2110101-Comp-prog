x = 0
y = 1
z = 1
while z != 0 :
    data = input()
    if data == "Zig-Zag" or data == "Zag-Zig" :
        break
    data = data.split(" ")
    if x == 0 :
        min_line1 = int(data[x%2])
        max_line1 = int(data[x%2])
        min_line2 = int(data[y%2])
        max_line2 = int(data[y%2])
    else :
        min_line1 = min(int(data[x%2]), min_line1)
        max_line1 = max(int(data[x%2]), max_line1)
        min_line2 = min(int(data[y%2]), min_line2)
        max_line2 = max(int(data[y%2]), max_line2)
    x += 1
    y += 1

if data == "Zig-Zag" :
    print(min_line1, max_line2)
if data == "Zag-Zig" :
    print(min_line2, max_line1)