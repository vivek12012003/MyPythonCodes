
class Math:

    #without static method u have to use 'self' keyword   
    def add(self,a,b):  
        return a+b
    
    #with static method no need to use 'self' keyword
    @staticmethod
    def minus(a,b):
        return a-b



m = Math()
# sum = m.add(2,3) #it needs and object and instance to call
# print(sum)


#we can static method with instance and without by using class name
print(Math.minus(5,3))
#or
print(m.minus(5,1))