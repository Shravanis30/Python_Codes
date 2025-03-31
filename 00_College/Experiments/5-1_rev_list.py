# Python program to reverse a list using different methods

def reverse_list_methods(lst):

    # Method 1: Using reverse() (Modifies original list)
    method1 = lst[:]
    method1.reverse()
    
    # Method 2: Using slicing (Does not modify original list)
    method2 = lst[::-1]
    
    # Method 3: Using reversed() (Returns an iterator, converted to list)
    method3 = list(reversed(lst))
    
    return method1, method2, method3

# Example usage
lst = [1, 2, 3, 4, 5]
rev1, rev2, rev3 = reverse_list_methods(lst)

print("Original List:", lst)
print("Reversed using reverse():", rev1)
print("Reversed using slicing:", rev2)
print("Reversed using reversed():", rev3)
