
class Account():

    def __init__(self,account,balance):
        self.account = account
        self.balance = balance
    def debit(self):
        print("Enter the amount to debit from '{}' account : ".format(self.account),end="",)
        amount = int(input())
        if amount > self.balance :
            print('Insufficient Balance.')
            return
        self.balance = self.balance -  amount
        print("{} amount is debit form '{}' account".format(amount,self.account))
    def credit(self):
        amount = int(input("Enter the amount to credit in '{}' account : ".format(self.account)))
        self.balance = self.balance + amount
        print(f"{amount} is credit in '{self.account}' account")
    def balance_print(self):
        print(f"Balance in {self.account} is : {self.balance}")
    

account_no = int(input("Enter the Account Number : "))
balance = int(input("Enter the Deposit amount : "))

u1 = Account(account_no,balance)
status = True

while status:
    print("""Choose Operation --
1. Credit Amount
2. Debit Amount
3. Check Balance
4. Exit""")
    op = int(input())
    match op:
        case 1 :
            u1.credit()
        case 2 :
            u1.debit()
        case 3 :
            u1.balance_print()
        case 4:
            status = False
        case _:
            print("!!Choose the Correct Operation")