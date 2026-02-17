
from Speech.Text_to_speech import speak 
import time
s = speak()

n = int(input("Enter the CountDown Timer : "))

while True:
    if n == 0:
        break

    min,sec = divmod(n,60)
    timer = f'{min:02d} : {sec:02d}'
    print(timer,end='\r')
    time.sleep(1)
    s.sp(sec)


    n = n-1

print('fire in the hole')
