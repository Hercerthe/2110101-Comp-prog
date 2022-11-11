import numpy as np
def toCelsius( f ):
    return (f-32)*5/9
def BMI( wh ):
    bmi = list()
    for i in range(wh.shape[0]) :
        bmi.append(wh[i][0]/((wh[i][1]/100)**2))
    return np.array(bmi)
def distanceTo( p, Points ):
    distance = list()
    for i in range(Points.shape[0]) :
        distance.append((((p[0]-Points[i][0])**2)+((p[1]-Points[i][1])**2))**0.5)
    return np.array(distance)
exec(input().strip())