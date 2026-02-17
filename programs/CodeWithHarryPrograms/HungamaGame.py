
import random, time

def ran():

    words = 'Dabangg, Singham, Rockstar, Barfi, Agneepath, Cocktail, Queen, Haider, Kick, Marykom, Piku, Tamasha, Masaan, Talvar, Airlift, Dangal, Sultan, Rustom, Raazi, Stree, Sanju, Chhichhore, Tanhaji, Thappad, Shershaah, Jawan, Pathaan, Animal, Brahmastra, Fighter, Maidan, Chhaava, Kantara, Vikram, Jailer, Ghajini, Saaho, Robot, Master, Beast, Leo, Pushpa, Kabali, Mersal, Lucifer'

    ran_list = words.split(', ')

    return random.choice(ran_list).lower()

word = ran()
chances = len(word) + 3
word_list = []
guess_word_list = []
try_word = ''
t = 60

def welcome():
    print(f'Welcome\nGuess the word! HINT: word is a name of a Movie')
    print('Total Chances : ',chances)
    print('Word Length : ',len(word))
    for i in word:
        word_list.append(i)
        guess_word_list.append('_')
        print('_ ',end='')
    print()

def check_condition():
    if word_list == guess_word_list:
        print('\nGreat, The Word is : ',word)
        print(f'Chances Used : {(len(word)+3)-chances}')
        exit()
    
    elif chances == 0:
        print('\nOops! Chances Are Ended.')        
        print('The Word is : ',word)
        exit()

def check_guess(guess):

    if guess in word_list:
        for i in range(len(word)):
            if word_list[i] == guess:
                guess_word_list[i] = guess
            
            print(guess_word_list[i]+" ",end='')
        print('\nLeft Chances = ',chances)
    else :
        print(f'{guess} Not Found. Left Chances = {chances}')

    print('Try Words : ',try_word)

       

welcome()
while True: 
    check_condition()
    g = input('\nEnter the Word : ').lower()
    try_word += g + ', '
    chances -= 1
    check_guess(g)





