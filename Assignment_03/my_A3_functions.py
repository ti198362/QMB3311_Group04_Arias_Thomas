# -*- coding: utf-8 -*-
"""
##################################################
#
# QMB 3311: Python for Business Analytics
#
# Name: Timothy Arias and Destiny Thomas
#
# Date:02/03/2025
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


##################################################
# Function Definitions
##################################################

#Exercise 1

def CESutility_valid(x, y, r)-> float:
    """Returns the value of the Constant Elasticity of Substitution using the
    utility function, which measure the theoretical degree of satisfaction a
    consumer may get from two goods.
    
    x represents good one.
    y represent good two.
    r is the parameter that represents the degree to which the goods 
    are complements or substitutes.
    
    >>> (CESutility_valid(5, 5, 0.20))
    160
    >>> (CESutility_valid(-10, 10, -0.10))
    Error: x should be a non-negative number.
    Error: r should be a strictly positive number.
    None
    >>> (CESutility_valid(5, -5, 0.20))
    Error: y should be a non-negative number.
    None
    """
    if x >= 0 and y >= 0 and r > 0:
        answer = (x ** r + y ** r) ** (1/r)
        return answer
    if x < 0:
        print("Error: x should be a non-negative number.")
    if y < 0:
        print("Error: y should be a non-negative number.")
    if r <= 0:
       print ("Error: r should be a strictly positive number.")
    return None  
                 
help(CESutility_valid)


# Exercise 2

def CESutility_in_budget(x, y, r, p_x, p_y, w)-> float:
    """Returns the value of the Constant Elasticity of Substitution using the
    utility function, which measure the theoretical degree of satisfaction a
    consumer may get from two goods within a budget constraint.
    
    x represents good one.
    y represent good two.
    r is the parameter that represents the degree to which the goods 
    are complements or substitutes.
    p_x is the price of good x.
    p_y is the price of good y.
    w is the budget/wealth of the consumer.
    
    
    >>> (CESutility_in_budget(5, 5, 0.20, 2, 6, 45))
    160
    >>> (CESutility_in_budget(-10, 10, 0, 5, 10, 20)
    Error: x should be a non-negative number.
    Error: r should be a strictly positive number.
    Error: The price of the basket of goods is greater than the consumer's budget constraint.
    None
    >>> CESutility_in_budget(15, 20, 0.20, 3, 9, 224)
    Error: The price of the basket of goods is greater than the consumer's budget constraint.
    None
    """
    if x >= 0 and y >= 0 and r > 0 and w >= ((p_x * x) + (p_y * y)):
        answer = (x ** r + y ** r) ** (1/r)
        return answer
    if x < 0:
        print("Error: x should be a non-negative number.")
    if y < 0:
        print("Error: y should be a non-negative number.")
    if r <= 0:
       print ("Error: r should be a strictly positive number.")
    if w <= (p_x * x) + (p_y * y):
        print ("Error: The price of the basket of goods is greater than the consumer's budget constraint.")
    return None

help(CESutility_in_budget)


# Exercise 3

def logit(x, b0, b1,)-> float:
    """Formula to calculate the logit link function
    
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

# Exercise 4

def logit_like(yi, xi, b0, b1) -> float: 
    """For each i observation yi equals 1 if the event occurred
    For each i observation yi equals 0 if the event did not occurred 

    >>>(logit_like(1, 2, 0.5, 0.8))
    -0.1155
    >>>(logit_like(0, 4, 0.7, 1/2))
    -2.7650
    >>>(logit_like(-1, 3, 1/2, 2))
    None

   """
    p=logit(xi, b0, b1,)
    
    if yi == 1:
        return math.log(p)

    elif yi == 0:
        return math.log(1-p)

    else:
        return (None)

##################################################
# Run the examples to test these functions
##################################################

# Exercise 1 Examples

print("#" + 50*"-")
print("Testing my Examples for Exercise 1.")

print("#" + 50*"-")
print("Exercise 1, Example 1:")
print("Evaluating CESutility_valid(5, 5, 0.2)")
print("Expected: " + str(160))
print("Got: " + str(CESutility_valid(5, 5, 0.2)))

print("#" + 50*"-")
print("Exercise 1, Example 2:")
print("Evaluating CESutility_valid(-10, 10, -0.5)")
print("Expected: " + str(None))
print("Got: " + str(CESutility_valid(-10, 10, -0.5)))

print("#" + 50*"-")
print("Exercise 1, Example 3:")
print("Evaluating CESutility_valid(5, -5, 0.2)")
print("Expected: " + str(None))
print("Got: " + str(CESutility_valid(5, -5, 0.2)))

# Exercise 2 Examples

print("#" + 50*"-")
print("Testing my Examples for Exercise 2.")

print("#" + 50*"-")
print("Exercise 2, Example 1:")
print("Evaluating CESutility_in_budget(5, 5, 0.20, 2, 6, 45)")
print("Expected: " + str(160))
print("Got: " + str(CESutility_in_budget(5, 5, 0.20, 2, 6, 45)))

print("#" + 50*"-")
print("Exercise 2, Example 2:")
print("Evaluating CESutility_in_budget(-10, 10, 0, 5, 10, 20)")
print("Expected: " + str(None))
print("Got: " + str(CESutility_in_budget(-10, 10, 0, 5, 10, 20)))

print("#" + 50*"-")
print("Exercise 2, Example 3:")
print("Evaluating CESutility_in_budget(15, 20, 0.20, 3, 9, 224)")
print("Expected: " + str(None))
print("Got: " + str(CESutility_in_budget(15, 20, 0.20, 3, 9, 224)))



# Exercise 3 Examples
print("#" + 50*"-")
print("Testing my Examples for Exercise 3.")

print("#" + 50*"-")
print("Exercise 3, Example 1:")
print("Evaluating logit(2, 0.5 ,0.8)")
print("Expected: " + str(0.8909))
print("Got: " + str(logit(2, 0.5 ,0.8)))

print("#" + 50*"-")
print("Exercise 3, Example 2:")
print("Evaluating logit(1/2, 4/5, 3/2 )")
print("Expected: " + str(0.8249))
print("Got: " + str(logit(1/2, 4/5, 3/2)))

print("#" + 50*"-")
print("Exercise 3, Example 3:")
print("Evaluating logit(-3, 4, -7)")
print("Expected: " + str(0.9999))
print("Got: " + str(logit(-3, 4, -7)))

# Exercise 4 Example
print("#" + 50*"-")
print("Testing my Examples for Exercise 4.")

print("#" + 50*"-")
print("Exercise 4, Example 1:")
print("Evaluating logit_like(1, 2, 0.5 ,0.8)")
print("Expected: " + str(-0.1155))
print("Got: " + str(logit_like(1 , 2 , 0.5, 0.8)))
 
print("#" + 50*"-")
print("Exercise 4, Example 2:")
print("Evaluating logit_like(1/2, 4/5, 3/2 )")
print("Expected: " + str(-2.7650))
print("Got: " + str(logit_like(0, 4, 0.7, 1/2)))

print("#" + 50*"-")
print("Exercise 4, Example 3:")
print("Evaluating logit_like(-1, 3, 1/2, 2)")
print("Expected: " + str(None))
print("Got: " + str(logit_like(-1, 3, 1/2, 2)))

