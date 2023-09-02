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


