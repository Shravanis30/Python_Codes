class Book:
    def __init__(self):
        self.name = "To Kill a Mockingbird"
        self.author = "Harper Lee"
        self.price = 399

    def display_details(self):
        print(f"Book Name: {self.name}")
        print(f"Author: {self.author}")
        print(f"Price: ₹{self.price}")

# Create an object and display details
book = Book()
book.display_details()
