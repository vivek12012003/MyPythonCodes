import random

#Guess the number game

print("""Let's Play the Game -----
Guess the Number Between 1 to 100.""")
status = True
count = 0
r = random.randrange(1,100)
while status:
    n = int(input("Guess Number : "))
    if not r == n:
        print("Opps!! {0} is Smaller.".format(n) if n < r else "Opps!! {0} is Greater.".format(n))
        status = True
    else:
        print("\n\nYahhh!! You Guess the Correct Number...",r)
        status = False
    count +=1

print("\nYou Took Total {0} Chances.".format(count))
print("\nThankyou For Playing....\nHave a Nice day :)")