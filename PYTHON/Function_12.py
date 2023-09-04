# In Python, a function is a block of reusable code that performs a specific task. Functions allow you to organize your code, make it more readable, and reuse it throughout your program. Here's how to define and use functions in Python:

# ### Defining a Function:

# You can define a function using the `def` keyword, followed by the function name and a pair of parentheses `()`. Any parameters (also known as arguments) that the function takes are listed inside the parentheses. The function's code block is indented and defined using a colon `:`.

# ```python
# def my_function(parameter1, parameter2):
#     # Function code goes here
#     result = parameter1 + parameter2
#     return result
# ```

# - `my_function` is the name of the function.
# - `parameter1` and `parameter2` are the input parameters the function takes.
# - `return` is used to specify the value the function should return. If no `return` statement is used, the function returns `None` by default.

# ### Calling a Function:

# To use a function, you call it by its name and provide the required arguments:

# ```python
# result = my_function(10, 20)
# print(result)  # This will print 30
# ```

# ### Function with Default Parameters:

# You can provide default values for function parameters. If a value for a parameter is not provided when calling the function, the default value is used.

# ```python
# def greet(name, greeting="Hello"):
#     return f"{greeting}, {name}"

# message1 = greet("Alice")
# message2 = greet("Bob", "Hi")
# ```

# In this example, the `greet` function has a default value for the `greeting` parameter. You can call it with or without specifying the `greeting` argument.

# ### Keyword Arguments:

# You can use keyword arguments to specify which parameter you're providing a value for, even if the parameters are out of order:

# ```python
# message = greet(greeting="Hey", name="Charlie")
# ```

# ### Variable-Length Argument Lists:

# You can define functions that accept a variable number of arguments using `*args` and `**kwargs`:

# ```python
# def sum_all(*args):
#     total = 0
#     for num in args:
#         total += num
#     return total

# result = sum_all(1, 2, 3, 4, 5)  # This will return 15
# ```

# - `*args` allows you to pass a variable-length list of positional arguments to the function.

# ### Anonymous Functions (Lambda Functions):

# Lambda functions are small, anonymous functions defined using the `lambda` keyword. They are often used for simple, one-line operations.

# ```python
# square = lambda x: x ** 2
# result = square(5)  # This will return 25
# ```

# ### Docstrings:

# It's a good practice to provide documentation for your functions using docstrings. A docstring is a string that describes what the function does and how to use it. It's placed as the first statement in the function body.

# ```python
# def my_function(parameter1, parameter2):
#     """
#     This function adds two numbers and returns the result.
    
#     Parameters:
#     parameter1 (int): The first number to be added.
#     parameter2 (int): The second number to be added.
    
#     Returns:
#     int: The sum of parameter1 and parameter2.
#     """
#     result = parameter1 + parameter2
#     return result
# ```

# These are the basic concepts of functions in Python. Functions are a fundamental building block of Python programming, allowing you to create modular and reusable code.


# print("Hello, This is a pre define Function.")

# def myFun():
#     print("Hello, This is a User define Function.")

# myFun()

# def myFun1(name) :
#     print(name + " Sharma")
# myFun1("Ajay")
# myFun1("Vijay")

# def myFun2(Fname, Lname) :
#     print(Fname + " " + Lname)

# myFun2("Raj", "Kumar")
# myFun2("Shivam", "Kumar")

# def myFun3(*Kids) :
#         i = Kids
#         for i in range(i.__len__()) :
#                 print("The youngest child is "+ Kids[i])
#                 i +=1
# myFun3("Chotu", "Raj", "Vivek", "Rk", "Vinod", "Amit")

# def myFun3(name1, name2, name3) :
#         for i in range(1, 4) :
#                 print('The {i} name of the person is : ' + name3)
#                 i +=1

# myFun3(name2="Ramu", name3="Abhishek", name1="Golu")

# def myFun4(**details) :
#         print("My first name is "+ details["Fname"])
#         print("My last name is "+ details["Lname"])
# myFun4(Fname="Raj", Lname= "Shukla")


# def myFun5(country = ' "Please enter your country name." ') :
#         print("I am from " + country)
# myFun5("India")
# myFun5()
# myFun5("UK")


# def myFun6(x) :
#         for i in x :
#                 print(i)
# y = ["book", "pen", "school", "code", "3", "4.4", "3", "True", "3j"]
# myFun6(y)


# def myFun7(x) :
#         return 2 * x
# print(myFun7(2))
# print(myFun7(5))


# def myFun8(x) :
#         pass
# myFun8(9)

# Lamda Function

# x = lambda a : a*10
# print(x(6))


# x = lambda a , b , c : a+b+c
# print(x(10, 16, 10))


# def myFun9(n) :
#         return lambda  y: y*n
# x = myFun9( 20)
# print(x(10))


# def myFun10(n) :
#         return lambda a : a*n
# x = myFun10(10)
# y = myFun10(10)
# print(x(3))
# print(y(2))


