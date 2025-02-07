# Program to calculate the surface volume and area of a cylinder

import math   # Import statements

# Taking the input of radius & height from the user
Radius = float(input("Enter the value of radius of Cylinder : "))
Height = float(input("Enter the value of height of Cylinder : "))

# Computing to find the volume & Area (using the algebric Formulas
Volume = math.pi * Radius * Radius * Height
Curved_Surface_Area = 2 * math.pi * Radius * Height
Total_Surface_Area = 2 * math.pi * Radius * (Height + Radius)


# Printing statement 
print(f"The volume of Cylinder = {Volume:.2f}")
print(f"The Curved Surface Area of Cylinder = {Curved_Surface_Area:.2f}")
print(f"The Total_Surface_Area of Cylinder = {Total_Surface_Area:.2f}")
