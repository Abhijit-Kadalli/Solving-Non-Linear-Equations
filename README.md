# Solving Non Linear Equations
This repo contains code for solving non linear equations (with single variable for now)

## Theorem
An equation f (x) = 0 , where f (x) is a real continuous function, has at least one root
between x=a and x=b if f(a) f(b) < 0 .

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
|∈~a~| = (  |m<sup>new</sup>  -  m<sup>old</sup> |  /  |m<sup>old</sup>|  ) * 100                           <br />
m<sup>new</sup> = estimated root from present iteration                                                     <br />
m<sup>old</sup> = estimated root from previous iteration                                                    <br />

5. Compare the absolute relative approximate error ∈a with the pre-specified relative error tolerance ∈s .  <br />
If ∈a >∈s , then go to Step 3, else stop the algorithm .                                                    <br />      

:memo: **Note:** We have to also check whether the number of iterations is more than the maximum number of iterations allowed. <br />
If so, one needs to terminate the algorithm and notify the user about it.

## Fixed Point Iteration Method 
