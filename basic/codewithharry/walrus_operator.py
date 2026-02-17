
# ':' walrus operator used to assign value in the operation

a = True

print(a:=False)



foods = list()
#without walrus operaotr

# while True:
#     food = input('What food do you like : ')
#     if food == 'quit':
#         break
    
#     foods.append(food)

# print(foods)

while(food:=input('what food you like : ')) != 'quit':
    foods.append(food)

print(foods)