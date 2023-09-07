import re
txt = "the rain is falling in india"
# txt = "in computing plain text is a loose term for data (e.g. file contents) that represent only characters of readable material but not its graphical representation nor other objects (floating-point numbers, images, etc.)"
x = re.search("^the.*india$", txt)
if x :
    print("It is present.")
else :
    print("It is not in the txt.")

y = re.findall("in", txt)
print(y)

z = re.findall("and", txt)
print(z)

a = re.search("\s", txt)
print(a.start())

b = re.search("pattern", txt)
print(b)

c = re.split("\s", txt)
print(c)

d = re.split("\s", txt, 3)
print(d)

e = re.sub("\s", "_NEW_", txt)
print(e)

f = re.sub( "\s", "__repl__", txt, 5)
print(f)
