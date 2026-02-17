
# class Student:

#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
    
#     def welcome(self):
#         print(f"Welcome, {(self.name).upper()}")
#         print(f"Your age is : {self.age}")            


# s1 = Student("vivek",22)

# s1.welcome()


class Person():
    name = ""
    occupation = ''

    def info(self):
        print(f'{self.name} is a {self.occupation}')

a = Person()

a.name = "Vivek"
a.occupation = "Software Developer"

b = Person()
b.name= 'Tashqeen'
b.occupation = 'HR'

a.info()
b.info()