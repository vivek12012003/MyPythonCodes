a = input()
b = input()

c ={1:a,2:b}

print(c[2])
print(c[1])

print(c.keys())
print(c.items())
print(c.values())

c[1]= 100

print(c.values())