
# f = open("demo.txt",'r')

# text = f.read()
# print(text)

# f.close()

with open('demo.txt','r') as f :
    txt = f.read()
    l = txt.split(',')
    for i in range(0,len(l)):
        print(l[i]) 
    #seek() move to the next 5 byte
    f.seek(5)
    #tell() which position the byte is 
    print(f.tell())
    data = f.read(5)
    print(data)

with open('sample.txt','w') as f:
    f.write('Hello World!')
    #truncate() kitne byte tk store krna h file me
    f.truncate(3)
    
