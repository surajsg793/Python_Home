# In Python, a set is an unordered collection of unique elements. Sets are similar to lists and tuples, but they do not allow duplicate values. They are defined using curly braces `{}` or the `set()` constructor. Here's an overview of how to work with sets in Python:

# ### Creating Sets:

# You can create a set by specifying its elements inside curly braces `{}`:

# ```python
# my_set = {1, 2, 3, 4, 5}
# ```

# Alternatively, you can create a set from a list or another iterable using the `set()` constructor:

# ```python
# my_set = set([1, 2, 3, 4, 5])
# ```

# ### Adding and Removing Elements:

# - **Adding Elements:** You can add elements to a set using the `add()` method:

#   ```python
#   my_set.add(6)
#   ```

# - **Removing Elements:** You can remove elements from a set using the `remove()` method. If the element is not found, a `KeyError` is raised. To avoid this, you can use the `discard()` method, which removes the element if it exists and does nothing if it doesn't:

#   ```python
#   my_set.remove(3)  # Removes 3 from the set
#   my_set.discard(10)  # Does nothing because 10 is not in the set
#   ```

# ### Set Operations:

# Python sets support various set operations, such as union, intersection, difference, and symmetric difference, which are performed using methods or operators:

# - **Union (`|` or `union()`):** Combines two sets, returning a new set containing all unique elements from both sets.

#   ```python
#   set1 = {1, 2, 3}
#   set2 = {3, 4, 5}
#   union_set = set1 | set2  # or set1.union(set2)
#   ```

# - **Intersection (`&` or `intersection()`):** Returns a new set containing elements that are common to both sets.

#   ```python
#   set1 = {1, 2, 3}
#   set2 = {3, 4, 5}
#   intersection_set = set1 & set2  # or set1.intersection(set2)
#   ```

# - **Difference (`-` or `difference()`):** Returns a new set containing elements that are in the first set but not in the second set.

#   ```python
#   set1 = {1, 2, 3}
#   set2 = {3, 4, 5}
#   difference_set = set1 - set2  # or set1.difference(set2)
#   ```

# - **Symmetric Difference (`^` or `symmetric_difference()`):** Returns a new set containing elements that are in either of the sets, but not in both.

#   ```python
#   set1 = {1, 2, 3}
#   set2 = {3, 4, 5}
#   symmetric_difference_set = set1 ^ set2  # or set1.symmetric_difference(set2)
#   ```

# ### Set Methods:

# Python sets provide various methods for working with sets, including `add()`, `remove()`, `discard()`, `clear()`, `pop()`, `copy()`, and others.

# ```python
# my_set.add(6)  # Add an element
# my_set.remove(3)  # Remove an element
# my_set.discard(10)  # Remove an element safely
# my_set.clear()  # Remove all elements from the set
# element = my_set.pop()  # Remove and return an arbitrary element
# new_set = my_set.copy()  # Create a shallow copy of the set
# ```

# Sets are useful for tasks that involve unique elements or testing membership of an element. They offer efficient operations for finding unions, intersections, and differences between sets.


x = {"book", "pen", "school", "code", "3", "4.4", 3, 23, True, "3j"}
y = set((10, 88, 23, 43, 55, 32, 70, 3))

# print(x)
# print(len(x))
# print(type(x))

# for i in x :
#     print(i)

# print("code" in x)

# if "schol" in x :
#     print("Yes, It is there.")
# else :
#     print("No")

# x.add("element")
# print(x)

# x.update(y)
# print(x)

# x.remove("code")
# print(x)

# x.discard("code")
# print(x)

# print(x)
# z = x.pop()
# print(z)
# print(x)

# x.clear()
# print(x)

# del x
# print(x)

# z = x.union(y)
# print(z)

# x.update(y)
# print(x)

# z = x.intersection(y)
# print(z)

# x.intersection_update(y)
# print(x)

# z = x.symmetric_difference(y)
# print(z)

# x.symmetric_difference_update(y)
# print(x)

# Set All Functions

# x.add(element)
# x.clear()
# x.copy()
# x.difference()
# x.difference_update()
# x.discard(element)
# x.intersection()
# x.intersection_update()
# x.isdisjoint(s)
# x.issubset(s)
# x.issuperset(s)
# x.pop()
# x.symmetric_difference(s)
# x.symmetric_difference_update(s)
# x.update()
# x.union()
# x.remove(element)
# del x

