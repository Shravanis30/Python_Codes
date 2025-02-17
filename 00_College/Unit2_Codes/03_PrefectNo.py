# Program to find out whether the input number is perfect nubmer or not.

import math

def IsPerfectNumber(n):
    if n < 1:
        print("Enter the value greater than ")
        return false
        
    SumOfDivisors = sum(i for i in range(1, n) if n % i == 0)
    return SumOfDivisors == n

num = int(input("Enter the number : "))

if IsPerfectNumber(num):
    print(f"{num} is a perfect number")
else:
    print(f"{num} is not a perfect number")

