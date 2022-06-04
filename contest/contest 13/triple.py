import time


start_time = time.time()
cases =  int(input())
for _ in range(cases):
    length = int(input())
    nums = input().split()
    if length < 3:
        print('-1')
        continue
    dict = {}
    found = False
    for i in nums:
        if int(i) in dict:
            dict[int(i)] += 1
            if dict[int(i)] == 3:
                print(i)
                found = True
                break
        else:
            dict[int(i)] = 1
    if not found:
        print('-1')

print(time.time()-start_time)
    