# Iterators in Python are objects that represent a sequence of elements or a collection of items. They allow you to traverse through the elements of a sequence one at a time without the need to load the entire sequence into memory. Iterators are widely used in Python, especially with constructs like loops and comprehensions. To work with iterators, you need to understand two important methods: `iter()` and `next()`.

# Here's how iterators work in Python:

# 1. **Iterable Objects**: An object is considered iterable if it can be iterated over, meaning you can loop through its elements. Examples of iterable objects include lists, tuples, strings, dictionaries, and sets.

# 2. **Iterator Objects**: An iterator is an object that implements two methods, `__iter__()` and `__next__()`. The `__iter__()` method returns the iterator object itself, and the `__next__()` method returns the next value from the sequence. When there are no more items to return, it raises the `StopIteration` exception.

# Here's a simple example of creating and using an iterator:

# ```python
# # Creating an iterable object
# my_list = [1, 2, 3, 4, 5]

# # Creating an iterator from the iterable
# my_iterator = iter(my_list)

# # Using the iterator to get values one at a time
# print(next(my_iterator))  # Output: 1
# print(next(my_iterator))  # Output: 2
# print(next(my_iterator))  # Output: 3
# ```

# You can also use a `for` loop to iterate through an iterable:

# ```python
# for item in my_list:
#     print(item)
# ```

# Behind the scenes, Python uses iterators to implement this loop.

# To create your own iterable object and iterator, you need to implement the `__iter__()` and `__next__()` methods in a custom class. Here's an example:

# ```python
# class MyIterable:
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end

#     def __iter__(self):
#         self.current = self.start
#         return self

#     def __next__(self):
#         if self.current < self.end:
#             result = self.current
#             self.current += 1
#             return result
#         raise StopIteration

# # Using the custom iterable and iterator
# my_custom_iterable = MyIterable(1, 5)
# for item in my_custom_iterable:
#     print(item)
# ```

# In this example, `MyIterable` is a custom iterable class that defines its own `__iter__()` and `__next__()` methods.

# Understanding iterators is essential when working with Python's looping constructs, comprehensions, and when processing large data sets efficiently. Iterators allow you to work with sequences of data without having to load the entire sequence into memory, making your code more memory-efficient.




# lists = [1, 2, 3, 4, 5, 6 ]
# y = iter(lists)
# x = "Apple"
# y = iter(x)

# print(next(y))
# print(next(y))
# print(next(y))
# print(next(y))
# print(next(y))
# print(next(y))

# for i in lists :
#     print(i)

# for i in x :
#     print(i)

# class Number :
#     def __iter__(self) :
#         self.a = 1
#         return self
#     def __next__(self) :
#         x = self.a
#         self.a += 1
#         return x
# myclass = Number()
# y = iter(myclass) 

# print(next(y))
# print(next(y))
# print(next(y))


class Number :
    def __iter__(self) :
        self.b = 1
        return self
    def __next__(self) :
        if self.b <= 20 :
            x = self.b
            self.b += 1
            return  x
        else :
            raise StopIteration
myclass = Number()
y = iter(myclass)

for i in y :
    print(i)
    
# print(next(y))
# print(next(y))
# print(next(y))
