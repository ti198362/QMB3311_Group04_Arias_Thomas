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


# Exercise 1

def matrix_inverse(mat_in):
    """Function that calculates the inverse of a two-by-two matrix
    
    Inputs: mat_in(numpy.array): A 2x2 NumPy array.

    Returns: numpy.array: A 2x2 NumPy array (the inverse of the input matrix).
             None: None if the matrix is not invertible (determinant = 0).
    
    >>> matrix_inverse(np.array([[4, 1], [3, 1]]))
    ([[1, -1], [-3, 4]])
    >>> matrix_inverse(np.array([[1/2, 2], [4/5, -11]]))
    ([[1.5493, 0.2817], [0.1127, -0.0704]])
    >>> matrix_inverse(np.array([[2, 3, 1], [5, 4, 2]]))
    None
    
    """
    if mat_in.shape != (2, 2):
        print("Error: Input must be a 2x2 matrix.")
        return None
    
    det = mat_in[0, 0] * mat_in[1, 1] - mat_in[0, 1] * mat_in[1, 0]
    
    if det == 0:
        print("Error: Determinant cannot be zero")
        return None
    
    mat_out = np.zeros((2, 2))
    
    for i in range(2):
        for j in range(2):
            if i == j:
                mat_out[i, j] = mat_in[1 - i, 1 - j] / det
            else:
                mat_out[i, j] = -mat_in[1 - j, 1 - i] / det
     
    if np.all(mat_out == np.floor(mat_out)):
        return mat_out.astype(int)
    return mat_out

help(matrix_inverse)

# Exercise 2

def logit(x, b0, b1):
    """Logistic function."""
    answer = (math.exp(b0 + b1 * x)) / (1 + math.exp((b0 + b1 * x)))
    return answer

def logit_like(yi, xi, b0, b1):
    """Computes the log-likelihood for a single observation."""
    p = logit(xi, b0, b1)
    if yi not in[0,1]:
        print("Error: Invalid y[i] value. Must be 0 or 1.")

help(matrix_inverse)    

# Exercise 2

def logit(x, b0, b1,)-> float: 
    """Formula to calculate the logit link function
    
    Inputs:
    - x: A numerical predictor value.
    - b0: A numerical intercept value.
    - b1: A numerical coefficient value.

    Returns: A float between 0 and 1 (the probability).
    
    
    >>>(logit(2, 0.5, 0.8))
    0.8909
    >>>(logit(1/2, 4/5, 3/2 ))
    0.8249
    >>>(logit(-3, 4, -7))
    0.9999...
    """
    answer= (math.exp(b0 + b1 * x)) / (1 + math.exp((b0 + b1 * x)))

    return answer
 
help(logit)   
  
def logit_like(y, x, b0, b1) -> float: 
    """For each i observation yi equals 1 if the event occurred
    For each i observation yi equals 0 if the event did not occurred
    
    Inputs: y: A value (0 or 1) representing whether an event occurred.
            x: A numerical predictor value.
            b0: A numerical intercept value.
            b1: A numerical coefficient value.

    Returns: A float (log-likelihood value).
             None if y is not 0 or 1.

    >>>(logit_like(1, 2, 0.5, 0.8))
    -0.1155
    >>>(logit_like(0, 4, 0.7, 1/2))
    -2.7650
    >>>(logit_like(-1, 3, 1/2, 2))
    None

   """
    
    if y not in[0,1]:
        print("Error:Invalid y value. Must be 0 or 1.")
        return None
   
    p = logit(x, b0, b1)
   
    if y == 1:
        return math.log(p)
    else:
        return math.log(1 - p)

help(logit_like)

def logit_like_sum(y, x, b0, b1):
    """Computes the sum of log-likelihoods across all observations.
    
    Inputs: y: A list or NumPy array of 0s and 1s.
            x: A list or NumPy array of predictor values.
            b0: The intercept of the model.
            b1: The coeffiecient of the model.

    Returns: A float (sum of log-likelihoods)
             None if any y value is not 0 or 1
    
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

help(logit_like_sum)


# Exercise 3
    
def logit_like_grad(y: list, x: list, beta_0: float, beta_1: float) -> float:
    """Calculates the gradient vector of the likelihood function
    for the bivariate logistic regression model
    for sevaral pairs of observations in the lists x and y,
    coefficients beta_0 and beta_1.
        
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
    b_0 = 0
    b_1 = 0
    
    for i in range(len(y)):
        p = logit(x[i], beta_0, beta_1)
        if y[i] == 1:
            b_0 += (1 - p)
            b_1 += x[i] * (1 - p)
        elif y[i] == 0:
            b_0 += (-p)
            b_1 += (-x[i] * p)
        else:
            print("Error: Values input for y should equal 0 or 1.")
            return None
    return [b_0, b_1]


help (logit_like_grad)


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
print("#" + 50*"-")
print("Testing my Examples for Exercise 1.")

print("#" + 50*"-")
print("Exercise 1, Example 1:")
print("Evaluating matrix_inverse(np.array([[4, 1],[3, 1]]))")
print("Expected: " + str([[1, -1], [-3, 4]]))
print("Got: " + str(matrix_inverse(np.array([[4, 1],[3, 1]]))))

print("#" + 50*"-")
print("Exercise 1, Example 2:")
print("Evaluating matrix_inverse(np.array([[2, 4], [1, 2]]))")
print("Expected: " + str(None))
print("Got: " + str(matrix_inverse(np.array([[2, 4], [1, 2]]))))

print("#" + 50*"-")
print("Exercise 1, Example 3:")
print("Evaluating matrix_inverse(np.array([[2, 3, 1], [5, 4, 2]])")
print("Expected: " + str(None))
print("Got: " + str(matrix_inverse(np.array([[2, 3, 1], [5, 4, 2]]))))

# Exercise 2 Examples
print("#" + 50*"-")
print("Testing my Examples for Exercise 2.")

print("#" + 50*"-")
print("Exercise 2, Example 1:")
print("Evaluating logit_like_sum([1, 0, 1], [2, 4, -3], 0.5, 0.8)")
print("Expected: " + str(-5.8793))
print("Got: " + str(logit_like_sum([1, 0, 1], [2, 4, -3], 0.5, 0.8)))

print("#" + 50*"-")
print("Exercise 2, Example 2:")
print("Evaluating logit_like_sum([0, 0, 1], [10/11, 2/4, -3], 3, 0.2)")
print("Expected: " + str(-6.4534))
print("Got: " + str(logit_like_sum([0, 0, 1], [10/11, 2/4, -3], 3, 0.2)))

print("#" + 50*"-")
print("Exercise 2, Example 3:")
print("Evaluating logit_like_sum([3, 0, 1], [1, 4/3, -3], 1, -0.8)")
print("Expected: " + str(None))
print("Got: " + str(logit_like_sum([3, 0, 1], [1, 4/3, -3], 1, -0.8)))

# Exercise 3 Examples
print("#" + 50*"-")
print("Testing my Examples for Exercise 3.")

print("#" + 50*"-")
print("Exercise 3, Example 1:")
print("Evaluating logit_like_grad([1, 1, 0, 0], [15.0, 5.0, 15.0, 5.0], 0.0, 0.0))")
print("Expected: " + str("[0.0, 0.0]"))
print("Got: " + str(logit_like_grad([1, 1, 0, 0], [15.0, 5.0, 15.0, 5.0], 0.0, 0.0)))

print("#" + 50*"-")
print("Exercise 3, Example 2:")
print("Evaluating logit_like_grad([1, 2, 0, 0], [15.0, 5.0, 15.0, 5.0], 0.0, 0.0))")
print("Expected: " + str(None))
print("Got: " + str(logit_like_grad([1, 2, 0, 0], [15.0, 5.0, 15.0, 5.0], 0.0, 0.0)))

print("#" + 50*"-")
print("Exercise 3, Example 3:")
print("Evaluating logit_like_grad([1, 1, 0, 0], [15.0, 5.0, 15.0, 5.0], math.log(7), 0.0)")
print("Expected: " + str("[-1.5, -15.0]"))
print("Got: " + str(logit_like_grad([1, 1, 0, 0], [15.0, 5.0, 15.0, 5.0], math.log(7), 0.0)))

# Exercise 4 Examples
print("#" + 50*"-")
print("Testing my Examples for Exercise 4.")

print("#" + 50*"-")
print("Exercise 4, Example 1:")
print("Evaluating CESutility_multi([2, 4, 6], [8, 10, 12], 0.5)")
print("Expected: " + str(353.81))
print("Got: " + str(CESutility_multi([2, 4, 6], [8, 10, 12], 0.5)))

print("#" + 50*"-")
print("Exercise 4, Example 2:")
print("Evaluating CESutility_multi([-2, 4, 6], [8, 10, 12], 0)")
print("Expected: " + str(None))
print("Got: " + str(CESutility_multi([-2, 4, 6], [8, 10, 12], 0)))

print("#" + 50*"-")
print("Exercise 4, Example 3:")
print("Evaluating CESutility_multi([2, 4, 6], [8, 10, 12, 14], 0.5)")
print("Expected: " + str(None))
print("Got: " + str(CESutility_multi([2, 4, 6], [8, 10, 12, 14], 0.5)))


##################################################
# End
##################################################

