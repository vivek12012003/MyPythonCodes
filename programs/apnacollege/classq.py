
class Student:

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
       
    def get_average(self):
        avg = sum(self.marks)/3
        return avg


s1 = Student('Vivek',[97,87,78])
print(s1.get_average())