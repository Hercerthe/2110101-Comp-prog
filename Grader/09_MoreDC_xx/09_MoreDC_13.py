team = set()
loss = set()
for i in range(int(input())) :
    for e in input().split() :
        team.add(e)
    loss.add(e)
win = team - loss
winner = []
for i in win :
    winner.append(i)
print(sorted(winner))