cases = int(input())
for _ in range(cases):
    count = int(input())
    candies = input().split()
    candies = [int(x) for x in candies]
    candies.sort()
    amount = 0
    for candy in candies:
        amount += candy-candies[0]
    print(amount)