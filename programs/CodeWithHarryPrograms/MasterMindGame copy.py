
import random

class Game:   

    ran_digit = random.randrange(1000,100000)
    ldigit = [int(x) for x in str(ran_digit)]
    length = len(str(ran_digit))
    chance = 0   

    def result(self,count,check):   
        
        if count == self.length:
            print(f"Great!\nYou guessed the number in {self.chance} try!\nYou're a Mastermind! ")
            exit()
        elif count == 0:
            print(f"Not quite the number.\nBut you did get {count} digit(s) correct!.")
        else :
            print(f"Not quite the number.\nBut you did get {count} digit(s) correct!\nAlso these numbers in your input were correct.")
            print(check)    


    def checks(self):

        self.guess = guess
        self.lguess = [int(x) for x in str(self.guess)]
        
        
        check = ''

        if len(self.lguess) != self.length:    
            print(f'Error! Enter the {self.length} Digit Number.')

        else :
            self.chance +=1
            count = 0
            for i in range(0,self.length):
                if self.ldigit[i] == self.lguess[i]:
                    check += str(self.ldigit[i]) + " "
                    count += 1
                else :
                    check += 'X '    
            self.result(count,check)
   

g = Game()
while True:    
    guess = int(input(f'\nGuess the {Game.length} Digit Number : '))
    g.checks()


  
