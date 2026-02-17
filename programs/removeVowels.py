
s = input("Enter the String : ")

# v = ('a','A','e','E','i','I','o','O','u','U')

# ns = ""
# for i in s:
#     if i not in v:
#         ns += i
# print(ns)


# using set

vowels = set('aeiouAEIOU')

ns = "".join(ch for ch in s if ch not in vowels)
print(ns)