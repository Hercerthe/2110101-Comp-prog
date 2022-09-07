ticket_data = []
ticket_number = 0
q_number = 0
wait_time = []

line = int(input())
for d in range(line) :
    ram = input().split()
    if ram[0] == "reset" :
        ticket_number = int(ram[1])
        q_number = int(ram[1])

    elif ram[0] == "new" :
        ticket_data += [[ticket_number, ram[1]]]
        print("ticket", ticket_number)
        ticket_number += 1
        
    elif ram[0] == "next" :
        print("call", q_number)
        q_number += 1

    elif ram[0] == "order" :
        for h in range(len(ticket_data)) :
            if ticket_data[h][0] == (q_number - 1) :
                delta_time = int(ram[1]) - int(ticket_data[h][1])
                break
        print("qtime", q_number - 1, delta_time)
        wait_time += [delta_time]

    elif ram[0] == "avg_qtime" :
        print("avg_qtime", round(sum(wait_time)/len(wait_time), 4))