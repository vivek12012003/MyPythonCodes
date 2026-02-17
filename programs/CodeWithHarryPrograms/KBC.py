
name = input("Enter Your Name : ")
print()
print(f"Welcome to the KBC {name}")

priceAmount = [1000,3000,10000,50000,100000]
print(f"""
Here are the Rules :\n
There are Five Question,
Price for each Answers:
    1 - {priceAmount[0]}
    2 - {priceAmount[1]}
    3 - {priceAmount[2]}
    4 - {priceAmount[3]}
    5 - {priceAmount[4]}""")

def question(i):
    qlist = [[
        "Which of the following is the largest internal organ in the human body?",
        "A. Heart B. Kidney \nC. Liver D. Brain"
    ],
    [
        "If you are using an Apple product, what operating system is most likely running on it?",
        "A. Android B. Windows \nC. iOS/macOS D. Linux"
    ],
    [
        "Which planet is known as the 'Red Planet'?",
        "A. Jupiter B. Venus \nC. Earth D. Mars"
    ],
    [
        "Which unit is commonly used to measure electric current?",
        "A. Volt B. Watt \nC. Ohm D. Ampere"
    ],
    [
        "Which major river flows through the city of Varanasi in India?",
        "A. Yamuna B. Ganga \nC. Godavari D. Brahmaputra"
    ]]
    
    print(qlist[i][0])
    print()
    print(qlist[i][1])
    print()
    
def answer(ans,i):
    anslist = [["C","Liver"],["C","iOS/macOS"],["D","Mars"],["D","Ampere"],["B","Ganga"]]

    if(ans == anslist[i][0]):
        print(f"Good, {anslist[i][1]} is the Correct Answer.\n")
        return True
    else:
        print("\nOops.. Wrong Answer.")
        print(f"Correct Answer is {anslist[i][1]}.")
        return False
     

print("\nSo Lets Start, Here is Your First Question...\n")

amount = 0
for i in range(5):
    question(i)
    ans = input("\nAnswer - ").upper()
    result = answer(ans, i)
    
        
    if result:
        
        if i != 4 :
            amount = priceAmount[i]
            print(f"Your Currently Wining Amount is : {amount}.\n")
            con = input("Want To Play More (Y/N) : ").upper()
            print()
            if con == 'N': break
        else :
            amount += priceAmount[i]
            print(f"Thanks For Playing {name}.\n")
            print(f"Your Wining Amount is : {amount}")
            exit()
    else:
        print(f"You Win : {amount}")
        break

print(f"Thanks For Playing {name}")
    
    