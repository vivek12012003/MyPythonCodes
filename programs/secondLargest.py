

a = [10,123,12,234,435,3432,3424]
max1 = 0
max2 = 0
for i in a:
    if max1 <= i:
        max1 = i
for i in a:
    if (max2 <= i and i < max1):
        max2 = i

print(max1)
print(max2) 