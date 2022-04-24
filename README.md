# Solving Non Linear Equations
This repo contains code for solving non linear equations

## Theorem
An equation f (x) = 0 , where f (x) is a real continuous function, has at least one root between x=a and x=b if f(a) f(b) < 0 .

If f(a) f(b) > 0 this implies there may or may not be any roots to the equation in the interval [a, b] .

## Bisection Method 
Since the root is bracketed between two points, a and b , one can find the midpoint, x=p1 between a and b . <br />
This gives us two new intervals:
1. [a, p1]
2. [p1, b]

We can find the sign of
f(a) f(p1), and if f(a) f(p1) < 0 then the new interval where solution lies will be [a, p1],                <br />
otherwise, it is between [p1, b] .

As we repeat this process, the width of the interval becomes smaller and smaller, until you
reach the zero of the equation f(x) = 0 .

### Algorithm For Bisection Method
1. Choose a and b as two guesses for the root such that f(a) f(b) < 0, or in other
   words, f (x) changes sign between a and b .

2. Estimate the root, m , of the equation f (x) = 0 as the mid-point between a and b as                     <br />
   m = (a + b)/2

3. Now check the following <br />
  a) If f (a ) f (m ) < 0 , then the root lies between a and m ; then a = a and b = m .                     <br />
  b) If f (b ) f (m ) > 0 , then the root lies between m and b ; then a = m and b = b .                     <br />
  c) If f (a ) f (b ) = 0 ; then the root is m. Stop the algorithm if this is true .                        <br />

4. Find the absolute relative approximate error as                                                          <br />
   |∈<sub>a</sub>| = (  |m<sup>new</sup>  -  m<sup>old</sup> |  /  |m<sup>old</sup>|  ) * 100                           <br />
   m<sup>new</sup> = estimated root from present iteration                                                     <br />
   m<sup>old</sup> = estimated root from previous iteration                                                    <br />

5. Compare the absolute relative approximate error ∈a with the pre-specified relative error tolerance ∈s .  <br />
   If ∈a >∈s , then go to Step 3, else stop the algorithm .                                                    <br />      

:memo: **Note:**                                                                                            <br />
We have to also check whether the number of iterations is more than the maximum number of iterations allowed. <br />
If so, one needs to terminate the algorithm and notify the user about it.

## Fixed Point Iteration Method 
Fixed point iteration method is open and simple method for finding real root of non-linear equation by successive approximation. <br />
It requires only one initial guess to start. Since it is open method its convergence is not guaranteed.                          <br />

To find the root of nonlinear equation f(x)=0 by fixed point iteration method,                                                   <br />
we write given equation f(x)=0 in the form of                                                                                    <br />
x = g(x)                                                                                                                         <br />
where  
1. there exists [a, b],  such that g(x) ∈ [a, b] for all x ∈ [a, b]
2. there exists a real number  L<1 such that |g′(x)|<= L < 1  for all x ∈ (a, b)

If x0 is initial guess then next approximated root in this method is obtaine by                                                  <br />
x1 = g(x0 )                                                                                                                      <br />   
And similarly, next to next approximated root is obtained by using value of x1 i.e.                                              <br />
x2 = g(x1 )                                                                                                                      <br />
And the process is repeated until we get root within desired accuracy .                                                          <br />

### Algorithm For Fixed Point Iteration Method
1. Define function f(x)

2. Define function g(x) which is obtained from f(x)=0 such that x = g(x) and |g'(x) < 1|

3. Choose intial guess x0, Tolerable Error e and Maximum Iteration N

4. Initialize iteration counter: step = 1

5. Calculate x1 = g(x0)

6. Increment iteration counter: step = step + 1

7. If step > N then print "Not Convergent" and terminate 

8. Set x0 = x1 for next iteration

9. If |f(x1)| > e then goto step (5) 

10. Display x1 as root.

## Newton's Method
Newton's Method is a root-finding algorithm which produces successively better approximations to the roots of a real-valued function. 

The most basic version starts with a single-variable function f defined for a real variable x, the function's derivative f′, and an initial guess x0 for a root of f. 

If the function satisfies sufficient assumptions and the initial guess is close, then

x1 = x0 - ( f(x0) / f'(x0) )

is a better approximation of the root than x0. Geometrically, (x1, 0) is the intersection of the x-axis and the tangent of the graph of f at (x0, f(x0)):

that is, the improved guess is the unique root of the linear approximation at the initial point. The process is repeated as

x<sub>n+1</sub> = x<sub>n</sub> - ( f(x<sub>n</sub>) / f'(x<sub>n</sub>) )

until a sufficiently precise value is reached.

:memo: **Note:**                                                                                               <br />
The function f(x) should be twice differentiable in the interval.

### Algorithm For Newton's Method
1. Define function as f(x)

2. Define first derivative of f(x) as g(x)

3. Input initial guess (x0), tolerable error (e) 
   and maximum iteration (N)

4. Initialize iteration counter i = 1

5. If g(x0) = 0 then print "Mathematical Error" and terminate 

6. Calcualte x1 = x0 - f(x0) / g(x0)

7. Increment iteration counter i = i + 1

8. If i >= N then print "Not Convergent" and terminate 

9. If |f(x1)| > e then set x0 = x1 and goto (5) 

10. Print root as x1

## Secant's Method
Secant method is also used to solve non-linear equations. This method is similar to the Newton method, 
but here we do not need to find the differentiation of the function f(x). 
Only using f(x), we can find f’(x) numerically by using Newton’s Divide difference formula. 
From the Newton formula, <br />

x<sub>n+1</sub> = x<sub>n</sub> - ( f(x<sub>n</sub>) / f'(x<sub>n</sub>) ) <br />

Now, using divide difference formula, we get, <br />

f'(x<sub>n</sub>) ~  ( f(x<sub>n</sub>) -   f(x<sub>n-1</sub>) ) / ( x<sub>n</sub> - x<sub>n-1</sub> ) <br />

By replacing the f’(x) of Newton-Raphson formula by the new f’(x), we can find the secant formula to solve non-linear equations. <br />

x<sub>n+1</sub> = ( x<sub>n-1</sub> f(x<sub>n</sub>) - x<sub>n</sub> f(x<sub>n-1</sub>) ) / ( f(x<sub>n</sub>) -   f(x<sub>n-1</sub>) )

### Algorithm for Secant's Method
1. Get values of x0, x1 and e <br /> *Here x0 and x1 are the two initial guessese is the stopping criteria and e is absolute error or the desired degree of accuracy*

2. Compute f(x0) and f(x1)

3. Compute x2 = [x0*f(x1) – x1*f(x0)] / [f(x1) – f(x0)]

4. Test for accuracy of x2 <br /> If | (x2 – x1)/x2 | > e <br /> then assign x0 = x1 and x1 = x2 <br /> goto step 3

5. Display the required root as x2
   


# Solving A System Of linear Equations
Extending this repo to also contain different methods to solve a system of equations

## Gauss Elimination Method 
Gaussian elimination is also known as row reduction. It is an algorithm of linear algebra used to solve a system of linear equations. Basically, a sequence of operations is performed on a matrix of coefficients. The operations involved are:

1. Swapping two rows
2. Multiplying a row by a nonzero number
3. Adding a multiple of one row to another row
These operations are performed until the lower left-hand corner of the matrix is filled with zeros, as much as possible.

### Algorithm for Gauss Elimination Method
1. At first, we have imported the necessary libraries we will use in our program.
2. We then asked the user for the number of unknown variables that we store in the variable ‘n’.
3. After that, we created a numpy array ‘a’ of size nx(n+1) and initialized it to zero. We will be storing our augmented matrix in this array.
4. Another array ‘x’ of size n is also created and initialized to zero. We will use this array to store the solution vector.
5. We then used a loop to get the input of the augmented matrix.
6. After that, we applied the Gaussian elimination method.
7. If any of the coefficients is 0, an error is raised as division by zero is not possible.
8. After that, we apply the back substitution method to obtain the desired output.

