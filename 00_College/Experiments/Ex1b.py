'''
The factorial of a no. (n!) is the product of all positive intergers from 1 to n 
Example 3! = 3 x 2 x 1 = 6
'''
print("Program to print factorial of a number")

#Taking user input
num = int(input("Enter the number : "))

#initializing factorial to 1
factorial = 1

#Loop from 1 to num

for i in range (1 , num + 1):
    factorial = factorial * i
    
    
#Display result
print("Factorial of ", num , " is ", factorial)