

arr = [345,3432,3,4,32,2,4,5,32,23]


n = len(arr)

for i in range (n-1):

    for j in range (0,n-i-1):

        if arr[j+1] < arr[j] :
            arr[j+1],arr[j] = arr[j],arr[j+1]

print(arr)
