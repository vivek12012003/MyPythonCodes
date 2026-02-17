
# 0 se n tk ke element ek array me present h, or usme se ek element miss h wo missing element ka pata krna h with less complexity

a = [1,2,3,5,6]
n = 6
# one way with loop time complexity - O(n^2)
# for i in range (1,n+1):
#     if i in a:
#         continue
#     else:
#         print('Missing Number : ',i)


# # second way way with set time complexity - O(n)
# a_set = set(a)
# for i in range (1,n+1):
#     if i not in a_set:
#         print('Missing number is ',i)


#third way

# sum = 0
# for i in range (1,n+1):
#     sum+=i

#remove above loop
total = n*(n+1)//2

# a_sum = 0
# for i in a:
#     a_sum += i

#short way 
a_sum = sum(a)

print(f'Missing Number is {total - a_sum}')