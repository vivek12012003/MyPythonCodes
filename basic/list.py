
# a = [1,3,5,7,9]
# b = [c**2 for c in a]
# print(a)
# print(b)

# #condition

# ab = [1,2,3,4,5,6]
# ba = [val for val in ab if val % 2 ==0]
# print(ba)


a = [(x,y) for x in range(3) for y in range (3)]

print('Length of List : ',len(a))
print('Elements of List are : \n',a)



b = [[1,2,3],[4,5,6],[7,8]]
c = [val for d in b for val in d]
print(b)
print(c)


q = [w for w in range(1,20,2)]
print(q)


l1 = [10,20,30,40,50,60,60]
l2 = [70,60,80,90,75,50]
common = list(set(l1) & set (l2))
print(common)
u = list(set(l1) | set(l2))
u.sort()
print(u)

