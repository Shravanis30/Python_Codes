# *******
#  *****
#   ***
#    *
    
num = int(input("Enter the value of num : "))

i = num
while i >= 1:
    
    j = 1
    while j <= num - i + 1:
        print(" ", end=" ")
        j += 1
    
    k = 1
    while k <= (2 * i - 1):
        print("*", end=" ")
        k += 1
        
    print()
    i -= 1
    