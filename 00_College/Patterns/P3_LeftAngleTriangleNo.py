# 1
# 12
# 123
# 1234

num = int(input("Enter the number : "))

i = 1

while i <= num:
    j = 1 
    while j <= i:
        print(j, end=" ")
        j += 1
    print()
    i += 1