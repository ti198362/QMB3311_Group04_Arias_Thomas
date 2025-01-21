# Script: my_functions.py
# Authors: Timothy Arias and Destiny Thomas
# Date: Jan 20 2025

# 1a.

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
    answer = cash_flow/(1 + interest_rate) ** num_yrs

    return answer

help(present_value)

print("Testing my Examples for Exercise 1a.")

print(present_value(300, 0.30, 3))
#136.549... 

print(present_value(200, 0.10, 2))
#165.289...

print(present_value(1000, 0.50, 2))
#444.444...


# 1b.

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
    answer = cash_flow * (1 + interest_rate) ** num_of_yrs

    return answer

help(future_value)

print("Testing my Examples for Exercise 1b.")

print(future_value(200, 0.10, 4))
#292.820...

print(future_value(450, 0.05, 6))
#603.043...

print(future_value(950, 0.08, 2))
#1108.080...



# 1c. 

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
    
    answer = units_sold * price
    
    return answer


help(total_revenue)

print("Testing my Examples for Exercise 1c.")

print(total_revenue(50, 20))
#1000

print(total_revenue(120, 60))
#7200

print(total_revenue(500, 100))
#50000


# 1d.  

def total_cost(q,a,b)-> float:
    """Return the total cost incurred by a firm to produce a product.
    >>> total_cost(4, 600, 5000)
    14600
    >>>total_cost(8, 800, 6000)
    57200
    >>>total_cost(7, 750, 7000)
    43750
    """
    answer = a*(q**2)+b
    
    return answer

help(total_cost)

print("Testing my Examples for Exercise 1d.")

print(total_cost(5, 300, 4000))
#11500

print(total_cost(6, 650, 2300))        
#25700

print(total_cost(3, 420, 3500))
#7280


# 1e. 

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
    answer = (x ** r + y ** r) ** (1/r)
   
    return answer

help(CESutility)

print("Testing my Examples for Exercise 1e.")

print(CESutility(10, 10, 0.5))
#40

print(CESutility(20, 20, 0.10))
#20480

print(CESutility(30, 30, 0.20))
#960

