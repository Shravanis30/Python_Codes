# Program to perform addition, subtraction, division and multiplication of given two numbers (menu driven)

import math

def Addition(a , b):
    return a + b

def Subtraction(a, b):
    return a - b

def Division(a, b):
    return a / b

def Multiplication(a, b):
    return a * b

while True:
    print()
    print("******MENU******")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Division")
    print("4. Multiplication")
    print("5. Exit")
    print()

    
    choice = input("Enter the number from 1 to 5 by refering the Menu : ")

    if choice == '5':
        print("Exiting the program as per your choice!")
        break

    num1 = float(input("Enter the value of num1 : "))
    num2 = float(input("Enter the value of num2 : "))

    if choice == '1':
        print(f"Addition of {num1} + {num2} = {Addition(num1, num2)}")
    elif choice == '2':
        print(f"Substraction of {num1} - {num2} = {Subtraction(num1, num2)}")
    elif choice == '3':
        print(f"Division of {num1} / {num2} = {Division(num1, num2)}")
    elif choice == '2':
        print(f"Multiplication of {num1} * {num2} = {Multiplication(num1, num2)}")
    else:
        print("Please enter the valid choice! & try again")