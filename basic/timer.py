import time

seconds = 60

while seconds >= 0:
    print(f"\r⏰ Time Left: {seconds:02d}", end="")
    time.sleep(1)
    seconds -= 1
    

print("\n⏱️ Time Over!")
