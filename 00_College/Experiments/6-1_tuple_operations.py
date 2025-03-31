# Creating a tuple of tuples
nested_tuple = ((1, 2, 3), (4, 5, 6), (7, 8, 9))

# Accessing elements from the outer tuple
print("Outer tuple:", nested_tuple)
print("First inner tuple:", nested_tuple[0])
print("Second inner tuple:", nested_tuple[1])

# Accessing elements from inner tuples
print("First element of first inner tuple:", nested_tuple[0][0])
print("Last element of second inner tuple:", nested_tuple[1][-1])
print("Middle element of third inner tuple:", nested_tuple[2][1])
