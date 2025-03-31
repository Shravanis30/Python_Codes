`students = {}

def add_student():
    roll_no = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    grade = float(input("Enter Grade: "))
    students[roll_no] = {'Name': name, 'Grade': grade}
    print("Student added successfully!\n")

def update_student():
    roll_no = input("Enter Roll Number to Update: ")
    if roll_no in students:
        name = input("Enter New Name: ")
        grade = float(input("Enter New Grade: "))
        students[roll_no] = {'Name': name, 'Grade': grade}
        print("Student details updated!\n")
    else:
        print("Student not found!\n")

def remove_student():
    roll_no = input("Enter Roll Number to Remove: ")
    if roll_no in students:
        del students[roll_no]
        print("Student removed successfully!\n")
    else:
        print("Student not found!\n")

def view_students():
    if students:
        for roll_no, details in students.items():
            print(f"Roll No: {roll_no}, Name: {details['Name']}, Grade: {details['Grade']}")
    else:
        print("No student records available.\n")

def calculate_average():
    roll_no = input("Enter Roll Number to Calculate Average Grade: ")
    if roll_no in students:
        print(f"Average Grade of {students[roll_no]['Name']}: {students[roll_no]['Grade']}\n")
    else:
        print("Student not found!\n")

def menu():
    while True:
        print("1. Add Student")
        print("2. Update Student")
        print("3. Remove Student")
        print("4. View All Students")
        print("5. Calculate Average Grade")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            update_student()
        elif choice == '3':
            remove_student()
        elif choice == '4':
            view_students()
        elif choice == '5':
            calculate_average()
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 6.\n")

menu()
`