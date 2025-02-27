# Program to perform all the implemntation of the operators:
# 1.Arithmetic operators
num1 = 15
num2 = 4
print()
print("Program to perform all the implementation of the operators : ")
print()
print("num1:", num1, " &  num2:", num2)
print()
print("Arithmetic operations : ")
print("Addition         :- ", num1, " + ", num2, ":", num1 + num2)  # 19
print("Subtraction      :- ", num1, " - ", num2, ":", num1 - num2)  # 11
print("Multiplication   :- ", num1, " * ", num2, ":", num1 * num2)  # 60
print("Division         :- ", num1, " / ", num2, ":", num1 / num2)  # 3.75
print("Exponentiation   :- ", num1, " ** ", num2, ":", num1**num2)  # 50625
print("Modulus          :- ", num1, " % ", num2, ":", num1 % num2)  # 3
print("Floor Division   :- ", num1, " // ", num2, ":", num1 // num2)  # 3



# 2.Assigment operators
# Example: Updating Marks using Assignment Operators
print()
print("Assigment operators : ")
Marks = 50
print("Marks:", Marks)

Marks += 10  # Marks = Marks + 10
print("Add Marks by 10          :", Marks)            # 60

Marks -= 10  # Marks = Marks - 10
print("Substract Marks by 10    :", Marks)      # 50

Marks *= 2  # Marks = Marks * 2
print("Multiply Marks by 2      :", Marks)        # 100

Marks /= 5  # Marks = Marks / 5
print("Divide Marks by 5        :", Marks)          # 20.0

Marks //= 5  # Marks = Marks // 5
print("Floor Divided Marks by 5 :", Marks)   # 4.0

Marks **= 2  # Marks = Marks ** 2
print("Exponential Marks by 2   :", Marks)     # 16.0

Marks %= 2  # Marks = Marks % 2
print("Module Marks by 2        :", Marks)          # 0.0



# 3. Comparison or Relational Operators
# Example: Comparing Student Ages

age1 = 18
age2 = 20
print()
print("Comparison or Relational Operators:")
print("Age1:", age1, " &  Age2:", age2)
print("Is age1 equal to age2?                   :", age1 == age2)   # False
print("Is age1 not equal to age2?               :", age1 != age2)   # True
print("Is age1 greater than age2?               :", age1 > age2)    # False
print("Is age1 less than age2?                  :", age1 < age2)    # False
print("Is age1 less than or equal to age2?      :", age1 <= age2)   # True
print("Is age1 greater than or equal to age2?   :", age1 >= age2)   # False



# 4. Logical Operators
# Example: Number Conditions

a = 10
b = 5

print()
print("Logical Operators : ")
print("a > 5 and b < 10 :", a > 5 and b < 10)   # True
print("a < 5 or b < 10  :", a < 5 or b < 10)    # True
print("not (a == 10)    :", not (a == 10))      # False




# 5. Bitwise Operators
# Example: Bitwise Operations 

print("\nBitwise Operators : ")
num1 = 6  # Binary: 110
num2 = 3  # Binary: 011

print("num1:", num1, "num2:", num2)

print(num1, "Bitwise AND", num2, "      :", bin(num1 & num2))   # 110 & 011 = 010 (2)
print(num1, "Bitwise OR", num2, "       :", bin(num1 | num2))   # 110 | 011 = 111 (7)
print(num1, "Bitwise XOR", num2, "      :", bin(num1 ^ num2))   # 110 ^ 011 = 101 (5)
print(num2, "Bitwise One's Complement   :", bin(~num2))         # 011 = 100 (4)
print(num1, "Bitwise Left Shift by 1    :", bin(num1 << 1))     # 110 << 1 = 1100 (12)
print(num1, "Bitwise Right Shift by 1   :", bin(num1 >> 1))     # 110 >> 1 = 11 (3)



# 6. Identity Operators
# Example: Checking Identity of Variables

a = 5
b = 5
c = [5]

print()
print("Identity Operators")
print("a is b   :", a is b)        # True (because it has same memory location)
print("a is c   :", a is c)        # False (list has a different memory location)
print("a == c[0]:", a == c[0])     # True (same values )



# 7. Membership Operators
# Example: Checking Presence of a word in a String

sentence = "Python is amazing!"

print()
print("Membership Operators")
print("sentence = ", sentence)
print("Is 'Python' in the sentence?     :", "Python" in sentence)     # True
print("Is 'Java' not in the sentence?   :", "Java" not in sentence) # True
