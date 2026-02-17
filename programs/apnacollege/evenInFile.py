
with open("demo.txt","r") as f:
    data = f.read()
    l = data.split(",")
    count = 0
    for i in l :
        if int(i)%2 == 0:
            count+=1

print(count)