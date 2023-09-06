# In Python, variables can have different scopes, primarily divided into two categories: global variables and local variables. The scope of a variable determines where in your code it can be accessed or modified. Here's an explanation of global and local variables in Python:

# ### Global Variables:

# 1. **Global Scope:** Variables defined outside of any function are considered global variables. They are accessible from anywhere in the program, including inside functions.

# Example:

# ```python
# global_var = 10  # This is a global variable

# def my_function():
#     print(global_var)  # Accessing the global variable

# my_function()  # This will print 10
# ```

# 2. **Modifying Global Variables:** To modify a global variable from within a function, you need to use the `global` keyword.

# ```python
# global_var = 10

# def modify_global():
#     global global_var
#     global_var = 20

# modify_global()
# print(global_var)  # This will print 20
# ```

# ### Local Variables:

# 1. **Local Scope:** Variables defined inside a function are considered local variables. They are only accessible within that function and have a limited lifetime, existing only as long as the function is executing.

# Example:

# ```python
# def my_function():
#     local_var = 5  # This is a local variable
#     print(local_var)

# my_function()  # This will print 5
# # print(local_var)  # This will raise a NameError because local_var is not defined in the global scope
# ```

# 2. **Shadowing:** If a local variable has the same name as a global variable, it "shadows" the global variable within the function. The function uses the local variable instead of the global one.

# ```python
# my_var = 10  # Global variable

# def shadowing_example():
#     my_var = 5  # Local variable with the same name as the global variable
#     print(my_var)

# shadowing_example()  # This will print 5
# print(my_var)  # This will print 10 (global variable is not affected)
# ```

# ### LEGB Scope Resolution:

# Python follows the LEGB (Local, Enclosing, Global, Built-in) rule for variable scope resolution. When you reference a variable, Python searches for it in the following order:

# 1. Local Scope: Inside the current function.
# 2. Enclosing Scope: In the local scope of enclosing functions (for nested functions).
# 3. Global Scope: At the global level (outside all functions).
# 4. Built-in Scope: In Python's built-in namespace (e.g., functions like `print`, `len`, etc.).

# If the variable is not found in any of these scopes, a `NameError` is raised.

# Understanding variable scope is crucial for writing maintainable and bug-free Python code. It helps you manage the visibility and lifetime of variables in your programs effectively.


# x = "Globle Variable"
# def myFunction_g():
#     print(x)
# myFunction_g()

# def myFunction_l():
#     x = "Local Variable"
#     print(x)
# myFunction_l()

# print(x)

# def Var():
#     x = 10
#     print(x)
# Var()

# def LocalVar() :
#     x = 20
#     def InnerVar() :
#         print(x)
#     InnerVar()
# LocalVar()

# x = 200

# def GlobalVar() :
#     print(x)
# GlobalVar()

# x = 2
# def Two() :
#     x = 3
#     print(x)
# Two()
# print(x)

# def Local() : 
#     global x
#     x = 12
#     # print(x)
# Local()
# print(x)

# x = 20
# def Abc() :
#     global x
#     x = 11
#     # print(x)
# Abc()
# print(x)

def Abc(x) :
     print(x)

Person = {
    "Name" : "Rajesh",
    "Age" : 32, 
    "Group" : "B"
}