# Program to generate students result. Accept marks of five subjects display result according to following conditions.

Python_Programming = float(input("Enter the marks of Python_Programming subject : "))
Cloud_Computing = float(input("Enter the marks of Cloud_Computing subject : "))
Android_Devlopment = float(input("Enter the marks of Android_Devlopment subject : "))
Human_Interface = float(input("Enter the marks of Human_Interface subject : "))
final_Project = float(input("Enter the marks of final_Project subject : "))

Total_Sum = Python_Programming + Cloud_Computing + Android_Devlopment + Human_Interface + final_Project
Percentage = (Total_Sum / 500) * 100

print(Percentage)

if Percentage >= 75:
    print("You are passed with First class with distinction!")
elif Percentage >= 60 and Percentage < 75:
    print("You are passed with First class.")
elif Percentage >= 45 and Percentage < 60:
    print("You are passed with Second class.")
elif Percentage >= 40 and Percentage < 45:
    print("You are passed.")
elif Percentage < 40:
    print("You are fail")
else:
    print("Enter vaild marks")
