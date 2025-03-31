"""
The sum of first 'n' natural number is calculated using formula
    sum = n * (n+1) /2
    for, n = 10, we get:
    
    sum = 10 * (10+1)/2
    sum = 10 * 11/2
    sum = 110/2
    sum = 55
"""
print("Program to print sum of n natural numbers")

#Define number
n = 10

#calulate sum 
sum_of_n_natural_numbers = n * (n + 1) / 2

#printing calculated sum 
print("Sum of 1st", n , "natural number is", sum_of_n_natural_numbers)