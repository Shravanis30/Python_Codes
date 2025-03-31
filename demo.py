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





# def nameAge(name, age):
# 	print("Hi, I am", name)				
# 	print("My age is ", age)

# # You will get correct output because 			
# # argument is given in order					
# print("Case-1:")
# nameAge("Suraj", 27)
# # You will get incorrect output because
# # argument is not in order
# print("\nCase-2:")
# nameAge(27, "Suraj")




# def myFun1(*args):
#     for arg in args:
#         print(arg)

# def myFun2(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key} == {value}")

# myFun1('Hello', 'Welcome', 'to', 'GeeksforGeeks')  
# myFun2(first='Geeks', mid='for', last='Geeks')




# # Step 1: Define two objects
# a=5
# b = 5 # Integers with the same value might have the same identity (small integer caching)
# # Step 2: Identity checks
# if a is b:
#     print("a is b: True")
# else:
#     print("a is b: False")
# if a is not b:
#     print("a is not b: True")
# else:
#     print("a is not b: False")
# # Step 3: Modify 'a'
# a = a + 1 # Changing 'a' (now a new object 6)
# # Step 4: Check identity after modification
# print("After modification:")
# if a is b:
#     print("a is b: True")
# else:
#     print("a is b: False")
# if a is not b:
#     print("a is not b: True")
# else:
#     print("a is not b: False")



# # Get user input
# salary = int(input("Enter the employee's salary: "))
# experience = int(input("Enter the employee's years of experience: "))
# performance_rating = float(input("Enter the employee's performance rating (1 to 5): "))
# # Initialize bonus percentage
# bonus_percentage = 0
# # Check performance rating condition first
# if performance_rating < 3:
#     print("Employee is not eligible for a bonus due to low performance rating.")
#     bonus = 0 # No bonus if performance is below 3
# else:
    
#     # Determine bonus percentage based on experience
#     if experience > 10:
#         bonus_percentage = 20
#     if 5 <= experience <= 10:
#         bonus_percentage = 10
#     if experience < 5:
#         bonus_percentage = 5
# # Calculate bonus
# bonus = (bonus_percentage / 100) * salary
# print(f"Bonus Amount: {bonus}")
# # Final salary calculation
# final_salary = salary + bonus
# print(f"Final Salary after Bonus: {final_salary}")



# total = 0
# for i in range(2, 101, 2):
#     total += i
# print(total)


# a, b = map(int, input("Enter range (a b): ").split())
# while a <= b:
#     if all(a % i != 0 for i in range(2, int(a**0.5) + 1)) and a > 1:
#         print(a, end=' ')
#     a += 1
# print()


# """

#     It is a docstring

# """

# print(__doc__)


#setOperatoions

list1 = {1, 2, 3, "shraavniii"}
list2 = {"shraavniii", "tejas", 1}
#union operation
unionOperation = list1 | list2
intersectionOperation = list1 & list2
differenceOperationList1 = list1 - list2
differenceOperationList2 = list2 - list1
symmtericDifference = list1 ^ list2

print(unionOperation)
print(intersectionOperation)
print(differenceOperationList1)
print(differenceOperationList2)
print(symmtericDifference)


 