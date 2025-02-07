# Varible declaring
x = 18
y = "shravani"
print(x);
print(y);


# Variables type can be changed even after declaring it
a = "Name"
a = 18
print(a);


# Casting (variable can be declared with a type)
print(str(3))
print(int(3))
print(float(3))


# type of the variable
b = 5
c = "shravani"
print(type(b))
print(type(c))

# variable are case senstive
d = 4
D = "Four"
print(d)
print(D)
# D will not overwirte d



"""
Rules for Python variables:
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.
"""



# declaring multiple variables at once
e, f, g = "Shravani", "Sanjay", "Salunke"
print(e)
print(f)
print(g)

# One value to many variables
E = F = G = "SHRAVANI"
print(E)
print(F)
print(G)

# unpack of collections
fruits = ["Orange", "Apple", "Banana", "Cheery"]
h, i, j, k = fruits 
print(h)
print(i)
print(j)
print(k)

# For numbers, the + character works as a mathematical operator:
# when you try to combine a string and a number with the + operator, Python will give you an error:
# The print() function is to separate them with commas, which even support different data types:


# global Variables
L = "Shravani"
def myfunc():
    L = "Deep"
    print("I am " + L)

myfunc();
print("I am " + L)


# global keyword usage
def funcFruits():
    global l
    l = "Orange"
    
funcFruits()
print("It is a " + l)


# use global to redeclare the global variable again in function
k = "apple"
def funcApple():
    global k
    k = "Apple"
    print(k)
funcApple()

print(k)