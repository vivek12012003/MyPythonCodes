
def cube(n):    
    l = [int(i) for i in str(n)]
    p = len(str(n))
    s = sum((i**p) for i in l)

    return True if n==s else False

   
    
# num = int(input("Enter the Number : "))

# print(f"{num} is a Armstrong Number." if cube(num) else f"{num} is Not a Armstrong Number.")

#10 arms strong numberr

# b = 5
# c = 0
# a = 10
# while True:
#     if cube(a):
#         print(a,end=" ")
#         c+=1
#     if b == c:
#         break
#     a+=1