"""
##################################################
#
# QMB 3311: Python for Business Analytics
#
# Name: Timothy Arias and Destiny Thomas
#
# Date:03/14/2025
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

import math
import doctest

##################################################
# Function Definitions
##################################################

#--------------------------------------------------
# Question 1
# Functions from Previous Assignments
#--------------------------------------------------

def logit(x: float, beta_0: float, beta_1: float) -> float:
    """Formula to calculate the logit link function
    
    >>> (logit(2, 0.5, 0.8))
    0.8909031788043871
    >>> (logit(1/2, 4/5, 3/2 ))
    0.8249137318359602
    >>> (logit(-3, 4, -7))
    0.9999999999861121
    """
    answer = (math.exp(beta_0 + beta_1 * x)) / (1 + math.exp((beta_0 + beta_1 * x)))

    return answer

def logit_like(yi: float, xi: float, b0: float, b1: float) -> float:
    """For each i observation yi equals 1 if the event occurred
    For each i observation yi equals 0 if the event did not occurred 

    >>> (logit_like(1, 2, 0.5, 0.8))
    -0.11551952317975495
    >>> (logit_like(0, 4, 0.7, 1/2))
    -2.7650435617765905
    >>> (logit_like(-1, 3, 1/2, 2))
    Error: y[i] must be equal to 0 or 1.
    """
    Error = False
    
    if yi != 0 and yi != 1:
        print("Error: y[i] must be equal to 0 or 1.")
        Error = True
    
    if Error == True:
        return None
        
    p = logit(xi, b0, b1) 
    
    if yi == 1:
        return math.log(p)

    elif yi == 0:
        return math.log(1-p)
    else:
        return None

def logit_like_sum(y: list, x: list, b0: float, b1: float)-> float:
    """Computes the sum of log-likelihoods across all observations.
        
    >>> logit_like_sum([1, 0, 1], [2, 4, -3], 0.5, 0.8)
    -5.879329127396495
    >>> logit_like_sum([0, 0, 1], [10/11, 2/4, -3], 3, 0.2)
    -6.4533899941288855
    >>> logit_like_sum([3, 0, 1], [1, 4/3, -3], 1, -0.8)
    Error: y[i] must be equal to 0 or 1.
    """
    Error = False
    if len(x) != len(y):
        print("Error: x and y should have the same number of elements.")
        Error = True
    
    if Error:
        return None

    total = 0
    
    for i in range(len(y)):
        log_likelihood = logit_like(y[i], x[i], b0, b1)
        if log_likelihood is None:
            return None  
        total += log_likelihood
    return total


#--------------------------------------------------
# Question 2
# New Functions
#--------------------------------------------------

# Exercise 1

def logit_d_i(x_i: float, k: int)-> float:
    """A helper function that helps calculate the term d_i in 
    the gradient vector.
    
    >>> logit_d_i(5, 0)
    1
    >>> logit_d_i(10, 1)
    10
    >>> logit_d_i(2, 5)
    Undefined: k should equal to 0 or 1.
    """
    if k == 0:
        return 1 
    if k == 1:
        return x_i
    else:
        print("Undefined: k should equal to 0 or 1.")
        return None


# Exercise 2

def logit_dLi_dbk(y_i: int, x_i:float, k: int, beta_0: float, beta_1: float) -> float:
    """A helper function that helps calculate an individual term in the
    sum of the gradient vector.
    >>> logit_dLi_dbk(1, 2, 0, 0.5, 0.5)
    0.18242552380635635
    >>> logit_dLi_dbk(0, 2, 1, 0.5, 0.5)
    -1.6351489523872873
    >>> logit_dLi_dbk(3, 2, 3, 0.5, 0.5)
    Undefined: k should equal to 0 or 1.
    Error y_i must equal 0 or 1.
    """
    p = logit(x_i, beta_0, beta_1)
   
    d_i = logit_d_i(x_i, k)
   
    if y_i == 1:
        return d_i * (1 - p) if d_i is not None else None
    elif y_i == 0:
        return d_i * (-p) if d_i is not None else None
    else:
        print("Error y_i must equal 0 or 1.")
        return None



doctest.testmod()



##################################################
# End
##################################################


