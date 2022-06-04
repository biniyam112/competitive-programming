t = int(input())
testcases = []
for i in range(t):
    testcases.append(int(input()))
for i in testcases:
    if i < 32:
        print('31')
        continue
    else:
        diff = i - 32
        if diff % 4 > 0:
            print('31')
        else:
            print('32')