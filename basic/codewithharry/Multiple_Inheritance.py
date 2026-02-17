
class Employee:
    def __init__(self,name):
        self.name = name

    def show(self):
        print(f'the name is {self.name}')

class Dancer:
    def __init__(self,dance):
        self.dance = dance

    def show(self):
        print(f'Dance is {self.dance}')    
    
class DanceEmployee(Employee,Dancer) :
    def __init__(self,name,dance):
        self.name = name 
        self.dance = dance

    #call by just object name
    def __str__(self):
        return f"{self.name} {self.dance}"


o = DanceEmployee('vivek','break dance')
print(o)

o.show()