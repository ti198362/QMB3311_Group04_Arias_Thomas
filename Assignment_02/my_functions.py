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

def future_value(dollar_amont_of_the_cashflow,discount_rate,number_of_years)-> float:
    return dollar_amont_of_the_cashflow * (1 + discount_rate)**number_of_years

"Formula to calculate the future value of a present cash flow."

dollar_amont_of_the_cashflow= 100000
discount_rate= 0.05
number_of_years= 3

print(future_value(dollar_amont_of_the_cashflow, discount_rate, number_of_years))


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
    return a*(q**2)+b

"Formula to calculate the total cost incurred by a firm to produce a product."
"q = the quantity produced."
"a = the number multiplied by the square of the number of units."
"b = the fixed cost."

q= 5
a= 300
b= 4000


print(total_cost(q, a, b)) 


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

