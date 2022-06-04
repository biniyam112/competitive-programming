val = input().split()
cities,capacity = int(val[0]),int(val[1])
cash = 0
fuel = 0
i = 1
required = cities-i
if capacity >= required:
    print(required)
else:
    fuel = capacity
    cash = capacity
    while fuel < required:
        i+=1
        fuel += 1   
        cash += i
    print(cash)
        


