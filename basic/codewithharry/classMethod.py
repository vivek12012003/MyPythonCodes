

#for changing the value of class level variable

class Employee:

    company = 'Apple'

    def show(self):

        print(f"The name is {self.name} and company name is {self.company}")

    @classmethod
    def changecompany(self,newCompany):
        self.company = newCompany

e1 = Employee()

e1.name = 'Vivek'
e1.show()
e1.changecompany('Tesla')
e1.show()
print(e1.company)