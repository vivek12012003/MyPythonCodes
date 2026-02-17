
import os

# print(os.getcwd())

# if(not os.path.exists('testOs')):
#     os.mkdir('testOs')

# for i in range (0,10):
#     os.mkdir(f"testOs/Day {i+1}")


# for i in range (0,10):
#     os.rename(f'testOs/Day {i+1}',f'testOs/Tutorial {i+1}')


# print(os.listdir('testOs'))

for i in range (0,10):
    if(f'testOs/Tutorial {i+1}' == f'testOs/Tutorial {5}'):
        os.mkdir(f'testOs/Tutorial 5/newfile.txt')
   
        
        

for i in os.listdir('testOs'):
    print(os.listdir(i))
