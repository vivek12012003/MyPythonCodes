import random 


def rand():
    alpha = ('a b c d e f g h i j k l m n o p q r s t u v w x y z')
    r = alpha.split()
    ran = ""
    for i in range(3):
        ran += random.choice(r)
    
    return ran

def decode():
        
    n = input("Enter Your Message : ")

    l = n.split()

    code = ""
    for i in l:
        if(len(i)<=3):
            code += i[::-1] + " "
        else :
            t = i[3:-3]
            new = t[1:] + t[:1]
            code += new + " "

    print(f"Screct Message is : {code}")

def encode():
    n = input("Enter Your Message : ")
    l = n.split()
    code = ""
    for i in l:
        if(len(i)<=3):
            code += i[::-1] + " "
        else :
            t1 = i[len(i)-1:]+i[:len(i)-1]
            code += rand() + t1 + rand() + " "
    
    print(f"Screct code is : {code} ")


while True:
    print('Choose Operation \n1.Encode\n2.Decode\n3.Exit')
    op = int(input())
    if(op == 1):
        encode()
    elif(op == 2):
        decode()
    else:
        break
