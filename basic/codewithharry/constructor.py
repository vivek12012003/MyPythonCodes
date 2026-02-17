
class Person :

    def __init__(self,n,o):
        self.name = n
        self.occ = o
    def info(self):
        print(f'{self.name} is a {self.occ}')

a = Person('vivek','HR')
a.info()

b = Person('Hema','Sale')
b.info()