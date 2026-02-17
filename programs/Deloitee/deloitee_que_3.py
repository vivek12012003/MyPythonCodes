

a = "6 6 6 6 6 6"

l1 = a.split(' ')

l2 = [int(i) for i in l1]

n = len(l2)

count = 0 

for i in range (n-1):

    for j in range(i+1,n):

        if l2[i] > 3* l2[j]:
            count += 1


print(count)