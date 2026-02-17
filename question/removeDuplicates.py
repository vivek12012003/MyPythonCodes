
a = [1,1,2,3,3,4,4]

#1st way

print(set(a))

#2nd way time comp. = O(n^2)

a1 = list()

for i in a:

    if i in a1:
        continue
    else:
        a1.append(i)

print(a1)

#3rd way without using third variable or any method
k = 0
j = 1
for i in range(0,len(a)):

    if a[k] == a[j]:
        j+=1
    else:
        k+=1
        a[k] = a[j]

print(a)
