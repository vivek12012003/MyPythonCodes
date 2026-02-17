

# num = int(input("Enter the Number : "))

# l = 0
# f = 1

# if num == 1 :
#     print("0")
# else :
#     print("0 1 ",end = '')
#     for i in range(3,num+1):
#         sum = l + f
#         print(sum, end = ' ')
#         l = f
#         f = sum
        

# more clearer version

# num = int(input("Enter the Number :"))

# a, b = 0 ,1

# if num <0 :
#     print("Enter the Positive Number.")

# elif num ==1:
#     print(a)
# else:
#     print(a,b,end=' ')
    
#     for i in range(3,num+1):
#         c = a+b
#         print(c,end=" ")
#         a,b = b,c

#until reach 1000


num = 1000
a, b = 0 ,1
print(a,b,end=' ')

while True:
    c = a+b
    if c >= num :
        break
    print(c,end=" ")
    a,b = b,c
    
