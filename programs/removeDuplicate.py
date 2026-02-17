
s = input("Enter the Sentence : ")

s1 = s.split()
word = []

for w in s1:
    if w not in word:
        word.append(w)

print(" ".join(word))