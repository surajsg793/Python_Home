# Python is a dynamically typed language, which means that you don't need to declare the data type of a variable when you create it. Python determines the data type of a variable based on the value you assign to it. Here are some common data types in Python:

# Integers (int): Integers are whole numbers, such as 1, -3, 1000, etc.

# Floating-Point Numbers (float): Floating-point numbers are numbers with a decimal point or in exponential notation, such as 3.14, -0.001, 2e-5, etc.

# Strings (str): Strings are sequences of characters enclosed in single (' '), double (" "), or triple (''' ''' or """ """) quotes. For example, "Hello, Python!" is a string.

# Lists (list): Lists are ordered collections of items that can be of any data type. Lists are mutable, meaning you can change their contents. For example, [1, 2, 3] is a list.

# Tuples (tuple): Tuples are similar to lists but are immutable, meaning you can't change their contents after creation. They are defined using parentheses. For example, (1, 2, 3) is a tuple.

# Dictionaries (dict): Dictionaries are collections of key-value pairs. Each key is associated with a value. Dictionaries are defined using curly braces {}. For example, {"name": "John", "age": 30} is a dictionary.

# Sets (set): Sets are unordered collections of unique elements. They are defined using curly braces {} or the set() constructor. For example, {1, 2, 3} is a set.

# Booleans (bool): Booleans represent either True or False values and are used in logical operations and conditional statements.

# None (NoneType): None is a special data type representing the absence of a value. It is often used to indicate that a variable has no value or that a function doesn't return anything.

# You can check the type of a variable using the type() function. For example:

# python
# Copy code
# x = 42
# print(type(x))  # This will print <class 'int'>

# y = "Hello, Python!"
# print(type(y))  # This will print <class 'str'>
# Python also allows you to explicitly convert between data types using functions like int(), float(), str(), and others.

# python
# Copy code
# num_str = "42"
# num = int(num_str)  # Converts the string "42" to an integer 42
# Understanding and working with these data types is fundamental to programming in Python.

# Built in DataType

# Text type : str
# Numeric type : int, float, complex
# Sequence type : list,truple, string, range
# Mapping : dict
# Set type : set, frozenset
# Boolean type : boolean
# Binary type : bytes, bytearray, memoryview

x = 5 # int
y = "chotu " # str
a = 20.4 # float
b = 2+3j # complex
c = [1, 12, "Raj", "golu"] # list
d = (1, 12, "Raj", "golu") # tuple
e = {"Name" : "Chotu", "Age" : 12} # dict
f = {"Apple ", "Banana ", "Orange"} # set
g = range(5) # range
h = True # bool
# i = b"byteArray" # bytearray
j = bytes(3)

l = memoryview(bytes(5)) # memoryview


# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))
# print(type(f))
# print(type(g))
# print(type(h))
# # print(type(i))
# print(type(j))
# print(type(l))
# print(type(x))
# print(type(y))

# print((a))
# print((b))
# print((c))
# print((d))
# print((e))
# print((f))
# print((g))
# print((h))
# # print((i))
# print((j))
# print((l))
# print((x))
# print((y))

m = float(x)
print(m)

n = int(a)
print(n)

o = complex(x)
print(o)

# p = int(b)
# print(p)

import random
q = random.randrange(1, 20)+1
print(q)



