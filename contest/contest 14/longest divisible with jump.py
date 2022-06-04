temp = input().split()
size = int(temp[0])
divisor = int(temp[1])
nums = input().split()
nums = [int(x) for x in nums]
nums.sort()
counter = 1
total = 0
items = {}
for i in nums:
    total += i
    if total > counter * divisor :
        pass
    if total % counter*divisor == 0:
         counter +=1

