
f = [1,2,4,5,5,6]

print(f)

# f.clear()
# print(f)

print(f.count(5))

f.insert(1,10)

print(f)


a = [7,8,9,0]

f.extend(a)

print(f)

f.append(a)

print(f)

f.extend((12,34))
print(f)

f.extend('hi')
print(f)