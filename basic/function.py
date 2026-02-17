

def sum(num):
    s = 0
    for i in num:
        s+=i
    print(s)
    # print(num)



# num1 = int (input('Enter the Number 1 : '))
# num2 = int (input('Enter the Number 2 : '))
# sum(num1,num2)

t = int(input('Calculate digit count : '))
num = []
for i in range(0,t):
    num.append(int(input()))

# print(num)
sum(num)

