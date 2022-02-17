import math

def f(x):
    #Add the desired function here 
    return x**3 + x**2 -1

def g(x):
    #Write the function in the form of x = g(x)
    return 1/math.sqrt(1+x)

def fixedPointIteration(a, e, N):
    step = 1
    flag = 1
    condition = True
    while condition:
        x1 = g(a)
        print('Iteration-%d, x1 = %0.6f and f(x1) = %0.6f' % (step, x1, f(x1)))
        a = x1

        step = step + 1
        
        if step > N:
            flag=0
            break
        
        condition = abs(f(x1)) > e

    if flag==1:
        print('\nRequired root is: %0.8f' % x1)
    else:
        print('\nNot Convergent.')

a = float(input('Enter Guess: '))
e = float(input('Tolerable Error: '))
N = int(input('Maximum Step: '))

fixedPointIteration(a,e,N)
