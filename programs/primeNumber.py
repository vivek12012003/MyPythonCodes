
# #check prime number


# num = int(input("Enter the Number : "))
# count = 0
# for i in range(1, num+1):
#     if num%i == 0:
#         count+=1
        
# print("Yes" if count == 2 else "No")
num = int(input("Enter the Number : "))

# for i in range (1,num+1):
#     count = 0
#     for j in range (1, i+1):
#         if i % j == 0 :
#             count +=1
#         if count > 2:
#             break
#     if count <= 2 and not i == 1 :
#         print(i, end = ' ')

# n number prime
i = 1
c = 0
while True:

    count = 0
    for j in range (1, i+1):
        if i % j == 0 :
            count +=1
        if count > 2:
            break
    if count <= 2 and not i == 1 :
        print(i, end = ' ')
        c+=1
    if c == num:
        break
    i+=1
