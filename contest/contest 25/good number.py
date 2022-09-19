temp = input().split()
k = int(temp[1])
counter = 0
s = set()
for i in range(k+1):
    s.add(str(i))
for _ in range(int(temp[0])):
    num = input()
    num = set(num)
    cor = True
    for i in s:
        if i not in num:
            cor = False
    if cor and len(set(num)) >= len(s):
        counter += 1
print(counter)
