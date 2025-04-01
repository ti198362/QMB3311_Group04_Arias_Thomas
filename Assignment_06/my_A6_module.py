"""
##################################################
#
# QMB 3311: Python for Business Analytics
#
# Name: Timothy Arias and Destiny Thomas
#
# Date:03/31/2025
# 
##################################################
#
# Function Definitions
#
##################################################
"""

##################################################
# Import Required Modules
##################################################

import numpy as np
import math
import doctest

##################################################
# Function Definitions
##################################################

# Exercise 1

def ln_taylor(z: float, n: int) -> float: 
    """Calculates the first 'n' terms of the Taylor series approximation of 
    the natural logarithm of 'z'.

    >>> ln_taylor(1.0, 10)
    0.0
    >>> ln_taylor(1.8, 25)
    0.5878523427056109
    >>> ln_taylor(1.5, 15)
    0.4054657568451514
    >>> ln_taylor(1.1, 10)
    0.09531017980349216
    >>> ln_taylor(0, 20)
    Error: z must be strictly positive.
    >>> ln_taylor(1.1, -10)
    Error: n must be a strictly positive integer.
    """
    Error = False
    
    if z <= 0:
        print("Error: z must be strictly positive.")
        Error = True
        
    if n <= 0:
        print("Error: n must be a strictly positive integer.")
        Error = True
    
    if Error:
        return None
    
    approx = 0
    
    for k in range(1, n + 1):
        function = ((-1) ** (k - 1)) * (1 / k) * (z - 1) ** k
        approx += function
        
    return approx


# Exercise 2

def exp_x_diff(x, z):
   """ Function that returns the value of e^x - z
    
    >>> round(exp_x_diff(4, 1), 3)
    53.598
    
    >>> round(exp_x_diff(2, math.e), 3)
    4.671

    >>> round(exp_x_diff(2, 11), 3)
    -3.611
    
   """
   return math.exp(x) - z


# Exercise 3

def ln_z_bisect(z, a_0, b_0, num_iter):
    """Function that approximates ln(z) using the bisection method.
    The method finds a root of f(x) = exp(x) - z within [a_0, b_0].

    >>> round(ln_z_bisect(1, 6, 3, 12), 3)
    Traceback (most recent call last):
    ValueError: Function must have different signs at the endpoints (f(a0) * f(b0) < 0)

    >>> round(ln_z_bisect(math.e, 0, 2, 20), 5)
    Iteration 1: m = 1.0, f(m) = 0.0
    Iteration 2: m = 1.5, f(m) = 1.7634072418790194
    Iteration 3: m = 1.75, f(m) = 3.0363208475466856
    Iteration 4: m = 1.875, f(m) = 3.8025372918710674
    Iteration 5: m = 1.9375, f(m) = 4.22309399273799
    Iteration 6: m = 1.96875, f(m) = 4.443436914034667
    Iteration 7: m = 1.984375, f(m) = 4.556217573771262
    Iteration 8: m = 1.9921875, f(m) = 4.613272179711203
    Iteration 9: m = 1.99609375, f(m) = 4.6419670707773
    Iteration 10: m = 1.998046875, f(m) = 4.656356604613448
    Iteration 11: m = 1.9990234375, f(m) = 4.663561917604852
    Iteration 12: m = 1.99951171875, f(m) = 4.667167213624078
    Iteration 13: m = 1.999755859375, f(m) = 4.668970521890564
    Iteration 14: m = 1.9998779296875, f(m) = 4.669872341135047
    Iteration 15: m = 1.99993896484375, f(m) = 4.670323292040976
    Iteration 16: m = 1.999969482421875, f(m) = 4.670548777815599
    Iteration 17: m = 1.9999847412109375, f(m) = 4.670661523283416
    Iteration 18: m = 1.9999923706054688, f(m) = 4.670717896662461
    Iteration 19: m = 1.9999961853027344, f(m) = 4.670746083513272
    Iteration 20: m = 1.9999980926513672, f(m) = 4.670760176978998
    2.0

    >>> round(ln_z_bisect(1.5, 0, 2, 20), 5)
    Iteration 1: m = 1.0, f(m) = 1.218281828459045
    Iteration 2: m = 0.5, f(m) = 0.1487212707001282
    Iteration 3: m = 0.25, f(m) = -0.2159745833122586
    Iteration 4: m = 0.375, f(m) = -0.04500858538179875
    Iteration 5: m = 0.4375, f(m) = 0.04883029863413313
    Iteration 6: m = 0.40625, f(m) = 0.0011778000001227973
    Iteration 7: m = 0.390625, f(m) = -0.022095804588261547
    Iteration 8: m = 0.3984375, f(m) = -0.010504458321830112
    Iteration 9: m = 0.40234375, f(m) = -0.0046747376017395315
    Iteration 10: m = 0.404296875, f(m) = -0.0017513264842758947
    Iteration 11: m = 0.4052734375, f(m) = -0.0002874783607902387
    Iteration 12: m = 0.40576171875, f(m) = 0.0004449819526823884
    Iteration 13: m = 0.405517578125, f(m) = 7.870709011648103e-05
    Iteration 14: m = 0.4053955078125, f(m) = -0.00010439681042995197
    Iteration 15: m = 0.40545654296875, f(m) = -1.2847654100589523e-05
    Iteration 16: m = 0.405487060546875, f(m) = 3.292901950069371e-05
    Iteration 17: m = 0.4054718017578125, f(m) = 1.0040508076070154e-05
    Iteration 18: m = 0.40546417236328125, f(m) = -1.4036166680053697e-06
    Iteration 19: m = 0.4054679870605469, f(m) = 4.3184347899849485e-06
    Iteration 20: m = 0.40546607971191406, f(m) = 1.457406332505684e-06
    0.40547

    >>> round(ln_z_bisect(2, 1, -1, 10), 5)
    Iteration 1: m = 0.0, f(m) = -1.0
    Iteration 2: m = 0.5, f(m) = -0.3512787292998718
    Iteration 3: m = 0.75, f(m) = 0.11700001661267478
    Iteration 4: m = 0.625, f(m) = -0.13175404256777767
    Iteration 5: m = 0.6875, f(m) = -0.011262530417708083
    Iteration 6: m = 0.71875, f(m) = 0.05186677348797675
    Iteration 7: m = 0.703125, f(m) = 0.020055527708696452
    Iteration 8: m = 0.6953125, f(m) = 0.004335330874331245
    Iteration 9: m = 0.69140625, f(m) = -0.003478832038737778
    Iteration 10: m = 0.693359375, f(m) = 0.0004244339097745353
    0.69238
    
    """
    
    f_a = exp_x_diff(a_0, z)
    f_b = exp_x_diff(b_0, z)
    
    if f_a * f_b >= 0:
        raise ValueError("Function must have different signs at the endpoints (f(a0) * f(b0) < 0)")
                         
    for i in range(1, num_iter + 1):
        m_i = (a_0 + b_0) / 2
        f_m = exp_x_diff(m_i, z)

        print(f"Iteration {i}: m = {m_i}, f(m) = {f_m}")

        if f_a * f_m < 0:
            b_0 = m_i  
            f_b = f_m
        else:
            a_0 = m_i 
            f_a = f_m

    return (a_0 + b_0) / 2
    

# Exercise 4

def exp_x_diff_prime(x, z):
    """Derivative of f(x) = e^x - z with respect to x.
   
   >>> round(exp_x_diff_prime(4, 7), 3)
   54.598

   >>> round(exp_x_diff_prime(0, -3), 3)
   1.0
   
   >>> round(exp_x_diff_prime(30/16, -50), 3)
   6.521
   
   """
    return math.exp(x)


def newton_root_f(x_0, z, tol, num_iter):
    """Uses Newton's method to find root of f(x) = e^x - z.
    
    >>> round(newton_root_f(4, 6, 0.0005, 50),3)
    1.792

    >>> round(newton_root_f(1, math.e, 0.1, 20), 5)
    1.0

    >>> (newton_root_f(1, 0, 0.001, 1))
    Exceeded allowed number of iterations
    
    """
    x_i= x_0
    
    for i in range(num_iter):
        x_i= x_i- exp_x_diff(x_i, z)/ exp_x_diff_prime(x_i, z)
        if abs(exp_x_diff(x_i, z)) < tol:
            
            return x_i
    
    print("Exceeded allowed number of iterations")
    return None
    

# Exercise 5

def ln_z_newton(z, x_0, tol, num_iter):
    """
   Uses Newton's method to estimate ln(z) by solving e^x - z = 0.

   Returns:
   - Approximation of ln(z) if converged
   - Last estimate if not converged

   >>> round(ln_z_newton(4, 5, 0.5, 5), 3)
   Newton-Raphson terminated successfully.
   Estimated ln(z): 1.4276635443782653
   Iterations: 5
   1.428

   >>> round(ln_z_newton(1.88, -3, 0.011, 25), 3)
   Reached max iterations without satisfying tolerance.
   Last estimate of ln(z): 9.76087250993465
   9.761

   >>> round(ln_z_newton(1, -2, 0.00004, 3), 3)
   Reached max iterations without satisfying tolerance.
   Last estimate of ln(z): 2.4347928347280563
   2.435
   """
    x = x_0
    for i in range(num_iter):
        f_val = exp_x_diff(x, z)
        f_prime_val = exp_x_diff_prime(x, z)

        x_next = x - f_val / f_prime_val

    
        if abs(x_next - x) < tol:
            print('Newton-Raphson terminated successfully.')
            print('Estimated ln(z):', x_next)
            print('Iterations:', i + 1)
            return x_next

        x = x_next
        
    print("Reached max iterations without satisfying tolerance.")
    print('Last estimate of ln(z):', x)
    
    return x


# Exercise 6

def exp_x_fp_fn(x: float, z: float) -> float:
    """
    Function to compute g(x) for a given z based on the equation:
    g(x) = 1/2 * (z - e^x + 2x)
        
    >>> exp_x_fp_fn(0.5, 2)
    0.6756393646499359
    >>> exp_x_fp_fn(0, 2)
    0.5
    >>> exp_x_fp_fn(1, 3)
    1.1408590857704775
    >>> exp_x_fp_fn(0.5, 1.5)
    0.4256393646499359
    """
    
    g_x = 0.5 * (z - math.exp(x) + 2 * x)
    
    return g_x


# Exercise 7















##################################################
# Examples
##################################################


doctest.testmod()


##################################################
# End
##################################################






    
