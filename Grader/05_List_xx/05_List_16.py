n = int(input())
record = [str(n)]
while n != 1 :
    if n % 2 == 0 :
        n //= 2
        record += [str(n)]
    else :
        n = (3*n) + 1
        record += [str(n)]
if len(record) <= 15 :
    print("->".join(record))
elif len(record) > 15 :
    record = record[::-1]
    record = record[:15]
    print("->".join(record[::-1]))