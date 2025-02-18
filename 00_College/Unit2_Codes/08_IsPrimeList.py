# Program to return prime numbers from a list

def is_prime(n):
    """Function to check if a number is prime"""
    if n < 2:
        return False  # Prime numbers start from 2
    for i in range(2, int(n ** 0.5) + 1):  # Check divisibility up to √n
        if n % i == 0:
            return False
    return True

def get_prime_numbers(numbers):
    """Function to return only prime numbers from a list"""
    return [num for num in numbers if is_prime(num)]

# Example list of numbers
num_list = [3, 4, 7, 8, 11, 15, 19, 20, 23, 29, 31, 35, 40]

# Get prime numbers from the list
prime_numbers = get_prime_numbers(num_list)

# Print the result
print("Prime numbers from the list:", prime_numbers)
