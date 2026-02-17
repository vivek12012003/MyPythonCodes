#s = input("Enter teh Sentence: ")
s = "vivek is a very awesome boy"
s1 = s.split()
l = 0
index = 0
count = 0
for i in s1:
    if len(i) >l:
        l = len(i)
        index = count
    count+=1

print(s1[index])
    

#best version

longest = max(s.split(), key=len)
print(longest)