# Program to print multiplication table of the given number

num = int(input("Enter the number : "))

i = 0
while(i<=10):
    print(f"{num} X {i} = {num*i}")
    i = i+1