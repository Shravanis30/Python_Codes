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








# l = ['Python', 'programming', 'is', 'easy']
# print(type(l))  
# # Output: <class 'list'>

# s = ','.join(l)  # Joining with space as separator
# print(s)  
# # Output: 'Python programming is easy'






# for i in range(1, 11):			
#     if i % 2 == 0:  # if even?
#         pass  # do nothing for even numbers
#     else:  # if odd?
#         print("odd numbers:", i)





# def student(firstname, lastname): 
# 	print(firstname, lastname)
# student("tejas", "Patil")
# student("Patil","tejas")





# def student(firstname, lastname): 
# 	print(firstname, lastname) 
# # Keyword arguments				 
# student(firstname ='Geeks', lastname ='Practice')	 
# student(lastname ='Practice', firstname ='Geeks') 






# def myFun1(*argv): 
#        for i in argv: 
#              print (i , end=" ") 

# def myFun2(**kwargs): 
#        for key, value in kwargs.items(): 
#              print ("% s == % s" %(key, value)) 

# # Driver code 
# print("Result of *args: ")
# myFun1('Hello', 'Welcome', 'to', 'GeeksforGeeks') 

# print("\nResult of **kwargs:")
# myFun2(first ='tejas', mid ='lalit', last ='patil') 





def nameAge(name, age):
	print("Hi, I am", name)				
	print("My age is ", age)

# You will get correct output because 			
# argument is given in order					
print("Case-1:")
nameAge("Suraj", 27)
# You will get incorrect output because
# argument is not in order
print("\nCase-2:")
nameAge(27, "Suraj")