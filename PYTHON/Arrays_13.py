# In Python, you can work with arrays using two primary data structures: lists and NumPy arrays.

# 1. **Lists:**
#    Lists are a built-in data structure in Python and are the most commonly used for creating arrays. A list is an ordered collection of items, and these items can be of different data types, including other lists.

#    Here's how to create and work with lists:

#    ```python
#    # Creating a list
#    my_list = [1, 2, 3, 4, 5]

#    # Accessing elements
#    print(my_list[0])  # Accessing the first element, which is 1

#    # Slicing
#    sliced_list = my_list[1:4]  # Returns [2, 3, 4]

#    # Modifying elements
#    my_list[2] = 10  # Modifying the third element

#    # Adding elements
#    my_list.append(6)  # Appends 6 to the end of the list

#    # Removing elements
#    my_list.remove(4)  # Removes the first occurrence of 4

#    # Finding the length of a list
#    length = len(my_list)

#    # Iterating through a list
#    for item in my_list:
#        print(item)

#    # Nesting lists
#    nested_list = [[1, 2], [3, 4]]
#    ```

#    Lists are flexible and versatile but may not be as efficient as NumPy arrays for numerical operations on large datasets.

# 2. **NumPy Arrays:**
#    NumPy (Numerical Python) is a popular library for numerical and scientific computing in Python. It provides a powerful array object called `numpy.ndarray`, which is well-suited for numerical computations. NumPy arrays are homogeneous, meaning all elements in an array must have the same data type.

#    Here's how to create and work with NumPy arrays:

#    ```python
#    import numpy as np

#    # Creating a NumPy array
#    my_array = np.array([1, 2, 3, 4, 5])

#    # Accessing elements
#    print(my_array[0])  # Accessing the first element, which is 1

#    # Slicing
#    sliced_array = my_array[1:4]  # Returns [2, 3, 4]

#    # Modifying elements
#    my_array[2] = 10  # Modifying the third element

#    # Mathematical operations
#    result = my_array * 2  # Multiplies each element by 2

#    # Finding the shape of an array
#    shape = my_array.shape  # Returns (5,)

#    # NumPy functions for arrays
#    mean = np.mean(my_array)  # Calculates the mean
#    max_value = np.max(my_array)  # Finds the maximum value

#    # Array operations
#    array_sum = np.add(my_array, my_array)  # Element-wise addition

#    # Creating multi-dimensional arrays
#    matrix = np.array([[1, 2], [3, 4]])

#    # NumPy provides many advanced features for numerical computing and manipulation.
#    ```

#    NumPy is widely used in scientific and data analysis applications due to its efficiency and rich set of functions for array manipulation and mathematical operations. To use NumPy, you typically need to install it first using a package manager like pip.

# These are the two primary ways to work with arrays in Python. The choice between lists and NumPy arrays depends on your specific requirements and whether you need to perform numerical computations on the array data.


# x = ["book", "pen", "school", "code", "3", "4.4", "3", "True", "3j"]
# print(x)

# x = ["book", "pen", "school", "code", "3", "4.4", "3", "True", "3j"]
# y = x[3]
# print(y)

# x = ["book", "pen", "school", "code", "3", "4.4", "3", "True", "3j"]
# x[2] = "Yamaha"
# print(x)

# x = ["book", "pen", "school", "code", "3", "4.4", "3", "True", "3j"]
# print(len(x))

# x = ["book", "pen", "school", "code", "3", "4.4", "3", "True", "3j"]

# for i in x:
#     print(i)

# x = ["book", "pen", "school", "code", "3", "4.4", "3", "True", "3j"]

# x.append("Life")
# print(x)

# x = ["book", "pen", "school", "code", "3", "4.4", "3", "True", "3j"]
# x.pop(3)
# print(x)

# x = ["book", "pen", "school", "code", "3", "4.4", "3", "True", "3j"]
# x.remove("pen")
# print(x)

# x = ["book", "pen", "school", "code", "3", "4.4", "3", "True", "3j"]
# y = x.copy()
# print(y)

# y[4] = 5
# print(y)
# print(x)

