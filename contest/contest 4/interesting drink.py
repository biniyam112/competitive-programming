import heapq
from itertools import count


shops = int(input())
prices = input()
prices = prices.split(" ")
prices = [int(x) for x in prices]
days = int(input())
coins = []
for i in range(days):
    coins.append(int(input()))


prices.sort()
i = 0
j = len(shops)-1
for coin in coins :
    while i <= j:
        mid = i + (j-i)//2
        if  prices[mid] > coins:
            j = mid
        else:
            i = mid
    
    
    
