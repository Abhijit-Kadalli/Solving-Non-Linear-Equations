from ast import Return
import math



def bisection(f,a,b,n,e):
    if f(a)*f(b) >= 0:
        print("Error please recheck the range")
        return None
    for i in range(1,n+1):
        m = (a+b)/2
        print('Iteration-%d, m = %0.6f and f(m) = %0.6f' % (i, m, f(m)))
        if f(a)* f(m) < 0 :
            a = a
            b = m
        elif f(m)* f(b) < 0:
            a = m
            b = b
        elif f(m)== 0:
            print("The Exact Solution is ")
            return m
        else :
            print("Bisection Method failed")    
        if abs((((a+b)/2)-m)/m) <= e:
            print("The approximate solution with regards to the inputed error tolerance is ")  
            return ((a+b)/2)
    return ((a+b)/2)

a = float(input('First Guess: '))
b = float(input('Second Guess: '))
n = int(input("Number of iterations: "))
e = float(input('Tolerable Error: '))

#EXAMPLE PLEASE CHANGE THE FUNCTION F TO THE FUNCTION THAT YOU WANT
f = lambda x: x**2 - x - 1
print(bisection(f,a,b,n,e))
