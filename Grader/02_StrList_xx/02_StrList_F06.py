from cgitb import reset


def add_vector(u, v):
    u = [float(u[0]), float(u[1]), float(u[2])]
    v = [float(v[0]), float(v[1]), float(v[2])]
    result = [u[0]+v[0], u[1]+v[1], u[2]+v[2]]
    return result

exec(input()) # DON'T remove this line