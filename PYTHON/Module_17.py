import GlobleVar_3 
GlobleVar_3.Abc(6)

import GlobleVar_3
GlobleVar_3.Person["Age"]

import GlobleVar_3 as Gv   # User Define Module
a = Gv.Person["Age"]
print(a)

import platform         # Pre Define Module
x = platform.system()
print(x)

from GlobleVar_3 import Person as p
print(p["Name"])
