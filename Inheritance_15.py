# Inheritance is a fundamental concept in object-oriented programming (OOP), and it allows you to create a new class that inherits properties and methods from an existing class. In Python, you can implement inheritance to create a new class, known as the subclass or derived class, based on an existing class, called the superclass or base class. This enables you to reuse and extend code efficiently. Here's how inheritance works in Python:

# ### Creating a Simple Base Class (Superclass):

# ```python
# class Animal:
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species

#     def speak(self):
#         pass  # Subclasses will implement this method

#     def introduce(self):
#         print(f"I am {self.name}, a {self.species}")
# ```

# In this example, `Animal` is a base class with attributes `name` and `species` and methods `speak()` and `introduce()`.

# ### Creating a Subclass (Derived Class):

# You can create a subclass by defining a new class that inherits from the superclass:

# ```python
# class Dog(Animal):
#     def speak(self):
#         return "Woof!"
# ```

# In this example, `Dog` is a subclass of `Animal`. It inherits all attributes and methods from `Animal` and overrides the `speak()` method.

# ### Using the Subclass:

# Now, you can create objects of the subclass and use its methods:

# ```python
# my_dog = Dog("Buddy", "Dog")
# my_dog.introduce()  # Output: "I am Buddy, a Dog"
# print(my_dog.speak())  # Output: "Woof!"
# ```

# The `Dog` subclass inherits the `introduce()` method from the `Animal` superclass and overrides the `speak()` method with its own implementation.

# ### Method Resolution Order (MRO):

# In Python, when a method is called on an object, Python looks for the method in the class of the object first. If it doesn't find it there, it continues searching in the base classes according to a specific order called Method Resolution Order (MRO). You can view the MRO of a class using the `mro()` method:

# ```python
# print(Dog.mro())
# ```

# ### Multiple Inheritance:

# Python supports multiple inheritance, where a class can inherit from multiple base classes. For example:

# ```python
# class Bird(Animal):
#     def speak(self):
#         return "Chirp!"

# class Parrot(Dog, Bird):
#     pass

# my_parrot = Parrot("Polly", "Parrot")
# print(my_parrot.introduce())  # Output: "I am Polly, a Parrot"
# print(my_parrot.speak())  # Output: "Woof!" (inherits from Dog)
# ```

# In this example, `Parrot` inherits from both `Dog` and `Bird`.

# Inheritance is a powerful mechanism in Python that allows for code reuse and the creation of more specialized classes based on existing ones. It's important to design your class hierarchy carefully to ensure that your code remains clear and maintainable.


class myClass6 :
    def __init__(self, A, B) :
        self.A = A
        self.B = B
    def myFun11(self) :
        print((self.A))
        print((self.B))

P1 = myClass6(10, 20)
P1.myFun11()
class myClass7(myClass6) :
    pass

class myClass6 :
    def __init__(self, A, B) :
        self.A = A
        self.B = B

    def myFun12(self) :
        print(self.A)
        print(self.B)
class myClass7(myClass6) :
    pass
x = myClass7(20, 50)
x.myFun12()

class myClass8 :
    def __init__(self, Fname, Lname) :
        self.Fname = Fname
        self.Lname = Lname
    def myFun13(self) :
        print((self.Fname, self.Lname))
class myClass9(myClass8) :
    def __init__(self, Fname, Lname) :
        myClass8.__init__(self, Fname, Lname)
y = myClass9(100, 300)
y.myFun13()

class myClass10 :
    def __init__(self, Name, Age) :
        self.Name = Name 
        self.Age = Age
    def myFun14(self):
        print(str(self.Name), self.Age)

# p2 = myClass10("Amit", 36)
# p3 = myClass10("Alok", 9)

# p2.myFun14()
# p3.myFun14()

class myClass11(myClass10):
    def __init__(self, Name, Age) :
        super().__init__(Name, Age)
x = myClass11("sharad", 39)
x.myFun14()


class School :
    def __init__(self, Name, Roll_No) :
        self.Name = Name
        self.Roll_No = Roll_No
    def STd_DTl(Details):
        print("Student Name : " + str(Details.Name))
        print("Student Roll_No : " + str(Details.Roll_No))
class Student(School) :
    def __init__(self, Name, Roll_No, Year) :
        super().__init__(Name, Roll_No)
        self.Year = Year
    def myDetails(D) :
        print("Year : " + str(D.Year))
# S1 = School("Abhishek", 25)
# S1.STd_DTl()

S1 = Student("Anu", 34, 2009)
S1.myDetails()