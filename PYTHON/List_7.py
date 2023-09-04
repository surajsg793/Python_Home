# In Python, a list is a data structure that allows you to store an ordered collection of items. Lists are one of the most commonly used data types in Python, and they can contain elements of different data types. Lists are defined by enclosing the elements in square brackets `[ ]` and separating them with commas. Here's how to work with lists in Python:

# ### Creating Lists:

# You can create a list by specifying its elements inside square brackets:

# ```python
# my_list = [1, 2, 3, 4, 5]
# ```

# Lists can also contain elements of different data types:

# ```python
# mixed_list = [1, "hello", 3.14, True]
# ```

# ### Accessing List Elements:

# You can access individual elements of a list using indexing. Python uses zero-based indexing, so the first element is at index 0, the second at index 1, and so on:

# ```python
# my_list = [10, 20, 30, 40, 50]
# first_element = my_list[0]  # Accessing the first element (10)
# second_element = my_list[1]  # Accessing the second element (20)
# ```

# You can also use negative indexing to access elements from the end of the list:

# ```python
# last_element = my_list[-1]  # Accessing the last element (50)
# second_last_element = my_list[-2]  # Accessing the second-to-last element (40)
# ```

# ### Slicing Lists:

# Slicing allows you to extract a portion of a list by specifying a start and end index:

# ```python
# my_list = [1, 2, 3, 4, 5]
# subset = my_list[1:4]  # Returns [2, 3, 4]
# ```

# ### Modifying Lists:

# You can modify individual elements of a list by assigning new values to them:

# ```python
# my_list = [1, 2, 3, 4, 5]
# my_list[2] = 10  # Modifying the third element to be 10
# ```

# ### List Methods:

# Python provides various built-in methods for working with lists. Some commonly used methods include:

# - `append()`: Adds an element to the end of the list.
# - `insert()`: Inserts an element at a specified position.
# - `remove()`: Removes the first occurrence of a specified element.
# - `pop()`: Removes and returns the element at a specified position.
# - `index()`: Returns the index of the first occurrence of a specified element.
# - `count()`: Returns the number of occurrences of a specified element.
# - `sort()`: Sorts the list in ascending order.
# - `reverse()`: Reverses the order of the list.

# ### List Length:

# You can find the length (the number of elements) of a list using the `len()` function:

# ```python
# my_list = [1, 2, 3, 4, 5]
# length = len(my_list)  # Returns 5
# ```

# Lists are versatile and widely used in Python for storing and manipulating collections of data. They are mutable, meaning you can change their contents after creation, making them suitable for a wide range of tasks.


# x = ["book", "pen", "school", "code", 3, 4.4, 3, True, 3j]
# print(x)
# print(len(x))
# print(type(x))

# x = list(("book", "pen", "school", "code", 3, 4.4, 3, True, 3j))
# print(type(x))
# print(x)

# print(x[4])
# print(x[2:6])
# print(x[-9 : -1])
# print(x[::-1]) # Reverse Function
# print(x[:6])
# print(x[4:])

# if "school" in x :
# if "cool" in x :
#     print("Yes" " ""it is there.")
# else :
#     print("No")

# x[2] = "cool"
# print(x)

# x[1:3] = ["home", "room"]
# print(x)

# print(x)
# x[1:2] = ["home", "room"]
# print(x)

# print(x)
# x[1:4] = ["home"]
# print(x)

# Advance list function

# x = ["book", "pen", "school", "code", 3, 4.4, 3, True, 3j]
# print(x)
# y = ["book", "pen", "school", "code", 4, 4.4, 7, True, 7j]
# print(y)

# x.append("Iphone")
# print(x)

# x.insert(3, "Live")
# print(x)

# x.extend(y)
# print(x)

# y.extend(x)
# print(y)

# x.remove("pen")
# print(x)

# x.pop(4)
# print(x)

# x.pop()
# print(x)

# del x[2]
# print(x)

# del x
# print(x)

# x.clear()
# print(x)

# Loop in List

# x = ["book", "pen", "school", "code", "3", "4.4", "3", "True", "3j"]
# print(x)

# for y in x :
#     print(y)

# for i in range(len(x)) :
#     print(x[i])

# i = 0
# while i<len(x) :
#     print(x[i])
#     i=i+1
    
# [print(i) for i in x]

# y = []
# for i in x :
#     if "o" in i :
#         y.append(i)
# print(y)

# y = [i for i in x if "o" in i]
# print(y)

# short, copy and join

x = ["book", "pen", "school", "code", "3", "4.4", "3", "True", "3j"]    

# x.sort()
# print(x)

# x.sort(reverse=True)
# print(x)

# def myfun(n) :
#     return abs(n-50)
# x = [10, 88, 23, 43, 55, 32, 70]   # NOT CLEAR
# x.sort(key = myfun)
# print(x)

# x.reverse()
# print(x)

# y = x.copy()
# print(y)

# y = list(x)
# print(y)

y = [10, 88, 23, 43, 55, 32, 70]

# z = x+y
# print(z)

# for i in y :
#     x.append(i)
# print(x)

# x.extend(y)
# print(x)

# List All Function

# x.append(object)
# x.clear()
# x.copy()
# x.count(value)
# x.extend(iterable)
# x.index(value)
# x.insert(index, object)
# x.pop()
# x.remove(value)
# x.reverse()
# x.sort()
# x.__add__(x)