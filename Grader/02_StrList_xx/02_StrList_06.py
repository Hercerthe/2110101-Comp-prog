u = input()
u = u[1:-1]
u = u.split(", ")
u = [float(u[0]), float(u[1]), float(u[2])]
v = input()
v = v[1:-1]
v = v.split(", ")
v = [float(v[0]), float(v[1]), float(v[2])]

print(u, "+", v, "=", [u[0]+v[0], u[1]+v[1], u[2]+v[2]])