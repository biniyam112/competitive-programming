cases = int(input())
for i in range(cases):
    num = int(input())
    power = 2 ** (len(bin(num))-3)-1
    print(power)