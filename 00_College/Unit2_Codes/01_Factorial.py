# Program to find factorial of a given number

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

num = int(input("Enter the postive number : "))
result = factorial(num)
print(f"Factorial of {num} is {result}")





# def factorial(n):
#     result = 1
#     for i in range(2, n + 1):
#         result *= i
#     return result

# num = int(input("Enter a number: "))
# print(f"Factorial of {num} is {factorial(num)}")





# import math

# num = int(input("Enter a number: "))
# print(f"Factorial of {num} is {math.factorial(num)}")