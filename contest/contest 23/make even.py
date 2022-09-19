cases = int(input())
for _ in range(cases):
    num = int(input())
    if num % 2 == 0:
        print('0')
    else:
        num = str(num)
        if int(num[0]) % 2 == 0:
            print('1')
        else:
            noEven = True
            for i in num:
                if int(i) % 2 == 0:
                    noEven = False
            if noEven:
                print('-1')
            else:
                print('2')
