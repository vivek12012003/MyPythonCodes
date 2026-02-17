
num = int(input('Enter the Number : '))

rev = 0
org  = num
while not num == 0:
    rem = num % 10
    rev = rev *10+rem
    num //=10

print(org)
print(rev)