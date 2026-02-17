
import os

os.chdir('F:\Python Learn\cluster')
print(os.getcwd())

count = 1
extension = 'png'

for file in os.listdir():

    if file.endswith(f'.{extension}'):
        os.rename(file,f'{count}.{extension}')
        count +=1


        
