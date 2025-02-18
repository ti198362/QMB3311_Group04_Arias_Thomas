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
    utility function, which measures the theoretical degree of satisfaction a
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


help (CESutility_multi)


##################################################
# Test the examples in your docstrings
##################################################

# Exercise 1 Examples


# Exercise 2 Examples


# Exercise 3 Examples


# Exercise 4 Examples
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



##################################################
# End
##################################################

