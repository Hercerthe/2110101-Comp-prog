import matplotlib.pyplot as plt 

def plot(X, Y, Y_hat):
    plt.plot(X, Y, 'g+')
    plt.plot(X, Y_hat,'r')
    plt.show()

def main():
    X = [1,2,3,4,5]
    Y = input('Y = ').split()
    Y = [float(Y[0]),float(Y[1]),float(Y[2]),float(Y[3]),float(Y[4])]
    
    a = float(input('a = '))
    b = float(input('b = '))
    c = float(input('c = '))

    Y_hat = [f(X[0],a,b,c),f(X[1],a,b,c),f(X[2],a,b,c),f(X[3],a,b,c),f(X[4],a,b,c)]

    plot(X, Y, Y_hat)
    print("Sum of squared errors =", SSE(Y, Y_hat))

def f(x, a, b, c):
    fx = (a*(x**2))+(b*x)+c
    return fx

def SSE(Y, Y_hat):
    sigma = ((Y[0]-Y_hat[0])**2)+((Y[1]-Y_hat[1])**2)+((Y[2]-Y_hat[2])**2)+((Y[3]-Y_hat[3])**2)+((Y[4]-Y_hat[4])**2)
    return sigma



main()