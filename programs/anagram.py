
s1 = input("String 1 : ")
s2 = input("String 2 : ")

# if len(s1) == len (s2):
#     temp1 = "".join(ch for ch in sorted(s1))
#     temp2 = "".join(ch for ch in sorted(s2))
#     if temp1 == temp2 :
#         print("Anagram.")
#     else:
#         print("Not Anagram")

# else:
#     print("Not Anagram")

#best clean version

s1_clean = (sorted(s1.replace(" ","").lower()))
s2_clean = (sorted(s2.replace(" ","").lower()))

print("Anagram" if s1_clean == s2_clean else "Not Anagram.")
