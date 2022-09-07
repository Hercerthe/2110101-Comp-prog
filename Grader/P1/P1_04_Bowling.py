data = list(input())
fgame = int(input())
game = []
stat = []
point = 0
block = 0
for i in range(9) :
    if data[0] == "X" :
        game += [[10]]
        data = data[1:]
    elif data[1] == "/" :
        game += [[int(data[0]), 10 - int(data[0])]]
        data = data[2:]
    elif int(data[1]) in range(10) :
        game += [[int(data[0]), int(data[1])]]
        data = data[2:]

if data[0] == "X" :
    if data[1] == "X" :
        if data[2] == "X" :
            game += [[10, 10, 10]]
        else :
            game += [[10, 10, int(data[2])]]
    elif data[2] == "/" :
        game += [[10, int(data[1]), 10 - int(data[1])]]
    else :
        game += [[10, int(data[1]), int(data[2])]]
elif data[1] == "/" :
    if data[2] == "X" :
        game += [[int(data[0]), 10 - int(data[0]), 10]]
    else :
        game += [[int(data[0]), 10 - int(data[0]), int(data[2])]]
elif int(data[1]) in range(10) :
    game += [[int(data[0]), int(data[1])]]

for i in range(9) :
    if game[i] == [10] :
        stat += [["strike"]]
    elif sum(game[i]) == 10 :
        stat += [["spare"]]
    elif sum(game[i]) < 10 :
        stat += [["norm"]]

if fgame not in range(1,11) :
    for i in range(10) :
        if i == 9 :
            block = sum(game[i])
        elif stat[i][0] == "strike" :
            if len(game[i + 1]) == 1 :
                block = game[i][0] + game[i + 1][0] + game [i + 2][0]
            else :
                block = game[i][0] + game[i + 1][0] + game[i + 1][1]
        elif stat[i][0] == "spare" :
            block = sum(game[i]) + game[i + 1][0]
        elif stat[i][0] == "norm" :
            block = sum(game[i])
        point += block
    print(point)
else :
    fgame -= 1
    if fgame == 9 :
        block = sum(game[fgame])
    elif stat[fgame][0] == "strike" :
        if len(game[fgame + 1]) == 1 :
            block = game[fgame][0] + game[fgame + 1][0] + game [fgame + 2][0]
        else :
            block = game[fgame][0] + game[fgame + 1][0] + game[fgame + 1][1]
    elif stat[fgame][0] == "spare" :
        block = sum(game[fgame]) + game[fgame + 1][0]
    elif stat[fgame][0] == "norm" :
        block = sum(game[fgame])
    print(block)