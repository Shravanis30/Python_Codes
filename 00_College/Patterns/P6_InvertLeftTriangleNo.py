# 12345
# 1234
# 123
# 12
# 1

num = int(input("Enter the number : "))

i = 1

while i <= num:
    j = num
    while j >= i:
        print(num - j + i, end=" ")   # num-j+i
        j -= 1
    print()
    i += 1
    