num = int(input())
if num ==0:
    print(0)
else:
    n = num
    counter  = 0
    while n > 1:
        if n %2 == 1:
            counter +=1
        n = n // 2
    # n = len(bin(num))-3
    # temp = 1 << n
    # num &= ~temp
    print(1+counter)