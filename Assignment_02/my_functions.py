# Script: my_functions.py
# Authors: Timothy Arias and Destiny Thomas
# Date: Jan 20 2025

# 1a.

def present_value(cash_flow: float, interest_rate: float, num_yrs: float) -> float:
    """Return the present value of cash_flow expected num_yrs from now
    discounted at interest_rate.

    >>> present_value(110, 0.10, 1)
    100.0
    >>> present_value(121, 0.10, 2)
    100.0
    >>> present_value(1000, 0.)
    """
    answer = cash_flow/(1 + interest_rate) ** num_yrs

    return answer

help(present_value)

present_value(300, 0.30, 3)
#136.549... 

present_value(200, 0.10, 2)
#165.289...

present_value(1000, 0.50, 2)
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

def total_revenue(units_sold,price)-> float:
    return units_sold * price

"Formula to calculate the revenue earned by a firm selling a product at\
    a fixed price."

units_sold= 10
price= 5

print(total_revenue(units_sold, price))


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

def CESutility(x,y,r)-> float:
    return (x**r + y**r)**2

"Formula to calculate the value of the Constant Elasticity of Substitution\
utility function, which measures the theoretical degree of satisfaction a\
    consumer may get from two goods."
"x and y =  the two goods consumed."
"r = parameter that represents the degree to which the goods are complements\
    or substitutes."

x= 10
y= 10
r= 0.5

print(CESutility(x, y, r)) 
