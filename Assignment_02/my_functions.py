# Script: my_functions.py
# Authors: Timothy Arias and Destiny Thomas
# Date: Jan 20 2025

# Exercise 1

def present_value(cash_flow: float, interest_rate: float, num_yrs: float) -> float:
    """Return the present value of cash_flow expected num_yrs from now
    discounted at interest_rate.

    >>> present_value(300, 0.30, 3)
    136.549
    >>> present_value(200, 0.10, 2)
    165.289
    >>> present_value(1000, 0.50, 2)
    444.444
    """
    
    # needs either a precondition or checks to make sure that variables are not negative (-1)
    
    answer = cash_flow/(1 + interest_rate) ** num_yrs

    return answer

help(present_value)

print("#" + 50*"-")
print("Testing my Examples for Exercise 1.")

print("#" + 50*"-")
print("Exercise 1, Example 1:")
print("Evaluating present_value(300, 0.30, 3)")
print("Expected: " + str(136.549))
print("Got: " + str(present_value(300, 0.30, 3)))

print("#" + 50*"-")
print("Exercise 1, Example 2:")
print("Evaluating present_value(200, 0.10, 2)")
print("Expected: " + str(165.289))
print("Got: " + str(present_value(200, 0.10, 2))) 

print("#" + 50*"-")
print("Exercise 1, Example 3:")
print("Evaluating present_value(1000, 0.50, 2)")
print("Expected: " + str(444.444))
print("Got: " + str(present_value(1000, 0.50, 2)))



# Exercise 2

def future_value(cash_flow,interest_rate,num_of_yrs)-> float:
    """Return the future value of cash_flow expected num_yrs from now
    discounted at interest_rate.
    
    >>> future_value(5000, 0.10, 1)
    5500
    >>> future_value(1000, 0.08, 2)    
    1166.4
    >>> future_value(6500, 0.05, 9)
    10083.63 
    """       
    
    # needs either a precondition or checks to make sure that variables are not negative (-1)
    
    answer = cash_flow * (1 + interest_rate) ** num_of_yrs

    return answer

help(future_value)


print("#" + 50*"-")
print("Testing my Examples for Exercise 2.")

print("#" + 50*"-")
print("Exercise 2, Example 1:")
print("Evaluating present_value(200, 0.10, 4)")
print("Expected: " + str(292.820))
print("Got: " + str(future_value(200, 0.10, 4)))

print("#" + 50*"-")
print("Exercise 2, Example 2:")
print("Evaluating present_value(450, 0.05, 6)")
print("Expected: " + str(603.043))
print("Got: " + str(future_value(450, 0.05, 6)))

print("#" + 50*"-")
print("Exercise 2, Example 3:")
print("Evaluating present_value(950, 0.08, 2)")
print("Expected: " + str(1108.080))
print("Got: " + str(future_value(950, 0.08, 2)))


# Exercise 3 

def total_revenue(units_sold, price)-> float:
    """Return the total revenue earned by a firm selling units_sold of a product
    for a value of price.
    
    >>> total_revenue(50, 20)
    1000
    >>> total_revenue(120, 60)
    7200
    >>> total_revenue(500, 100)
    50000   
    """
    
    # needs either a precondition or checks to make sure that variables are not negative (-1)
    
    answer = units_sold * price
    
    return answer


help(total_revenue)


print("#" + 50*"-")
print("Testing my Examples for Exercise 3.")

print("#" + 50*"-")
print("Exercise 3, Example 1:")
print("Evaluating total_revenue(50, 20)")
print("Expected: " + str(1000))
print("Got: " + str(total_revenue(50, 20)))

print("#" + 50*"-")
print("Exercise 3, Example 2:")
print("Evaluating total_revenue(120, 60)")
print("Expected: " + str(7200))
print("Got: " + str(total_revenue(120, 60)))

print("#" + 50*"-")
print("Exercise 3, Example 3:")
print("Evaluating total_revenue(500, 100)")
print("Expected: " + str(50000))
print("Got: " + str(total_revenue(500, 100)))


# Exercise 4 

def total_cost(q,a,b)-> float:
    """Return the total cost incurred by a firm to produce a product.
    >>> total_cost(4, 600, 5000)
    14600
    >>>total_cost(8, 800, 6000)
    57200
    >>>total_cost(7, 750, 7000)
    43750
    """
    
    # needs either a precondition or checks to make sure that variables are not negative (-1)
    
    answer = a*(q**2)+b
    
    return answer

help(total_cost)

print("#" + 50*"-")
print("Testing my Examples for Exercise 4.")

print("#" + 50*"-")
print("Exercise 4, Example 1:")
print("Evaluating total_cost(5, 300, 4000)")
print("Expected: " + str(11500))
print("Got: " + str(total_cost(5, 300, 4000)))

print("#" + 50*"-")
print("Exercise 4, Example 2:")
print("Evaluating total_cost(6, 650, 2300)")
print("Expected: " + str(25700))
print("Got: " + str(total_cost(6, 650, 2300)))

print("#" + 50*"-")
print("Exercise 4, Example 3:")
print("Evaluating total_cost(3, 420, 3500)")
print("Expected: " + str(7280))
print("Got: " + str(total_cost(3, 420, 3500)))


# Exercise 5

def CESutility(x, y, r)-> float:
    """Returns the value of the Constant Elasticity of Substitution using the
    utility function, which measure the theoretical degree of satisfaction a
    consumer may get from two goods.
    
    x represents good one.
    y represent good two.
    r is the parameter that represents the degree to which the goods 
    are complements or substitutes.
    
    >>> (CESutility(10, 10, 0.5))
    40
    >>> (CESutility(20, 20, 0.10))
    20480
    >>> (CESutility(30, 30, 0.20))
    960
    """
    
    # needs either a precondition or checks to make sure that variables are not negative (-1)
    
    answer = (x ** r + y ** r) ** (1/r)
   
    return answer

help(CESutility)


print("#" + 50*"-")
print("Testing my Examples for Exercise 5.")

print("#" + 50*"-")
print("Exercise 5, Example 1:")
print("Evaluating CESutility(10, 10, 0.5)")
print("Expected: " + str(40))
print("Got: " + str(CESutility(10, 10, 0.5)))

print("#" + 50*"-")
print("Exercise 5, Example 2:")
print("Evaluating CESutility(20, 20, 0.10)")
print("Expected: " + str(20480))
print("Got: " + str(CESutility(20, 20, 0.10)))

print("#" + 50*"-")
print("Exercise 5, Example 3:")
print("Evaluating CESutility(30, 30, 0.2)")
print("Expected: " + str(960))
print("Got: " + str(CESutility(30, 30, 0.2)))
