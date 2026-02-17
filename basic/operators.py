
a = 17
b = 3

print("addition :",a+b)
print("subtraction :",a-b)
print("multiplication :",a*b)
print("division :",a/b)
print("floor division :",a//b)
print("module :",a%b)
print("exponentation :",a**b)


#logical

c = True
d = False
print(c and d)
print(c or d)
print(not c)

#identity operators

e = 23
f = 45
g = e

print(e is not f)
print(g is e)
print(f is g)

#members in operators

ab = 20
cd = 30
ad = 23
list = [10,20,30,40,50]

print(ab in list)
print(cd not in list)
print(ad in list)

#ternary operator

a,b = 10,20
min = a if a<b else b
max = a if a>b else b
print(max)
print(min)