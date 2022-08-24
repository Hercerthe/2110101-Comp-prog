cid = input()
n12 = (11 - (( (13*int(cid[0]))+(12*int(cid[1]))+(11*int(cid[2]))+(10*int(cid[3]))+(9*int(cid[4]))+(8*int(cid[5]))+(7*int(cid[6]))+(6*int(cid[7]))+(5*int(cid[8]))+(4*int(cid[9]))+(3*int(cid[10]))+(2*int(cid[11]))) % 11 )) % 10

print(cid[0], cid[1:5], cid[5:10], cid[10:12], n12)