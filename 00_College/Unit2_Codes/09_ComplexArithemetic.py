# Program to perform addition, subtraction, division and multiplication of given two complex numbers (menu driven)

def add_complex(c1, c2):
    return c1 + c2

def subtract_complex(c1, c2):
    return c1 - c2

def multiply_complex(c1, c2):
    return c1 * c2

def divide_complex(c1, c2):
    if c2 == 0:
        return "Division by zero is not allowed!"
    return c1 / c2

# Taking input for two complex numbers
real1 = float(input("Enter real part of first complex number: "))
imag1 = float(input("Enter imaginary part of first complex number: "))
real2 = float(input("Enter real part of second complex number: "))
imag2 = float(input("Enter imaginary part of second complex number: "))

c1 = complex(real1, imag1)
c2 = complex(real2, imag2)

while True:
    print("\nOperations Menu:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        print(f"Result: {c1} + {c2} = {add_complex(c1, c2)}")
    elif choice == '2':
        print(f"Result: {c1} - {c2} = {subtract_complex(c1, c2)}")
    elif choice == '3':
        print(f"Result: {c1} * {c2} = {multiply_complex(c1, c2)}")
    elif choice == '4':
        print(f"Result: {c1} / {c2} = {divide_complex(c1, c2)}")
    elif choice == '5':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice! Please enter a valid option.")
