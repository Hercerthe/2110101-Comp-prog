line = int(input())
coordinate = []
for i in range(line) :
    ram = [float(e) for e in input().split(" ")]
    absolute = ((ram[0] **2 ) + (ram[1] ** 2)) ** (1 / 2)
    coordinate += [[absolute] + ram + [(i + 1)]]
coordinate = sorted(coordinate)
print("#" + str(coordinate[2][3]) + ":" , "(" + str(coordinate[2][1]) + "," , str(coordinate[2][2]) + ")")