

import time

for i in range(1):
    print(i)
    time.sleep(1) #wait for 1 second

for i in range(60):

    t = time.localtime()

    formmated_time = time.strftime('%Y-%m-%d %H:%M:%S')

    print(f'\r{formmated_time}',end='')
    time.sleep(1)