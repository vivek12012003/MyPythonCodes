

s = "aab"
dic = {}
for i in s:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1

print(dic)


