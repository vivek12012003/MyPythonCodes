

class Employee:

    def __init__(self, name, salary):

        self.name = name
        self.salary = salary

    #by class method

    @classmethod
    def fromStr(cls, string):
        return cls(string.split('-')[0], int(string.split('-')[1]))
    
e1 = Employee('vivek', 50000)

print(e1.name, e1.salary)

s = 'rohan-10000'

#first and normal way
e2 = Employee(s.split('-')[0],s.split('-')[1])
print(e2.name, e2.salary)



#class method
s1 = 'sohan-60000'
e3 = Employee.fromStr(s1)
print(e3.name, e3.salary)

