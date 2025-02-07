# Program to find square root of number

import math   # import statement 

Num = int(input("Enter the number : "))   # Taking the input from user


# squareRoot = math.sqrt(Num)   # using of math module 

# squareRoot = (Num ** 0.5)     # use of exponentiation operator

squareRoot = pow(Num, 0.5)      # use of pow function

print("SqaureRoot = ", squareRoot)