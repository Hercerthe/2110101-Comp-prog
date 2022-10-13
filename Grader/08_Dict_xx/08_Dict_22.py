icecream = {} #name,price
sales = {} #name,qunatity
net = {} #name,net
topnet = {}
for i in range(int(input())) :
    data = input().split()
    icecream[data[0]] = float(data[1])

for i in range(int(input())) :
    data = input().split()
    if data[0] in icecream :
        if data[0] not in sales :
            sales[data[0]] = float(data[1])
        else :
            sales[data[0]] += float(data[1])

for i in sales :
    if i in icecream :
        net[i] = icecream[i]*sales[i]

for i in net :
    if net[i] not in topnet :
        topnet[net[i]] = [i]
    else :
        topnet[net[i]] += [i]

if sales == {} :
    print("No ice cream sales")
else :
    print("Total ice cream sales:",sum(net[i] for i in net))
    print("Top sales:",", ".join(sorted(topnet[max(i for i in topnet)])))