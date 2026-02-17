import os

# f = open("demo.txt","r")
# #rint(data)
# #readline
# line1 = f.readline()
# print(line1)
# f.close()

#for write

# f = open("demo.txt","w")

# f.write("this is a write mode text.")

#for append

# f = open("demo.txt","a")

# f.write("and now this is a append line")


# f.close()

#creating the file

# f = open("demo1.txt","w")

# f.write("This file is created by the code.")

# f.close()


#with syntax

with open("demo.txt","r") as f :
    data = f.read()
    print(data)
    f.close()


#delete file

os.remove("demo1.txt")