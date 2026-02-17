
a = input("Enter the String :")

v = {"a","e","i","o","u"}
count = 0

for i in a:
    if i in v:
        count +=1

print(count)
