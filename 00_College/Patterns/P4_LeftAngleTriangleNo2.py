# 1
# 22
# 333
# 4444


num = int(input("Enter the number : "))

i = 1

while i <= num:
    j = 1
    while j <= i:
        print(i, end=" ")
        j += 1
    print()
    i += 1