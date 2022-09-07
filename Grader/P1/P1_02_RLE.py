mode = input()

if mode != "RLE2str" and mode != "str2RLE" :
    print("Error")
else :
    data = input()
    if mode == "str2RLE" :

        for e in range(0, len(data)) :
            if len(data) == 1 :
                new_data = data + " 1"

            elif e == 0 :
                new_data = data[0] + " "
                x = 1

            elif e == (len(data) - 1) :
                if data[e - 1] != data[e] :
                    new_data += str(x) + " "
                    new_data += data[e] + " "
                    new_data += "1"
                else :
                    x += 1
                    new_data += str(x)

            elif data[e - 1] == data[e] :
                x += 1

            elif data[e - 1] != data[e] :
                new_data += str(x) + " "
                new_data += data[e] + " "
                x = 1

        print(new_data)

    elif mode == "RLE2str" :

        data = data.split(" ")
        char = data[::2]
        char_len = data[1::2]
        new_char = []

        for e in range(0, len(char)) :
            new_char += char[e] * int(char_len[e])

        print("".join(new_char))