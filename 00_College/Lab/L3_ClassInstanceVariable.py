# Program to check wheather the class and instance variable's id changes when modified
class A:
    a = 9      #class variable
    def get(self,b):
        self.b = b
        
obj1 = A()      #object of class A
obj1.get(3)
print("Accessing class Variable a from class A :", obj1.a)
print("Id of the class variable a from class A :", id(obj1.a))
print()

print("Accessing instance Variable b from class A :", obj1.b)
print("Id of the instance variable b from class A :", id(obj1.b))
print()

#After changing the class variable

obj1.a = 900
print("After changing the value of class variable : ")
print("Accessing class Variable a from class A :", obj1.a)
print("Id of the class variable a from class A :", id(obj1.a))
print()

#After changing the instance variable
obj1.b = 300
print("After changing the value of instance variable : ")
print("Accessing instance Variable b from class A :", obj1.b)
print("Id of the instance Variable b from class A :", id(obj1.b))
print() 