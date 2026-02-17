x = 10
x = "Now a string"
print(x)

#typecasting
a = 10
print(type(a))
b = int(a)
print(type(b))
c = float(a)
print(type(c))
d = str(a)
print(type(d))

#reference

x = 10
print(x)
y = x
print(y)
x = 100
print(x)
print(y)

y =x 
print(y)
y =200
print(y)
print(x)

#delete word
ab = 50
print(ab)
del ab
#print(ab) cause an error

#swapping variable

v,t = 20, 30
print(v,t)
v,t=t,v
print(v,t)


#counting character

l = "vivek sahu"
length = len(l)
print("length of",l,"is :",length)