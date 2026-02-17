

def average(*l):
    sum = 0
    for i in l :
        sum +=i
    
    return sum/len(l)

c = average(2,3,4,5)
print(c)


