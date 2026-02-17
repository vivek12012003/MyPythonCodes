import random
i = 0
computer , player = 0 , 0

print('This is 5 Round Game :-')


while True:
    if i== 5:
        break

    i+=1
    print(f"\nRound {i} : ")
    l = ['Snake','Water','Gun']
    print(f'\nScores are :-\nPlayer = {player}\nComputer = {computer}')
    print(f'''
Choose One of Them : 
{l[0]} - 1
{l[1]} - 2
{l[2]}   - 3''')
    p = int(input('Choose : '))

    #random choice
    c = random.choice([1,2,3])

    #0-DRAW, 1- WIN,2-LOSE
    win = [[0,1,2],[2,0,1],[1,2,0]]

    #correct answer
    ans = win[p-1][c-1]

    #result
    # result = ""``
    if (ans == 1):
        result = 'You win'
        player += 1
    elif (ans == 2):
        result = 'You Lose'
        computer +=1
    else :
        result = 'Game Draw'

    print(f"\nYou Choose : {l[p-1]}\nComputer Choose : {l[c-1]}\nSo, the result is : {result}\n")

if(player > computer ):
    print('You Win')
elif(player < computer):
    print('Computer Wins')
else:
    print('Game is Draw')

print(f'\nFinal Scores are :-\nPlayer = {player}\nComputer = {computer}\n')
print('Thanks For Playing....')
