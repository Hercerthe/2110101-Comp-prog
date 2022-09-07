def RLE(t):
    lenght = len(t)
    main_list = []
    return_list = []
    len_list = []
    start = 0
    if lenght == 0 :
        return []
    if lenght == 1 :
        return [[t, 1]]
    
    main_list += t[0]

    for e in range(1, lenght) :
        if t[e] != t[e - 1] :
            main_list += t[e]
    
    for e in main_list :
        x = 0
        for i in range(start, lenght) :
            if e == t[i] :
                x += 1
            else :
                start = i
                break
        len_list += [x]

    for e in range(0, len(main_list)) :
        return_list += [[main_list[e], len_list[e]]]

    return return_list

exec(input())