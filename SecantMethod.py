import math

def f(x):
    #add the function you need here 
    return x

def SecantMethod(x0,x1,n,e):
    step = 1
    flag = 1
    condition = True
    while condition:
        x2 = (x0*f(x1) - x1*f(x0)) - (f(x1) - f(x0))
        print('Iteration-%d, x1 = %0.6f and f(x1) = %0.6f' % (step, x1, f(x2)))
        x0 = x1
        x1 = x2

        step = step + 1
        
        if step > n:
            flag=0
            break
        
        condition = abs((x2 - x1)/x2) > e

    if flag==1:
        print('\nRequired root is: %0.8f' % x2)
    else:
        print('\nNot Convergent.')



x0 = float(input('First Guess: '))
x1 = float(input('Second Guess: '))
n = int(input("Number of iterations: "))
e = float(input('Tolerable Error: '))    

SecantMethod(x0,x1,n,e)