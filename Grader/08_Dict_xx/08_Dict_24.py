button = {"2":"ABC","3":"DEF","4":"GHI","5":"JKL","6":"MNO","7":"PQRS","8":"TUV","9":"WXYZ","0":" "}
time = {1:"ADGJMPTW ", 2:"BEHKNQUX", 3:"CFILORVY", 4:"SZ"}
def text2keys(text):
    text = [i.upper() for i in text if i.isalpha() or i.isspace()]
    for i in range(len(text)) :
        for e in button :
            if text[i] in button[e] :
                for r in time :
                    if text[i] in time[r] :
                        text[i] = e*r
    return " ".join(text)

def keys2text(keys):
    keys = keys.split()
    for i in range(len(keys)) :
        keys[i] = button[keys[i][0]][len(keys[i])-1]
    return "".join(keys).lower()

exec(input().strip())