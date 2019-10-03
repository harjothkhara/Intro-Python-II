value assigments
Integers, Strings, Floats
x-->[24]
y-->[24]

---

x = 12
y = x
y = 24
print(x) # 12
print(y) # 24
x = y
print(x) # 24
=====================================
Reference assignments
Objects, Lists, Dictionaries
[Room('outside')]
^
|
y
x-->[Room('foyer')]

---

x = Room('outside')
y = x
x = Room('foyer')
