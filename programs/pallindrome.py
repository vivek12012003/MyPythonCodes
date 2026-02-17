

n1 = int(input("From : "))
n2 = int(input("To : "))

# for i in range(n1,n2+1):
#     temp = str(i)
#     if temp[::-1] == temp:
#         print(temp,end=" ")
    
for i in range (n1, n2+1):
    org = i
    rev = 0
    while not i == 0:
        rem = i % 10
        rev = rev*10+rem
        i //= 10
    if rev == org:
        print(org,end=" ")
