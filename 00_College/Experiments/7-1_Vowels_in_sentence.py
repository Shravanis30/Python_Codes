# Q1: Function to find vowels in a sentence

def find_vowels(sentence):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    return {char for char in sentence if char in vowels}

sentence = "Hello, welcome to the world of Python!"
print("Vowels in the sentence:", find_vowels(sentence))