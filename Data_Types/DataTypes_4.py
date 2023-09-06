# Built in DataType

# Text type : str
# Numeric type : int, float, complex
# Sequence type : list,truple, string, range
# Mapping : dict
# Set type : set, frozenset
# Boolean type : boolean
# Binary type : bytes, bytearray, memoryview

x = 5 # int
y = "chotu " # str
a = 20.4 # float
b = 2+3j # complex
c = [1, 12, "Raj", "golu"] # list
d = (1, 12, "Raj", "golu") # tuple
e = {"Name" : "Chotu", "Age" : 12} # dict
f = {"Apple ", "Banana ", "Orange"} # set
g = range(5) # range
h = True # bool
# i = b"byteArray" # bytearray
j = bytes(3)

l = memoryview(bytes(5)) # memoryview


# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))
# print(type(f))
# print(type(g))
# print(type(h))
# # print(type(i))
# print(type(j))
# print(type(l))
# print(type(x))
# print(type(y))

# print((a))
# print((b))
# print((c))
# print((d))
# print((e))
# print((f))
# print((g))
# print((h))
# # print((i))
# print((j))
# print((l))
# print((x))
# print((y))

m = float(x)
print(m)

n = int(a)
print(n)

o = complex(x)
print(o)

# p = int(b)
# print(p)

import random
q = random.randrange(1, 20)+1
print(q)



