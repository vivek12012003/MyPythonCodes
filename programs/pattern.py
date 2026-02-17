
num = int(input())
for i in range(0,num):
    t= num - i
    # print(f"{'*':>{t}s}")
    print('{:>{}s}'.format('*',t))