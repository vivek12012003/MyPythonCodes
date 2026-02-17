
class Student:

    def __init__(self,name):
        # self.name = name # public variable
        self.__name = name # private (__) variable

    
s = Student('vivek')

# print(s.name)#can't be accessed private variable

print(s._Student__name)# access through like this <-

print(dir(s))