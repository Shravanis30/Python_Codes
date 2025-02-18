# Program to check whether a number is palindrome or not

def IsPalindrome(n):
    
    original_str = str(n)
    reverse_str = original_str[::-1]
    
    return original_str == reverse_str

num = int(input("Enter the number : "))

if IsPalindrome(num):
    print(f"The {num} is a palindrome")
else:
    print(f"The {num} is not a palindrome")
    