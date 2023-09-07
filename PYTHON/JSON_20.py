import json
x = '{"Name" : "Suraj", "Age" : 24, "City" : "Bangalore"}'
y = json.loads(x)

print(y["City"])

print(y["Age"])

a = {"Name" : "Suraj", "Age" : 24, "City" : "Bangalore"}
b = json.dumps(a)
print(b)

print(json.dumps({"Name" : "Suraj", "Age" : 24, "City" : "Bangalore"}))
print(json.dumps(["Name", "Suraj", "Age", 24, "City", "Bangalore"]))
print(json.dumps(("Name", "Suraj", "Age" , 24, "City" , "Bangalore")))
print(json.dumps("Hello"))
print(json.dumps(11))
print(json.dumps(2.4))
print(json.dumps(True))
print(json.dumps(None))

import json
c = {"Name" : "Suraj", "Age" : 24, "City" : "Bangalore","details" : ["Name", "Suraj", "Age", 24, "City", "Bangalore"], "About" : ("Name", "Suraj", "Age" , 24, "City" , "Bangalore", None, 11, 4.4, True)}
# d = json.dumps(c)
# print(d)

# e = json.dumps(c, indent = 4)
# print(e)

# f = json.dumps(c, indent=4, separators=(". ", " = "))
# print(f)

g = json.dumps(c, indent=4,sort_keys = True, separators=(". ", " = "))
print(g)