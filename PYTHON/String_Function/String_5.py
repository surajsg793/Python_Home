# Strings are a fundamental data type in Python, and Python provides a wide range of built-in string functions (also known as methods) to manipulate and work with strings. Here are some of the most commonly used string functions in Python:

# 1. **String Concatenation:**
#    - `+`: Combines two or more strings.

#    ```python
#    str1 = "Hello"
#    str2 = " World"
#    result = str1 + str2  # "Hello World"
#    ```

# 2. **String Length:**
#    - `len()`: Returns the length of a string.

#    ```python
#    text = "Python"
#    length = len(text)  # 6
#    ```

# 3. **String Indexing:**
#    - You can access individual characters in a string using square brackets and an index (starting from 0 for the first character).

#    ```python
#    text = "Python"
#    first_char = text[0]  # 'P'
#    ```

# 4. **String Slicing:**
#    - You can extract a portion of a string using slicing.

#    ```python
#    text = "Python"
#    slice = text[1:4]  # "yth" (characters at index 1, 2, and 3)
#    ```

# 5. **String Case Conversion:**
#    - `upper()`: Converts a string to uppercase.
#    - `lower()`: Converts a string to lowercase.
#    - `capitalize()`: Capitalizes the first character of a string.
#    - `title()`: Converts the first character of each word to uppercase.

#    ```python
#    text = "hello, world"
#    upper_text = text.upper()  # "HELLO, WORLD"
#    lower_text = text.lower()  # "hello, world"
#    title_text = text.title()  # "Hello, World"
#    ```

# 6. **String Stripping:**
#    - `strip()`: Removes leading and trailing whitespace characters.
#    - `lstrip()`: Removes leading whitespace.
#    - `rstrip()`: Removes trailing whitespace.

#    ```python
#    text = "   Hello, World!   "
#    stripped_text = text.strip()  # "Hello, World!"
#    ```

# 7. **String Searching and Counting:**
#    - `find()`: Searches for a substring and returns the index of the first occurrence (or -1 if not found).
#    - `count()`: Counts the number of occurrences of a substring.

#    ```python
#    text = "Python is fun and Python is powerful"
#    index = text.find("Python")  # 0
#    count = text.count("Python")  # 2
#    ```

# 8. **String Replacement:**
#    - `replace()`: Replaces all occurrences of a substring with another substring.

#    ```python
#    text = "Hello, Python!"
#    new_text = text.replace("Python", "World")  # "Hello, World!"
#    ```

# 9. **String Splitting and Joining:**
#    - `split()`: Splits a string into a list of substrings based on a delimiter.
#    - `join()`: Joins a list of strings into a single string using a delimiter.

#    ```python
#    sentence = "This is a sample sentence."
#    words = sentence.split()  # ['This', 'is', 'a', 'sample', 'sentence.']
#    joined_sentence = "-".join(words)  # 'This-is-a-sample-sentence.'
#    ```

# These are just a few of the many string functions available in Python. They provide powerful tools for working with and manipulating text data.


# x = "chootu"
# y = "chootu"

# print(x)
# print(y)


# z = '''Python string is a sequence of Unicode characters that is enclosed in quotation marks. In this article,
#  we will discuss the in-built function i.e. the            functions provided by Python to operate on strings.'''
# print(z)


# print(z[6])
# print(z[5])

# for x in z :
#     print(x)

# print(len(z))

# print("marks" in z)

# if "Pyton" in z :
#     print("It is there.")
# else :
#     print("It is not there.")

# print(z[2:9])
# print(z[:9])
# print(z[2:])
# print(z[-5:-2])

# print(z.upper())
# print(z.lower())
# a = 'Python string is a sequence of Unicode characters that is enclosed in quotation marks.'

# print(a.strip())

# print(a.replace("Python", "A"))

# b = a.split(",")
# print(b)
# type = 90
# type = "easy"
# b = "Python has many" + type +" features."
# b = "Python has many {} type of features"

# c = a + b
# print(c)

# c = a + " " + b
# print(c)

# print(b)
# print(b.format(type))

# c1 = 10
# c2 = 20
# c3 = 30

# d = "Realme {}, {}, {} is new series mobile."
# print(d.format(c1, c2, c3))

# c1 = 10
# c2 = 20
# c3 = 30

# d = "Realme {2}, {0}, {1} is new series mobile."
# print(d.format(c1, c2, c3))
