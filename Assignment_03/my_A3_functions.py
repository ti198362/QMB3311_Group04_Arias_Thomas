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

# Boolean



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
    if x >= 0 and y >=0 and r > 0:
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






##################################################
# Run the examples to test these functions
##################################################

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


print("#" + 50*"-")
print("Testing my Examples for Exercise 2.")




    
