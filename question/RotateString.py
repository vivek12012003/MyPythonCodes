
#given two string if rotate string 1 can it get string two

s = 'abcde'
goal = 'cdeab'

if len(s) != len(goal):
    print('False')
    exit

else :
    s1 = s+s
    if goal in s1:
        print('True')
    else:
        print(False)