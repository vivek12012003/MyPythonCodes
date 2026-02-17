
class Shape:

    def __init__(self,x,y):
        self.x = x
        self.y = y  
    
    def area(self):
        return self.x * self.y
    
class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius
        #set parent class constructor value
        super().__init__(radius,radius)

    #wrong way to do
    # def area(self):
    #     return 3.14*self.radius*self.radius

    def area(self):
        return 3.14 * super().area() #method override here

rec = Shape(2,4)

print(rec.area())


cir = Circle(5)

print(cir.area())