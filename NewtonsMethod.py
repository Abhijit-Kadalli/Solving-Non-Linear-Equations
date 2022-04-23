import math

def f(x):
    # add your twice differentiable function here
    return x

def g(x):
    # add derivative of f(x) here
    return 1

def NewtonsMethod(a,e,N):
    step = 1
    flag = 1
    condition = True
    while condition:
        x1 = a - f(a)/g(a)
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

NewtonsMethod(a,e,N)