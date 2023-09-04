# Conditional statements in Python allow you to control the flow of your program based on specific conditions. The primary conditional statements in Python are `if`, `elif` (short for "else if"), and `else`. Here's an overview of how to use conditional statements in Python:

# ### 1. `if` Statement:
# The `if` statement allows you to execute a block of code if a given condition is `True`. If the condition is `False`, the code block is skipped.

# ```python
# if condition:
#     # Code to execute if the condition is True
# ```

# Example:

# ```python
# x = 10
# if x > 5:
#     print("x is greater than 5")
# ```

# ### 2. `elif` Statement:
# The `elif` statement is used when you want to check multiple conditions one after the other. If the condition specified after `if` is `False`, Python checks the condition after `elif`. You can have multiple `elif` statements.

# ```python
# if condition1:
#     # Code to execute if condition1 is True
# elif condition2:
#     # Code to execute if condition2 is True
# else:
#     # Code to execute if no conditions are True
# ```

# Example:

# ```python
# x = 10
# if x > 15:
#     print("x is greater than 15")
# elif x > 5:
#     print("x is greater than 5 but not greater than 15")
# else:
#     print("x is not greater than 5")
# ```

# ### 3. `else` Statement:
# The `else` statement is used to specify a block of code to execute when no previous `if` or `elif` conditions are True.

# ```python
# if condition:
#     # Code to execute if the condition is True
# else:
#     # Code to execute if the condition is False
# ```

# Example:

# ```python
# x = 3
# if x > 5:
#     print("x is greater than 5")
# else:
#     print("x is not greater than 5")
# ```

# ### Nested Conditionals:
# You can also nest conditional statements within each other to handle more complex scenarios.

# ```python
# if condition1:
#     if condition2:
#         # Code to execute if both condition1 and condition2 are True
#     else:
#         # Code to execute if condition1 is True but condition2 is False
# else:
#     # Code to execute if condition1 is False
# ```

# Example:

# ```python
# x = 10
# y = 5
# if x > 5:
#     if y > 3:
#         print("Both x and y are greater than 5")
#     else:
#         print("x is greater than 5, but y is not greater than 3")
# else:
#     print("x is not greater than 5")
# ```

# Conditional statements are essential for controlling the execution flow in your Python programs, allowing you to make decisions based on specific conditions.


x = 13
y = 17
z = 15

a = x
b = y
c = z

# if x > y :
#     print("true")


# if x > y : 
#     print("true")
# else : 
#     print("false")


# if x > y :
#     print("true")
# elif x == y :
#     print("equals")
# else :
#     print("false")

# if x > y : print("true")

# print("true") if x > y else print("false")

# print("true") if x > y else print("equals") if x == y else print("false")

# if a>b and a>c :
#     print("a")
# elif b>a and b>c :
#     print("b")
# else :
#     print("c")

# if a>b or a>c :
#     print("a")
# elif b>a or b>c :
#     print("b")
# else :
#     print("c")

# if a > b and c > a :
#     print("both the true")

# if a > b or a > c :
#     print("true")

# if x > 10 : 
#     print("it is above 10, ")
#     if y > 12 :
#         print("and it is also above 12.")
#     else :
#         print("but is is not above 20.")

# if a > b :
#     pass