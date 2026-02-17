

class Parent:

    def parent_method(self):
        print('This is a parent class')

class Child(Parent):

    def parent_method(self):
        print('This is a Parent method 2')

    def child_method(self):
        print('This is a child method')
        self.parent_method()
        #now if we want to call the parent class method so we use the super keyword
        super().parent_method()

c = Child()
c.child_method()

#next example




class Employee:

    def __init__(self,name,id):
        self.name = name
        self.id = id

class Programmer(Employee):

    #this is wrong u use same line twice

    # def __init__(self, name, id, lang):
    #     self.name = name
    #     self. id = id
    #     self.lang = lang

    def __init__(self, name, id ,lang):
        super().__init__(name, id)
        self.lang = lang


e1 = Employee('Rohan',532)

e2 = Programmer('Sohan',685,'Python')

print(e1.name)
print(e1.id)
print(e2.name)
print(e2.id)
print(e2.lang)
