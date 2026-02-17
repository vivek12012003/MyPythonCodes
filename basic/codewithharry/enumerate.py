
marks = [55,65,77,34,78,78,34]

for index, mark in enumerate(marks):

    print(f"{index} : {mark}")

print('start index at 1')
for index, mark in enumerate(marks,start = 1):

    print(f"{index} : {mark}")
    