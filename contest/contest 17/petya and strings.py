s = input()
t = input()
found = False
for i in range(len(s)):
    first = s[i].lower()
    second = t[i].lower()
    diff = ord(first) - ord(second)
    if diff != 0:
        if diff > 0:
            print(1)
        else:
            print(-1)
        found = True
        break
if not found:
    print(0)