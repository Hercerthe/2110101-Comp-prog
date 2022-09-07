m = int(input())
tie = m * 3
p = 0
p1 = 0
p2 = 0
a1 = ["R", "P"]
a2 = ["P", "S"]
a3 = ["S", "R"]
b1 = ["P", "R"]
b2 = ["S", "P"]
b3 = ["R", "S"]

while p1 != m and p2 != m :
    data = input().split()
    if data == a1 or data == a2 or data == a3 :
        p2 += 1
        p += 1
    elif data == b1 or data == b2 or data == b3 :
        p1 += 1
        p += 1
    else :
        p += 1
    if tie == p :
        break

if tie == p :
    print(p1, p2)
    print("Tie")
elif p1 > p2 :
    print(p1, p2)
    print("Player 1 wins")
elif p1 < p2 :
    print(p1, p2)
    print("Player 2 wins")
