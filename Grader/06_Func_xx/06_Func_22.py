def distance1(x1, y1, x2, y2):
    return ((abs(x2-x1)**2)+(abs(y2-y1)**2))**(1/2)

def distance2(p1, p2):
    return ((abs(p2[0]-p1[0])**2)+(abs(p2[1]-p1[1])**2))**(1/2)

def distance3(c1, c2):
    if distance2(c1, c2) > c1[2]+c2[2] :
        overlap = False
    if distance2(c1, c2) <= c1[2]+c2[2] :
        overlap = True
    return distance2(c1, c2), overlap
def perimeter(points):
    diameter = 0
    points += [points[0]]
    for i in range(1,len(points)) :
        diameter += distance2(points[i-1], points[i])
    return diameter

exec(input().strip())