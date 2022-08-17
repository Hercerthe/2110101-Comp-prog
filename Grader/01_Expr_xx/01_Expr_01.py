import math

n = int(input())
lowerline = (math.sqrt(2*math.pi))*(n**(n+0.5))*(math.e**(-n+(1/(12*n+1))))
upperline = (math.sqrt(2*math.pi))*(n**(n+0.5))*(math.e**(-n+(1/(12*n))))

print("Lowerline is",lowerline)
print("Upperline is",upperline)