
print("Program to print reversed string")

#Taking user input
user_string = input("Enter a string : ")

#Reversing string & joining each character with comma
reversed_string = ",".join(user_string[::-1])

#Printing reversed string
print("Revered string : ", reversed_string)