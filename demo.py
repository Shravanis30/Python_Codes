# s = "Python programming is easy"
# print(s)  
# # Output: 'Python programming is easy'

# l = s.split()  # Split without any argument (default: whitespace)
# print(l)  
# # Output: ['Python', 'programming', 'is', 'easy']

# l = s.split(',')  # Splitting using ',' as the delimiter
# print(l)  
# # Output: ['Python', 'programming', 'is', 'easy']

# print(type(l))  
# # Output: <class 'list'>





# s = "Python,programming,is,easy"
# print(s)  
# # Output: 'Python,programming,is,easy'

# l = s.split(',')  # Splitting using ',' as the delimiter
# print(l)  
# # Output: ['Python', 'programming', 'is', 'easy']

# l = s.split()  # Split without any argument (default: whitespace)
# print(l)  

# print(type(l))  
# # Output: <class 'list'>





l = ['Python', 'programming', 'is', 'easy']
print(type(l))  
# Output: <class 'list'>

s = ','.join(l)  # Joining with space as separator
print(s)  
# Output: 'Python programming is easy'