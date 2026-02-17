
import time


def forwhile():

    i = 0
    while i<500000:
        i+=1
        continue

def forfor():

    i = 0
    for i in range(500000):
        continue

start = time.time()#tell the time from 1970 to yet
forwhile()
print(time.time()-start)

start1 = time.time()
forfor()
print(time.time()-start1)