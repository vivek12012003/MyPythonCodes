
s = input('Enter the String : ')
lc = 0
uc = 0
for i in s:
    if i.islower():
        lc +=1
    elif i.isupper():
        uc +=1

print("Lower Case in the String '{0}' is {1}".format(s,lc))
print("Upper Case in the String '{0}' is {1}".format(s,uc))
