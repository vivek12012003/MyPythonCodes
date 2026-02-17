
class circle_OP:
    def __init__(self,r):
        self.radius = r
    def area(self):
        area = float(3.14 * self.radius * self.radius)
        return area
    


r = int(input("Enter Radius : "))
c = circle_OP(r)
print(c.area())