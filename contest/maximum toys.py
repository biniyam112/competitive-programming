def maximumToys(prices, k):
    # Write your code here
    toys = 0
    prices.sort()
    i = 0
    while k-prices[i] > 0:
        k -= prices[i]
        i +=1
        toys +=1
    return toys



maximumToys([2,4,6,7,8,2],1)