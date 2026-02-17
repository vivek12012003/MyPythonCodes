
import random

ran_digit = random.randrange(1000,100000)
ldigit = [int(x) for x in str(ran_digit)]
length = len(str(ran_digit))
chance = 0

while True :

    guess = int(input(f'\nGuess the {length} Digit Number : '))
    lguess = [int(x) for x in str(guess)]

    check = ''

    if len(lguess) != length:    
        print(f'Error! Enter the {length} Digit Number.')

    else :
        chance +=1
        count = 0
        for i in range(0,length):
            if ldigit[i] == lguess[i]:
                check += str(ldigit[i]) + " "
                count += 1
            else :
                check += 'X '

        if count == length:
            print(f"Great!\nYou guessed the number in {chance} try!\nYou're a Mastermind! ")
            exit()
        elif count == 0:
            print(f"Not quite the number.\nBut you did get {count} digit(s) correct!.")
        else :
            print(f"Not quite the number.\nBut you did get {count} digit(s) correct!\nAlso these numbers in your input were correct.")
            print(check)
            