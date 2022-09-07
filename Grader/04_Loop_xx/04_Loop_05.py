int_word = input()
int_sent = list(input())

for e in range(0,len(int_sent)) :
    if int_sent[e] == '"' :
        int_sent[e] = " "
    elif int_sent[e] == "'" :
        int_sent[e] = " "
    elif int_sent[e] == "(" :
        int_sent[e] = " "
    elif int_sent[e] == ")" :
        int_sent[e] = " "
    elif int_sent[e] == "," :
        int_sent[e] = " "
    elif int_sent[e] == "." :
        int_sent[e] = " "

int_sent = "".join(int_sent)
int_sent = int_sent.split(" ")
x = 0
for e in int_sent :
    if int_word == e :
        x += 1
        
print(x)