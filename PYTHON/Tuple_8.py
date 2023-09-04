# In Python, a tuple is an ordered and immutable collection of elements. Tuples are similar to lists in that they can hold multiple items, but they differ in that tuples cannot be modified once they are created. They are defined using parentheses `()` or the `tuple()` constructor. Here's an overview of how to work with tuples in Python:

# ### Creating Tuples:

# You can create a tuple by specifying its elements inside parentheses `()`:

# ```python
# my_tuple = (1, 2, 3, 4, 5)
# ```

# Alternatively, you can create a tuple without parentheses, separating the elements with commas:

# ```python
# my_tuple = 1, 2, 3, 4, 5
# ```

# ### Accessing Elements:

# You can access individual elements of a tuple using indexing, similar to lists:

# ```python
# my_tuple = (10, 20, 30, 40, 50)
# first_element = my_tuple[0]  # Accessing the first element (10)
# second_element = my_tuple[1]  # Accessing the second element (20)
# ```

# You can also use negative indexing to access elements from the end of the tuple:

# ```python
# last_element = my_tuple[-1]  # Accessing the last element (50)
# second_last_element = my_tuple[-2]  # Accessing the second-to-last element (40)
# ```

# ### Tuple Packing and Unpacking:

# You can create a tuple by packing multiple values into a single variable, and you can also unpack a tuple to assign its values to multiple variables:

# ```python
# # Packing values into a tuple
# my_tuple = 1, 2, 3

# # Unpacking a tuple
# x, y, z = my_tuple
# ```

# ### Immutability:

# Tuples are immutable, which means their elements cannot be modified, added, or removed once the tuple is created. You can, however, create a new tuple by concatenating or slicing existing tuples.

# ### Tuple Methods:

# Tuples in Python have a limited set of methods because they are immutable. Common tuple methods include `count()` and `index()`:

# - `count()`: Returns the number of occurrences of a specified element in the tuple.

#   ```python
#   my_tuple = (1, 2, 2, 3, 4, 2)
#   count_2 = my_tuple.count(2)  # Returns 3
#   ```

# - `index()`: Returns the index of the first occurrence of a specified element in the tuple.

#   ```python
#   my_tuple = (1, 2, 3, 4, 5)
#   index_3 = my_tuple.index(3)  # Returns 2
#   ```

# ### Use Cases for Tuples:

# Tuples are commonly used when you want to represent a collection of items that should not be modified. Some common use cases for tuples include:

# - Representing coordinates (x, y, z) in 3D space.
# - Returning multiple values from a function.
# - Serving as keys in dictionaries (since they are immutable).

# ```python
# point = (3, 4, 5)
# x, y, z = point  # Unpacking values

# employee_info = ("John", 30, "Engineer")
# name, age, job = employee_info  # Unpacking values
# ```

# Tuples provide a lightweight and efficient way to store and manipulate collections of values when immutability is desired.


x = ("book", "pen", "school", "code", "3", "4.4", "3", "True", "3j") 
y = tuple((10, 88, 23, 43, 55, 32, 70))

# print(x)
# print(type(x))
# print(len(x))
# print(type(y))

# print(x[1])

# print(x[-1])

# print(x[1:4 ])

# print(x[:-1])

# print(x[1:])

# print(x[:6])

# print(x[-5:-1])

# if "school" in x :
#     print("Yes, It is there.")

# y = list(x)
# print(type(y))
# y[1] = "Tutorial"
# x = tuple(y)
# print(x)

# y = list(x)
# print(type(y))
# y.append("works")
# x = tuple(y)
# print(type(x))
# print(x)

# x += y
# print(x)

# y = list(x)
# print(type(y))
# y.remove("code")
# x = tuple(y)
# print(type(x))
# print(x)


# del x
# print(x)

# x = ("book", "pen", "school", "code")
# y = list(x)
# y.reverse()
# x = tuple(y)
# book, pen, school, code = x
# print(book)
# print(pen)
# print(school)
# print(code)

# x = ("book", "pen", "school", "code", "area", "new", "keep")
# y = list(x)
# y.reverse()
# x = tuple(y)
# (book, pen, school, *code) = x
# print(book)
# print(pen)
# print(school)
# print(code)

# for i in x :
#     print(i)

# for i in range(len(y)) :
#     print(y[i])

# i = 0
# while i < len(x) :
#     print(x[i])
#     i = i+1

# z = x + y
# print(z)

# z = y*5
# print(z)


