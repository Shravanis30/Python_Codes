# Program to find area of rectangle

# Taking the values of length & breadth from the user
Length = int(input("Enter the value of Length of Rectangle : "))
Breadth = int(input("Enter the value of Breadth of Rectangle : "))

Area = Length * Breadth                     # Computing area
Perimeter = 2 * (Length + Breadth)          # Computing perimeter

# Printing statement
print("Area of Rectangle = ", Area)
print("Perimeter of Rectangle = ", Perimeter)
