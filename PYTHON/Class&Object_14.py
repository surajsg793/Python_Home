# In Python, a class is a blueprint or a template for creating objects, and an object is an instance of a class. Classes define the attributes (data members) and behaviors (methods) that objects of the class will have. Here's a basic overview of classes and objects in Python:

# ### Defining a Class:

# You can define a class using the `class` keyword, followed by the class name. Inside the class, you can define attributes and methods.

# ```python
# class MyClass:
#     # Constructor method (__init__)
#     def __init__(self, attribute1, attribute2):
#         self.attribute1 = attribute1
#         self.attribute2 = attribute2

#     # Instance method
#     def some_method(self):
#         return f"Attribute1: {self.attribute1}, Attribute2: {self.attribute2}"
# ```

# - The `__init__` method is a special method called a constructor. It is used to initialize object attributes when an object is created. The `self` parameter refers to the instance of the class and is used to access instance variables.
# - `attribute1` and `attribute2` are instance variables, which are specific to each object created from the class.
# - `some_method` is an instance method, which can access and manipulate the object's attributes.

# ### Creating Objects:

# Once you have defined a class, you can create objects (instances) of that class by calling the class as if it were a function, passing any required arguments to the constructor:

# ```python
# # Creating objects
# obj1 = MyClass("Value1", "Value2")
# obj2 = MyClass("Hello", "World")

# # Accessing object attributes
# print(obj1.attribute1)  # "Value1"
# print(obj2.attribute2)  # "World"

# # Calling object methods
# result1 = obj1.some_method()  # "Attribute1: Value1, Attribute2: Value2"
# result2 = obj2.some_method()  # "Attribute1: Hello, Attribute2: World"
# ```

# ### Class and Instance Variables:

# - Class variables are shared among all instances of a class and are defined within the class but outside of any methods. They are accessed using the class name or an instance.
# - Instance variables are specific to each instance of a class and are defined inside the constructor or instance methods using the `self` keyword.

# ```python
# class MyClass:
#     class_var = 0  # Class variable

#     def __init__(self, instance_var):
#         self.instance_var = instance_var  # Instance variable

#     def increment_class_var(self):
#         MyClass.class_var += 1

# # Creating objects
# obj1 = MyClass("Object 1")
# obj2 = MyClass("Object 2")

# print(obj1.class_var)  # 0
# print(obj2.class_var)  # 0

# obj1.increment_class_var()
# print(obj1.class_var)  # 1
# print(obj2.class_var)  # 1
# ```

# In this example, `class_var` is a class variable shared among all instances, while `instance_var` is an instance variable unique to each object.

# Python's object-oriented programming features, including classes and objects, are powerful and flexible, allowing you to model and organize your code in a structured and reusable manner.

# class myClass :
#     x = 5
# print(myClass)

# p1 = myClass()
# print(p1.x)

# class myClass1 :
#     def __init__(self, name, age) :
#         self.name = name
#         self.age = age
# p1 = myClass1("Ram", 19)

# print(p1.name, p1.age)
# print(p1.age)

# class myClass2 :
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def myfunc(self) :
#         print("My name is " + self.name)
#         print(" and my age is " + str(self.age))
# p1 = myClass2("Vivek", 30)
# p1.myfunc()

# class myClass3 :
#     def __init__(s, x, y):
#         s.x = x
#         s.y = y
#     def myfunc1(slf) :
#         print("This is add of two number " + str(slf.x + slf.y))
# p1 = myClass3(10, 29)
# p1.myfunc1()

# class myClass4 :
#     def __init__(s, n, a):
#         s.a = a
#         s.n = n
#     def myfunc2(any):
#         print("My name is " + any.n)
#         print("My age is " + str(any.a))
# p1 = myClass4("chiku", 12)
# p1.myfunc2()
# p1.a = 19
# p1.myfunc2()
# print(p1.a)


# class myClass5 :
#     def __init__(self, Name, Age, DOB, Gender):
#         self.Name = Name
#         self.Age = Age
#         self.DOB = DOB
#         self.Gender = Gender
#     def myfunc3(slf):
#         print(" Name : " + slf.Name)
#         print(" Age : " + str(slf.Age))
#         print(" DOB : " + str(slf.DOB))
#         print(" Gender : " + slf.Gender)
# p1 = myClass5("Rajat", 43, 23_01_1980, "Male")
# p1.myfunc3()
# p1.Age = 44
# del p1.Age   #Delete Properties Only
# del p1       #Delete Object


