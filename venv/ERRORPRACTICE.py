import math
try:
    g=open("first.txt","w")
    g.write("YOINK")
except IOError:
    g=open("first.txt","x")
g.close()
try:
    math.sqrt(-1)
except ValueError:
    print("DON'T")
a="1"
b=2
try:
    c=a+b
except TypeError:
    print("its 3")
listy=[0,1,2]
try:
    print(listy[5])
except IndexError:
    listy.append(3)
    listy.append(4)
    listy.append(5)
    print(listy)