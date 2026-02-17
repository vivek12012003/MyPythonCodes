
def Addition(num1,num2):
    return num1+num2
def Substraction(num1,num2):
    return num1-num2
def Multiply(num1,num2):
    return num1*num2
def Divide(num1,num2):
    return num1/num2

print('--Calculator--')
run = True
while run:
    print('Choose Operation :-')
    print('1. Addition\n2. Substraction\n3. Multiply\n4. Divide\n5. Exit')
    op = int(input())
    if op == 5:
        run = False
        continue
    num1 = int(input("Enter Num1 : "))
    num2 = int(input("Enter Num2 : "))

    match op:
        case 1:
            print(Addition(num1,num2))
        case 2:
            print(Substraction(num1,num2))
        case 3:
            print(Multiply(num1,num2))
        case 4:
            print(Divide(num1,num2))
        case 5:
            run = False
        case _:
            print('Choose Correct Operation.')