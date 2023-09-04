# In Python, a variable is a symbolic name or identifier that can be used to store and reference data. Variables are used to hold values or objects, making it easier to work with data and manipulate it in your programs. Here are some key points about variables in Python:

# ### Variable Naming Rules:

# 1. Variable names must begin with a letter (a-z, A-Z) or an underscore `_`. They cannot begin with a digit (0-9).
# 2. After the initial letter or underscore, variable names can contain letters, digits, and underscores.
# 3. Variable names are case-sensitive, so `my_var`, `My_Var`, and `MY_VAR` are all different variables.
# 4. Variable names should be descriptive and follow the Python naming conventions (e.g., use lowercase letters and underscores for variable names: `my_variable`, `user_age`, etc.).
# 5. Variable names should not use Python's reserved keywords (e.g., `if`, `else`, `for`, `while`, etc.) as they have predefined meanings in the language.

# ### Variable Assignment:

# You can assign a value to a variable using the assignment operator `=`. The value on the right side of the `=` is assigned to the variable on the left side:

# ```python
# my_variable = 42
# ```

# You can also assign the result of an expression or function call to a variable:

# ```python
# result = 2 + 2
# ```

# ### Variable Data Types:

# In Python, variables are dynamically typed, which means you do not need to specify the data type of a variable explicitly. The interpreter determines the data type based on the value assigned to the variable. Common variable data types in Python include:

# - **Integers (`int`):** Used for whole numbers, e.g., `5`, `-10`, `1000`.

# - **Floating-Point Numbers (`float`):** Used for decimal numbers, e.g., `3.14`, `-0.5`, `2.0`.

# - **Strings (`str`):** Used for text, e.g., `"Hello, World!"`, `'Python'`, `"42"`.

# - **Boolean (`bool`):** Used for `True` and `False` values.

# - **Lists, Tuples, Sets, and Dictionaries:** Used for collections of data.

# ### Variable Scope:

# The scope of a variable refers to the region of the code where the variable can be accessed or modified. Python has different scopes, including:

# - **Local Scope:** Variables defined within a function have local scope and are accessible only within that function.

# - **Enclosing Scope:** Variables defined in an outer function are accessible in nested functions.

# - **Global Scope:** Variables defined outside of any function have global scope and can be accessed from anywhere in the program.

# - **Built-in Scope:** Python provides built-in variables and functions that are accessible from anywhere in your code.

# ### Variable Reassignment:

# You can change the value of a variable by assigning it a new value:

# ```python
# my_variable = 42
# my_variable = "Hello"
# ```

# ### Deleting Variables:

# You can delete a variable using the `del` statement:

# ```python
# my_variable = 42
# del my_variable
# ```

# After deletion, attempting to access the variable will result in an error.

# Understanding variables and their scope is fundamental to Python programming, as they allow you to work with and manipulate data effectively in your programs.


x = 5
y = "sharad"

print(x)
print(y) 

a = str(4)
b = int(a)
c = float(b)
d = bool(c)

print(a)
print(b)
print(c)
print(d)

print(type(a))
print(type(b))
print(type(c))
print(type(d))


# print(myVar)
myvar = "Sharad"
_myVar = "Home"
Myvar = "Book"
myVar1 = "Email"

print(myvar)
print(_myVar)
print(Myvar)
print(myVar1)

l, m, n, o = 1, 3, "pen", True
print((l, m, n, o))

l, m, n, o = "Home"

print(type(l))
print(l, m, n, o)

l=m=n=o 
print(l, m, n, o)

l=m=n=o = "Bike"
print(l, m, n, o)

fruits = ["orange", "banana", "apple", "mango"]
print(fruits)
l, m, n, o = fruits

print(l, m, n, o)

print(type(fruits))

p = "My name "
q = "is "
r = "Sharad "
print(p, q, r)
print(p + q + r)








