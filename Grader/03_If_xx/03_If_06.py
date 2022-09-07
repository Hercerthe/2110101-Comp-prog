w = int(input())

if w in range(101) :
    print("18")
if w in range(101, 251) :
    print("22")
if w in range(251, 501) :
    print("28")
if w in range(501, 1001) :
    print("38")
if w in range(1001, 2001) :
    print("58")
if w > 2000 :
    print("Reject")