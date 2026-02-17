
#you have given the array ho stock price, calculate when we buy and sell the stock through which u gain maximum profit


profit = 0
price = [7,1,5,3,5,6]

for i in range(1,len(price)):

    if price[i] - price[i-1] > 0:
        profit += price[i]-price[i-1]

print(profit)