def count_vowels(string):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return sum(1 for char in string.lower() if char in vowels)

# Example
print(count_vowels("Hello World"))  # Output: 3
