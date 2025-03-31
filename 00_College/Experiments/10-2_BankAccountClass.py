class BankAccount:
    def __init__(self, account_number, balance=1000):
        self.account_number = account_number
        self.balance = max(balance, 100)  # Ensures balance is at least 100

    def display_details(self):
        print(f"Account Number: {self.account_number}")
        print(f"Balance: ₹{self.balance}")

# Creating two BankAccount objects
account1 = BankAccount("123456", 50)   # Balance < 100, so it will set to 100
account2 = BankAccount("789012", 1500) # Balance > 100, will remain 1500

print("Account 1 Details:")
account1.display_details()
print("\nAccount 2 Details:")
account2.display_details()
