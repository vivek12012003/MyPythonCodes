

stack = [0] * 5

top = -1

size = 5


def push(x):

    global top 
    if top == size - 1:
        print("Stack is Over Flow.")
    
    else:
        top +=1
        stack[top] = x
        print(f"{x} is inserted in the stack. ")

def pop():

    global top
    if top == -1:
        print("Stack is Empty")
    else:
        print(f'{stack[top]} is removed for the list.')
        top -=1

def dispaly():

    if top == -1:
        print("Stack is Empty")
    else :
        print('Stack elments are : ')
        count = 0
        while True:
            if top < count:
                exit()
            print(f"{stack[count]} ",end="",sep="")
            count+= 1


push(10)
push(20)
push(30)
pop()
dispaly()