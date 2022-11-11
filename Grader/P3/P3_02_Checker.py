pos = input().strip()
if len(pos) <= 3 :
    row = pos[0].strip().lower()
    col = pos[1:].strip()
elif len(pos) > 3 :
    pos = pos.split(",")
    for i in pos :
        if "row" in i :
            row = i.replace("row", "").replace("=", "").strip().lower()
        elif "col" in i :
            col = i.replace("col", "").replace("=", "").strip().lower()
rowState = True
colState = True
if not row.isalpha() or len(row) > 1 :
    rowState = False
if col.isdigit() :
    if int(col) not in range(1,53) :
        colState = False
else :
    colState = False
if rowState is False and colState is False :
    print("Invalid row and column")
elif rowState is False :
    print("Invalid row")
elif colState is False :
    print("Invalid column")
else :
    r = 'abcdefghijklmnopqrstuvwxyz'.find(row)
    if (r+int(col))%2 == 0 :
        print('Black')
    else:
        print('White')