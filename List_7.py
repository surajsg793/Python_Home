# x = ["book", "pen", "school", "code", 3, 4.4, 3, True, 3j]
# print(x)
# print(len(x))
# print(type(x))

# x = list(("book", "pen", "school", "code", 3, 4.4, 3, True, 3j))
# print(type(x))
# print(x)

# print(x[4])
# print(x[2:6])
# print(x[-9 : -1])
# print(x[::-1]) # Reverse Function
# print(x[:6])
# print(x[4:])

# if "school" in x :
# if "cool" in x :
#     print("Yes" " ""it is there.")
# else :
#     print("No")

# x[2] = "cool"
# print(x)

# x[1:3] = ["home", "room"]
# print(x)

# print(x)
# x[1:2] = ["home", "room"]
# print(x)

# print(x)
# x[1:4] = ["home"]
# print(x)

# Advance list function

# x = ["book", "pen", "school", "code", 3, 4.4, 3, True, 3j]
# print(x)
# y = ["book", "pen", "school", "code", 4, 4.4, 7, True, 7j]
# print(y)

# x.append("Iphone")
# print(x)

# x.insert(3, "Live")
# print(x)

# x.extend(y)
# print(x)

# y.extend(x)
# print(y)

# x.remove("pen")
# print(x)

# x.pop(4)
# print(x)

# x.pop()
# print(x)

# del x[2]
# print(x)

# del x
# print(x)

# x.clear()
# print(x)

# Loop in List

# x = ["book", "pen", "school", "code", "3", "4.4", "3", "True", "3j"]
# print(x)

# for y in x :
#     print(y)

# for i in range(len(x)) :
#     print(x[i])

# i = 0
# while i<len(x) :
#     print(x[i])
#     i=i+1
    
# [print(i) for i in x]

# y = []
# for i in x :
#     if "o" in i :
#         y.append(i)
# print(y)

# y = [i for i in x if "o" in i]
# print(y)

# short, copy and join

x = ["book", "pen", "school", "code", "3", "4.4", "3", "True", "3j"]    

# x.sort()
# print(x)

# x.sort(reverse=True)
# print(x)

# def myfun(n) :
#     return abs(n-50)
# x = [10, 88, 23, 43, 55, 32, 70]   # NOT CLEAR
# x.sort(key = myfun)
# print(x)

# x.reverse()
# print(x)

# y = x.copy()
# print(y)

# y = list(x)
# print(y)

y = [10, 88, 23, 43, 55, 32, 70]

# z = x+y
# print(z)

# for i in y :
#     x.append(i)
# print(x)

# x.extend(y)
# print(x)

# List All Function

# x.append(object)
# x.clear()
# x.copy()
# x.count(value)
# x.extend(iterable)
# x.index(value)
# x.insert(index, object)
# x.pop()
# x.remove(value)
# x.reverse()
# x.sort()
# x.__add__(x)