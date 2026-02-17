

class Employee :

    company = 'google' #class variable, use same or all objects

    def __init__(self,name):
        self.name = name #instance variable means object jis name ka h uski details aayengi har object ki different details

        self.raise_amount = 0.43 #instance variable

    def showdetails(self):
        print(f'Employee name is {self.name} and raise amount is {self.raise_amount} of company {self.company}')


emp1 = Employee('vivek')

# Employee.showdetails(emp1) # both works same
emp1.raise_amount = 0.7

emp1.showdetails()



emp2 = Employee('rohan')
emp2.showdetails()