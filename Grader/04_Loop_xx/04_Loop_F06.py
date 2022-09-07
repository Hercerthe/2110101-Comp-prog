def print_triangle(h):
    w = (2 * h) - 1

    for e in range(0,h) :
        e += 1
        if e == 1 :
            dot = "." * (h - e)
            print(dot + "*")
        elif h > e > 1 :
            dot_out = "." * (h - e)
            dot_in = "." * (1 + (2 * (e - 2)))
            print(dot_out + "*" + dot_in + "*")
        elif e == h :
            print("*" * w)
exec(input())