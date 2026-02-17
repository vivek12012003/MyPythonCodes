
age = int(input('Enter the age : '))

# age_check = lambda a: 'Adult' if a >= 18 else 'Minor'
# print(age_check(age))
age_check = lambda : 'Adult' if age >= 18 else 'Minor'
print(age_check())


