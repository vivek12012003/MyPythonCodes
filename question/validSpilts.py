
#given array me se right side ke ese kitne count h jinka sum left side se bada ya bara h(>=) 

a = [10,4,-8,7,3,6]

total_sum = sum(a)
current_sum = 0
count = 0
for i in range (len(a)-1):
    current_sum +=a [i]

    if current_sum >= (total_sum - current_sum):
        count +=1 

print(count)
