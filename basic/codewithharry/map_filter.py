
#map

l = [1,2,3,4,5]

def cube(x):
    return x*x*x

#without using map

# newl = []
# for i in l:
#     newl.append(cube(i))
# print(l)
# print(newl)

# newl = list(map(cube,l))
newl = list(map(lambda x : x*x*x,l))
print(l)
print(newl)




#filter

def filterfunction(a):
    return a>2

# newl1 = list(filter(filterfunction,l))
newl1 = list(filter(lambda a : a>2,l))

print(newl1)