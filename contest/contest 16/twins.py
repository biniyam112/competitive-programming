from math import remainder


count = int(input())
coins = input().split()
coins = [int(x) for x in coins]

remaining = sum(coins)
coins.sort(reverse=True)
myHalf = 0
counter = 0
while myHalf <= remaining:
    myHalf += coins[counter]
    remaining-= coins[counter]
    counter+=1
print(counter)
