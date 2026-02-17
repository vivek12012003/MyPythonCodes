

class Animal:

    def __init__(self,name):
        self.name = name        

    def show_animal(self):
        print(f'{self.name} this is an animal')


class Dog(Animal):
    def show_dog(self):
        print(f'Dog barks')


d = Dog

