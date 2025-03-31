def register_students(class_name, *students, **details):
    print(f"Class Name: {class_name}")
    print("Students:", students if students else "No students registered.")
    
    if details:
        print("Additional Details:")
        for key, value in details.items():
            print(f"{key.capitalize()}: {value}")

# Example
register_students("Physics", "John", "Emma", teacher="Mr. Smith", room_number=101)
