# Program to check whether a string is a palindrome or not

def IsPalindrome(s):
    s = s.lower().replace(" ", "")      # this makes a string into lower case and remove the blank spaces
    return s == s[::-1]                 # checks wheather string is same after reversing it

string = input("Enter the string : ")

if IsPalindrome(string):
    print(f"The {string} is palindrome!")
else:
    print(f"The {string} is not palindrome.")
    