point = {"R":1, "Y":2, "G":3, "W":4, "B":5, "P":6, "K":7, "X":0}
listed = ["Y", "G", "W", "B", "P", "K"]
red = 6
score = {"1":0, "2":0}
while listed != [] :
    data = list(input())
    if red != 0 and data[1] == "R" and data[2] != "R" :
        red -= 1
        score[data[0]] += point[data[1]] + point[data[2]]
    elif red == 0 and data[1] == listed[0] :
        score[data[0]] += point[data[1]]
        listed.pop(0)
print(score["1"], score["2"])
if score["1"] > score["2"] :
    print("Player 1 wins")
elif score["1"] < score["2"] :
    print("Player 2 wins")
else :
    print("Tie")