#     *
#    ***
#   *****
#  *******


num = int(input("Enter the number : "))

i = 1
while i <= num:
    
    j = 1
    while j <= num - i:          # num-i+1
        print(" ", end=" ")
        j += 1
    
    k = 1
    while k <= (2 * i - 1):               # 2*i-1
        print("*", end=" ")         
        k += 1 
    
    print()
    i += 1
    