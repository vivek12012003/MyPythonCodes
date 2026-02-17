

class animal:
    def __init__(self,name):
        self.name = name
    
    def info(self):
        print("Animal Name : ",self.name)

class dog(animal):
    def sound(self):
        print(self.name, " barks")

d = dog("buddy")
d.info()
d.sound()