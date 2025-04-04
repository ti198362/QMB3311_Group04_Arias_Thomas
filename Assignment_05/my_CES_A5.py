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

import numpy as np
import doctest

##################################################
# Function Definitions
##################################################

#--------------------------------------------------
# Question 1
# Functions from Previous Assignments
#--------------------------------------------------
def CESutility(good_x: float, good_y: float, r: float):
    """Calculate the constant elasticity of subsitution utility function for two goods.
    
    >>> CESutility(3, 4, 2)
    5.0
    >>> CESutility(1, 1, 2)
    1.41
    >>> CESutility(3**0.5, 4**0.5, 4)
    2.24
    """
    
    utility = (good_x**r + good_y**r)**(1/r)
    return round(utility, 2)

help(CESutility)
 
def CESutility_valid(x:float, y:float, r:float):
    """Returns the value of the Constant Elasticity of Substitution using the
    utility function, which measure the theoretical degree of satisfaction a
    consumer may get from two goods.
    
    x represents good one.
    y represent good two.
    r is the parameter that represents the degree to which the goods 
    are complements or substitutes.
    
    >>> (CESutility_valid(5, 5, 0.20))
    160.0
    >>> (CESutility_valid(-10, 10, -0.10))
    Error: x should be a non-negative number.
    Error: r should be a strictly positive number.
    
    >>> (CESutility_valid(5, -5, 0.20))
    Error: y should be a non-negative number.
   
    """
    if x >= 0 and y >= 0 and r > 0:
        answer = CESutility(x, y, r)
        return answer
    if x < 0:
        print("Error: x should be a non-negative number.")
    if y < 0:
        print("Error: y should be a non-negative number.")
    if r <= 0:
       print ("Error: r should be a strictly positive number.")
    return None                  

help(CESutility_valid)


def CESutility_in_budget(x:float, y:float, r:float, p_x:float, p_y:float, w:float):
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
    160.0
    >>> (CESutility_in_budget(-10, 10, 0, 5, 10, 20))
    Error in CESutility_in_budget: budget constraint not satisfied.
    >>> CESutility_in_budget(15, 20, 0.20, 3, 9, 224)
    Error in CESutility_in_budget: budget constraint not satisfied.
    
    """
    if (p_x <= 0) or (p_y <= 0):
        print('Error in CESutility_in_budget: prices cannot be negative or zero.')
        return None
    elif p_x*x + p_y*y > w:
       # print('Error in CESutility_in_budget: budget constraint not satisfied.')
        return None
    else :
        return CESutility_valid(x, y, r)

help(CESutility_in_budget)

if __name__== "__main__":
    doctest.testmod(verbose= True)
   
#--------------------------------------------------
# Question 2
# New Functions
#--------------------------------------------------

#Problem 1
def CESdemand_calc(r, p_x, p_y, w): # expected input/output?
    """ Formula that returns a list of two values [x star,y star] that achieve
    the maximum value of CES utility 
    
    >>> CESdemand_calc(5, 10, 12, 200)
    [8.87, 9.28]
    
    >>> CESdemand_calc(10, 5, 5, 250)
    [25.0, 25.0]
    
    >>> CESdemand_calc(-1.5, 2, 5, 100)
    Error: r should be a strictly positive number.
    
    >>> CESdemand_calc(1.5, -2, 5, 100)
    Error: Prices must be strictly positives
    
    >>> CESdemand_calc(1.5, 2, 5, -100)
    Error: Budget must be strictly positive
    
    """
    if r <= 0:
       print ("Error: r should be a strictly positive number.") 
       return None
    
    if p_x <= 0 or p_y <= 0:
        print ("Error: Prices must be strictly positives")
        return None
    
    
    if w <= 0:
        print ("Error: Budget must be strictly positive")
        return None
    
    
    denominator= (p_x**(r/(r-1))) + (p_y**(r/(r-1)))
    x_star= p_x **(1/ (r-1)) /denominator * w
    y_star= p_y **(1/ (r-1)) /denominator * w

    return [round(x_star, 2), round(y_star, 2)]

help(CESdemand_calc)

if __name__ == "__main__":
    doctest.testmod(verbose= True)

def max_CES_xy(x_min,x_max, y_min, y_max, step, r, p_x, p_y, w): # expected input/output?
    """Finds the values of x and y that maximize CESutility under
    the budget constraint.
    
    >>> max_CES_xy(0, 10, 0, 10, 1, 0.5, 2, 3, 20)
    [7,2]
    
    
    >>> max_CES_xy(0, 5, 0, 5, 0.5, 0.8, 1, 2, 10)
    [4.0, 3.0]

    
    >>> max_CES_xy(1, 10, 1, 10, 1, 0.5, 10, 15, 5)
    Error in CESutility_in_budget: budget constraint not satisfied.
    
    """
  
    x_list= np.arange(x_min, x_max, step)
    y_list= np.arange(y_min, y_max, step)
   
    max_CES=float("-inf")
    i_max= None
    j_max= None
   
    for i in range(len(x_list)):
        for j in range(len(y_list)):
            CES= CESutility_in_budget(x_list[i], y_list[j], r, p_x, p_y, w)
           
            if CES is not None and CES > max_CES:
                i_max= i
                j_max= j
                max_CES = CES
            
            if i_max is None or j_max is None:
                return None
    
    return [x_list[i_max], y_list[j_max]]

help(max_CES_xy)

if __name__== "__main__":
    doctest.testmod()

##################################################
# End
##################################################
