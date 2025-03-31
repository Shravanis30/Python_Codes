# Define two tuples
tuple1 = (7, 2, 9, 1)
tuple2 = (5, 8, 3, 6)

# Concatenating tuples
concat_tuple = tuple1 + tuple2
print("Concatenated Tuple:", concat_tuple)

# Sorting in ascending order
asc_sorted_tuple = tuple(sorted(concat_tuple))
print("Ascending Order:", asc_sorted_tuple)

# Sorting in descending order
desc_sorted_tuple = tuple(sorted(concat_tuple, reverse=True))
print("Descending Order:", desc_sorted_tuple)
