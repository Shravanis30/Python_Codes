# Creating a tuple with three elements
my_tuple = (10, 20, 30)

# Tuple unpacking: Assigning each element to a variable
a, b, c = my_tuple

print("Before swapping:")
print("a =", a, ", b =", b, ", c =", c)

# Swapping values using tuple unpacking
a, b, c = c, a, b

print("After swapping:")
print("a =", a, ", b =", b, ", c =", c)
