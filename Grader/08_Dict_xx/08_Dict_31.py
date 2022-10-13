def total(pocket):
    pocket = sum([pocket[i]*i for i in pocket])
    return pocket
def take(pocket, money_in):
    for i in money_in :
        if i not in pocket :
            pocket[i] = money_in[i]
        else :
            pocket[i] += money_in[i]
def pay(pocket, amt):
    bank = []
    choose = {}
    extra = 0
    for i in pocket :
        bank += [i]
    bank = sorted(bank, reverse=True)
    for i in bank :
        choose[i] = amt//i
        amt %= i
    for i in bank :
        if extra != 0 :
            choose[i] += extra//i
            extra %= i
        if choose[i] > pocket[i] :
            extra += (choose[i]-pocket[i])*i
            choose[i] = pocket[i]
    for i in pocket :
        if choose[i] == 0 :
            choose.pop(i)
    if extra != 0 :
        return {}
    for i in choose :
        pocket[i] -= choose[i]
    return choose
exec(input().strip())