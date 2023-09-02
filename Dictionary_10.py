x = {
  "brand": "Ford",
  "brand": "Kia",
  "model": "Mustang",
  "year": 1964,
  "year": 2020,
  "electric": False,
  "year": 2007,
  "colors": ["red", "white", "blue"]
}
# y = {
#     "child1" :{
#         "name" : "Rahul",
#         "age" : 24
#     },
#     "child2" :{
#         "name" : "Ram",
#         "age" : 27
#     },
#      "child3" :{
#         "name" : "Ramesh",
#         "age" : 30
#     } 
# }

# print(x)

# print(type(x))

# print(x["brand"])

# y = x["colors"]
# print(y)

# print(x["colors"][1])

# y = x.get("year")
# print(y)

# y = x.keys()
# print(y)

# x["year"] = 2009
# print(x["year"])

# y = x.values()
# print(y)

# y = x.items()
# print(y)

# for i in x :
#     print(i)
#     print(x[i])

# if "colors" in x :
    # print("Yes, It is present.")

# x.update({"brand" : "BMW"})
# print(x)

# x.pop("electric")
# print(x)

# x.popitem()
# print(x)

# del x["model"]
# print(x)

# del x
# print(x)

# x.clear()
# print(x)

# for i in x.keys() :
    # print(i)

# for i in x.values() :
#     print(i)

# for i , j in x.items() :
    # print(i , j)

# y = x.copy()
# print(y)

# y = dict(x)
# print(y)

# print(y)
# print(y.keys())
# print(y["child1"]["name"])

child1 = {
        "name" : "Rahul",
        "age" : 24
    },
child2 = {
        "name" : "Ram",
        "age" : 27
    },
child3 = {
        "name" : "Ramesh",
        "age" : 30
    } 

z = {
    "child1" : child1,
    "child2" : child2,
    "child3" : child3
}
print(z)

# Dictionary All Function
# x.clear()
# x.copy()
# x.fromkeys(iterable)
# x.get(key)
# x.items()
# x.keys()
# x.pop(key)
# x.popitem()
# x.setdefault(key)
# x.update(m)
# x.values()
# del x