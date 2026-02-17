
s = int(input("Enter the Shape :"))
n = int(input("Enter the Number :"))


# print("Forward")
# for i in range(0,n):  
#     for j in range (0,i+1):
#         print('*', end='')
#     print()


# print("Backward")

# for i in range(n,0,-1):
#     for j in range (0,i+1):
#         print('*', end='')
#     print()



# print("Forward Space")
# for i in range (1,n+1):
#     for j in range (0,n-i):
#         print(" ",end='')

#     for k in range (0,i):
#         print("*",end='')
#     print()

# print("Backward Space")
# for i in range (0,n):
#     for j in range(0,i):
#         print(' ',end='')
#     for k in range(0,n-i):
#         print('*',end='')
#     print()


#print(" Forward Triangle")

    
for i in range (0,n):
    for a in range(0,s):    
        for j in range (0,n-(i+1)):
            print(" ",end='')

        for k in range (0,i+1):
            print("*",end='')
        
        for l in range (0,i):
            print("*",end='')

        for b in range(0,n-i):
            print(" ",end='')
    print()


# print("Backward Triangle")

for i in range (0,n):
    if i ==0:
        continue
    for a in range(0,s):    
        for j in range (0,i):
            print(" ",end='')

        for k in range (0,n-i):
            print("*",end='')
        
        for l in range (0,n-(i+1)):
            print("*",end='')

        for b in range(0,i+1):
            print(" ",end='')
    print()

