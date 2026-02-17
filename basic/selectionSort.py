
arr = [12,3,34,532,3,45,25,45,4,465,87]

n = len(arr)

for i in range (n-1):

    small = i

    for j in range(i+1,n):
        
        if arr[small] > arr[j]: small = j

    arr[i],arr[small] = arr[small],arr[i]

    
print(arr)
