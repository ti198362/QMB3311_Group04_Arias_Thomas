# -*- coding: utf-8 -*-
"""
##################################################
#
# QMB 3311: Python for Business Analytics
#
# Name: Destiny Thomas and Timothy Arias
#
# Date: 02/17/2024
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

##################################################
# Function Definitions
##################################################

# Only function definitions here - no other calculations. 

# Exercise 1


# Exercise 2
def logit(x, b0, b1):
    """Logistic function."""
    answer= (math.exp(b0 + b1 * x)) / (1 + math.exp((b0 + b1 * x)))
    return answer

def logit_like(yi, xi, b0, b1):
    """Computes the log-likelihood for a single observation."""
    p = logit(xi, b0, b1)
    if yi not in[0,1]:
        print("Error:Invalid yi value. Must be 0 or 1.")
        return None
    if yi == 1:
        return math.log(p)
    else:
        return math.log(1 - p)

def logit_like_sum(y, x, b0, b1):
    """Computes the sum of log-likelihoods across all observations.
    
    >>>logit_like_sum([1, 0, 1], [2, 4, -3], 0.5, 0.8)
    -5.8793
    >>>logit_like_sum([0, 0, 1], [10/11, 2/4, -3], 3, 0.2)
    -6.4534
    >>>logit_like_sum([3, 0, 1], [1, 4/3, -3], 1, -0.8)
    None
    
    """
    total = 0
    for i in range(len(y)):
        log_likelihood = logit_like(y[i], x[i], b0, b1)
        if log_likelihood is None:
            return None  
        total += log_likelihood
    return total

# Exercise 3


def logit_like_grad(y: list, x: list, beta_0: float, beta_1: float) -> float:
    """Calculates the gradient vector of the likelihood function
    for the bivariate logistic regression model
    for sevaral pairs of observations in the lists x and y,
    coefficients beta_0 and beta_1.
    
    Notice if you are missing the space after the >>>, 
    it causes an error.
    Also, an example without the >>> does not get run with doctest.
    
    >>> logit_like_grad([1, 1, 0, 0], [15.0, 5.0, 15.0, 5.0], 0.0, 0.0)
    [0.0, 0.0]
    >>> logit_like_grad([1, 1, 0, 0], [15.0, 5.0, 15.0, 5.0], math.log(3), 0.0)
    [-1.0, -10.0]
    >>> logit_like_grad([1, 1, 0, 0], [15.0, 5.0, 15.0, 5.0], math.log(7), 0.0)
    [-1.5, -15.0]
    >>> logit_like_grad([1, 0, 1], [1, 1, 1], 0.0, math.log(2))
    [0.0, 0.0]
    >>> logit_like_grad([1, 0, 1], [1, 1, 1], 0.0, math.log(5))
    [-0.5, -0.5]
    >>> logit_like_grad([1, 0, 1], [3, 3, 3], 0.0, math.log(2))
    [-2/3, -2.0]
    """
    
    return None


# Exercise 4

def CESutility_multi(x: list, a: list, r: float) -> float:
    """Returns the value of the Constant Elasticity of Substitution using the
    utility function, which measure the theoretical degree of satisfaction a
    consumer may get from more than two goods.

    x is a vector of quantities of goods consumed.
    a is a vector of weighting parameters for each good.
    i is the subscript that indicates the ith element of each vector
    r is the parameter that represents the degree to which the goods 
    are complements or substitutes.
    
    >>> CESutility_multi([2, 4, 6], [8, 10, 12], 0.2)
    353.8099...
    >>> CESutility_multi([-2, 4, 6], [8, 10, 12], 0)
    Error: Elements of x should be non-negative numbers only.
    Error: r should be a strictly positive number.
    None
    >>> CESutility_multi([2, 4, 6], [8, 10, 12, 14], 0.2)
    Error: x and a should have the same number of elements.    
    None
    """    
    Error = False
    if len(x) != len(a):
        print("Error: x and a should have the same number of elements.")
        Error = True
    
    if Error:
        return None
    
    for i in range(len(x)):
        if x[i] < 0:
            print("Error: Elements of x should be non-negative numbers only.")
            Error = True       
        if a[i] < 0:
            print("Error: Elements of a should be non-negative numbers only.")
            Error = True     
    if r <= 0:
        print("Error: r should be a strictly positive number.")
        Error = True
        
    if Error:
        return None
    
    inside = 0
    for i in range(len(x)):
        inside += (a[i] ** (1 - r)) * (x[i] ** r)
    return inside ** (1 / r)



# Only function definitions above this point. 


##################################################
# Test the examples in your docstrings
##################################################
# Exercise 1 Example
print("#" + 50*"-")
print("Testing my Examples for Exercise 1.")

print("#" + 50*"-")
print("Exercise 1, Example 1:")
print("Evaluating matrix_inverse(np.array([[4, 1],[3, 1]]))")
print("Expected: " + str([[1, -1], [-3, 4]]))
print("Got: " + str(matrix_inverse(np.array([[4, 1],[3, 1]]))))

print("#" + 50*"-")
print("Exercise 1, Example 2:")
print("Evaluating matrix_inverse(np.array([[1/2, 2], [4/5, -11]]))")
print("Expected: " + str([[1.5493, 0.2817], [0.1127, -0.0704]]))
print("Got: " + str(matrix_inverse(np.array([[1/2, 2], [4/5, -11]]))))

print("#" + 50*"-")
print("Exercise 1, Example 3:")
print("Evaluating matrix_inverse(np.array([[2, 3, 1], [5, 4, 2]])")
print("Expected: " + str(None))
print("Got: " + str(matrix_inverse(np.array([[2, 3, 1], [5, 4, 2]]))))

# Exercise 2 Example

print("#" + 50*"-")
print("Testing my Examples for Exercise 2.")

print("#" + 50*"-")
print("Exercise 1, Example 1:")
print("Evaluating logit_like_sum([1, 0, 1], [2, 4, -3], 0.5, 0.8)")
print("Expected: " + str(-5.8793))
print("Got: " + str(logit_like_sum([1, 0, 1], [2, 4, -3], 0.5, 0.8)))

print("#" + 50*"-")
print("Exercise 1, Example 2:")
print("Evaluating logit_like_sum([0, 0, 1], [10/11, 2/4, -3], 3, 0.2)")
print("Expected: " + str(-6.4534))
print("Got: " + str(logit_like_sum([0, 0, 1], [10/11, 2/4, -3], 3, 0.2)))

print("#" + 50*"-")
print("Exercise 1, Example 3:")
print("Evaluating logit_like_sum([3, 0, 1], [1, 4/3, -3], 1, -0.8)")
print("Expected: " + str(None))
print("Got: " + str(logit_like_sum([3, 0, 1], [1, 4/3, -3], 1, -0.8)))

# Exercise 3 Example




# Exercise 4 Example
print("#" + 50*"-")
print("Testing my Examples for Exercise 4.")

print("#" + 50*"-")
print("Exercise 4, Example 1:")
print("Evaluating CESutility_multi([2, 4, 6], [8, 10, 12], 0.5)")
print("Expected: " + str(353.81))
print("Got: " + str(CESutility_multi([2, 4, 6], [8, 10, 12], 0.5)))

print("#" + 50*"-")
print("Exercise 4, Example 1:")
print("Evaluating CESutility_multi([-2, 4, 6], [8, 10, 12], 0)")
print("Expected: " + str(None))
print("Got: " + str(CESutility_multi([-2, 4, 6], [8, 10, 12], 0)))

print("#" + 50*"-")
print("Exercise 4, Example 1:")
print("Evaluating CESutility_multi([2, 4, 6], [8, 10, 12, 14], 0.5)")
print("Expected: " + str(None))
print("Got: " + str(CESutility_multi([2, 4, 6], [8, 10, 12, 14], 0.5)))


# Question 2: Test using the doctest module. 


# Make sure to include examples in your docstring
# with the proper formatting. 

# Test all functions with three examples each. 

# Choose good examples that will test interesting cases. 
# Make sure they all work correctly. 




##################################################
# End
##################################################

