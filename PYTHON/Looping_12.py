# In Python, you can use loops to repeatedly execute a block of code. Python provides two main types of loops: `for` loops and `while` loops. Here's an overview of how to use each type of loop:

# ### `for` Loops:

# A `for` loop is used to iterate over a sequence (such as a list, tuple, string, or range) or any iterable object. It allows you to execute a block of code for each item in the sequence. The `for` loop in Python is particularly useful when you know how many times you want to execute a block of code.

# **Syntax:**

# ```python
# for variable in sequence:
#     # Code to be executed for each item in the sequence
# ```

# Here's an example of a `for` loop:

# ```python
# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)
# ```

# ### `range()` Function with `for` Loops:

# The `range()` function generates a sequence of numbers that can be used with `for` loops. It is often used when you want to execute a block of code a specific number of times.

# **Syntax:**

# ```python
# for variable in range(start, stop, step):
#     # Code to be executed for each value in the range
# ```

# Example:

# ```python
# for i in range(1, 6):  # Generates numbers from 1 to 5
#     print(i)
# ```

# ### `while` Loops:

# A `while` loop is used when you want to repeatedly execute a block of code as long as a certain condition is `True`. `while` loops are useful when you don't know in advance how many times the loop should run.

# **Syntax:**

# ```python
# while condition:
#     # Code to be executed as long as the condition is True
# ```

# Example:

# ```python
# count = 0
# while count < 5:
#     print(count)
#     count += 1
# ```

# ### Loop Control Statements:

# Python provides loop control statements that allow you to control the flow of loops:

# - `break`: Terminates the loop prematurely, even if the loop condition is still `True`.
# - `continue`: Skips the current iteration and continues with the next iteration of the loop.
# - `else` in `for` and `while` loops: Allows you to specify a block of code to be executed when the loop has completed normally (i.e., without encountering a `break` statement).

# Here's an example using `break` and `continue`:

# ```python
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# for num in numbers:
#     if num % 2 == 0:
#         continue  # Skip even numbers
#     if num == 7:
#         break  # Exit the loop when 7 is encountered
#     print(num)
# else:
#     print("Loop completed normally")
# ```

# Understanding and effectively using loops is a fundamental skill in Python programming, as it allows you to perform repetitive tasks and iterate over data structures.


# i = 0
# while i < x :
#     print(i)
#     i +=1

# i = 0
# while i < x :
#     print(i)
#     if i == 5 :
#         break
#     i +=1


# i = 0
# while i < x :
#     i +=1
#     if i == 5 :
#         continue
#     print(i)


# i = 0
# while i < y :
#     print(i)
#     i +=1
# else :
#     print("It is last value of y." )

x = ["book", "pen", "school", "code", "3", "4.4", "3", "True", "3j"]

# for i in x :
#     print(i)

# for i in "code" :
#     print(i)

# for i in x :
#     print(i)
#     if i in "code" :
#         break


# for i in x :
#     if i in "code" :
#         break
#     print(i)

# for i in x :
#     if i in "code" :
#         continue
#     print(i)

# for i in x :
#     print(i)
#     if i in "code" :
#         continue
    
# for i in range(10) :
    # print(i+1)

# for i in range(2, 20) :
#     print(i)

# for i in range(1, 29, 3) :
#     print(i)

# for i in range(20) :
#     print(i)
# else :
#     print("and 20 ")


# for i in range(23) :
#     print(i)
#     if i == 20 :
#         break
#     print(i)
# else :
#     print("Game over.")


# for i in range(23) :
#     print(i)
#     if i == 20 :
#         continue
#     print(i)
# else :
#     print(i+1)
#     print("Game over.")

# for i in range(20) :
#     for j in range(20):
#         if i == j :
#             print(i+j)
#         else :
#             print(j)

# for i in range(20) :
#     for j in range(20):
#         if i == j :
#             print(i, j)

# for i in [1, 2, 4, 6] :
#     pass