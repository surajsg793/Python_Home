# A dictionary in Python is an unordered collection of key-value pairs. Each key in a dictionary is unique and associated with a specific value. Dictionaries are created using curly braces `{}` or with the `dict()` constructor. Here's an overview of how to work with dictionaries in Python:

# ### Creating a Dictionary:

# You can create a dictionary using curly braces `{}` and specifying key-value pairs separated by colons `:`. For example:

# ```python
# my_dict = {"name": "John", "age": 30, "city": "New York"}
# ```

# Alternatively, you can create an empty dictionary and add key-value pairs later:

# ```python
# empty_dict = {}
# empty_dict["key1"] = "value1"
# empty_dict["key2"] = "value2"
# ```

# ### Accessing Values:

# You can access the values in a dictionary using square brackets and the key:

# ```python
# name = my_dict["name"]  # Accessing the value associated with the key "name"
# ```

# You can also use the `get()` method to access values safely, which returns `None` if the key is not found:

# ```python
# age = my_dict.get("age")  # Accessing the value associated with the key "age"
# ```

# ### Modifying Values:

# You can change the value associated with a key in a dictionary:

# ```python
# my_dict["age"] = 31  # Modifying the value associated with the key "age"
# ```

# ### Removing Key-Value Pairs:

# You can remove a key-value pair from a dictionary using the `del` statement:

# ```python
# del my_dict["city"]  # Removing the key "city" and its associated value
# ```

# ### Checking if a Key Exists:

# You can check if a key exists in a dictionary using the `in` keyword:

# ```python
# if "name" in my_dict:
#     print("The key 'name' exists in the dictionary")
# ```

# ### Dictionary Methods:

# Python dictionaries provide various methods for working with keys and values, including:

# - `keys()`: Returns a list of all keys in the dictionary.
# - `values()`: Returns a list of all values in the dictionary.
# - `items()`: Returns a list of key-value pairs (tuples) as `(key, value)`.

# ```python
# keys = my_dict.keys()
# values = my_dict.values()
# items = my_dict.items()
# ```

# ### Iterating Over a Dictionary:

# You can iterate over the keys, values, or key-value pairs (items) of a dictionary using loops:

# ```python
# for key in my_dict:
#     print(key, my_dict[key])  # Iterating over keys and values

# for key, value in my_dict.items():
#     print(key, value)  # Iterating over key-value pairs
# ```

# Dictionaries are commonly used for mapping and associating data in Python. They are flexible, efficient, and versatile, making them suitable for various tasks like configuration settings, database records, and more.


x = {
  "brand": "Ford",
  "brand": "Kia",
  "model": "Mustang",
  "year": 1964,
  "year": 2020,
  "electric": False,
  "year": 2007,
  "colors": ["red", "white", "blue"]
}
# y = {
#     "child1" :{
#         "name" : "Rahul",
#         "age" : 24
#     },
#     "child2" :{
#         "name" : "Ram",
#         "age" : 27
#     },
#      "child3" :{
#         "name" : "Ramesh",
#         "age" : 30
#     } 
# }

# print(x)

# print(type(x))

# print(x["brand"])

# y = x["colors"]
# print(y)

# print(x["colors"][1])

# y = x.get("year")
# print(y)

# y = x.keys()
# print(y)

# x["year"] = 2009
# print(x["year"])

# y = x.values()
# print(y)

# y = x.items()
# print(y)

# for i in x :
#     print(i)
#     print(x[i])

# if "colors" in x :
    # print("Yes, It is present.")

# x.update({"brand" : "BMW"})
# print(x)

# x.pop("electric")
# print(x)

# x.popitem()
# print(x)

# del x["model"]
# print(x)

# del x
# print(x)

# x.clear()
# print(x)

# for i in x.keys() :
    # print(i)

# for i in x.values() :
#     print(i)

# for i , j in x.items() :
    # print(i , j)

# y = x.copy()
# print(y)

# y = dict(x)
# print(y)

# print(y)
# print(y.keys())
# print(y["child1"]["name"])

child1 = {
        "name" : "Rahul",
        "age" : 24
    },
child2 = {
        "name" : "Ram",
        "age" : 27
    },
child3 = {
        "name" : "Ramesh",
        "age" : 30
    } 

z = {
    "child1" : child1,
    "child2" : child2,
    "child3" : child3
}
print(z)

# Dictionary All Function
# x.clear()
# x.copy()
# x.fromkeys(iterable)
# x.get(key)
# x.items()
# x.keys()
# x.pop(key)
# x.popitem()
# x.setdefault(key)
# x.update(m)
# x.values()
# del x