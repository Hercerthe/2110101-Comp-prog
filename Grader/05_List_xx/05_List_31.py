card = input().split()
method = list(input())
for i in range(len(method)) :
    deck = []
    if method[i] == "C" :
        deck1 = card[:(len(card)//2)]
        deck2 = card[(len(card)//2):]
        card = deck2 + deck1
    elif method[i] == "S" :
        for i in range((len(card)//2)) :
            deck += card[i::(len(card)//2)]
        card = deck
    else :
        pass
print(" ".join(card))