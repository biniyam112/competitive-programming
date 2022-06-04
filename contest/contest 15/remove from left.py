s = input()
t = input()
totalLen = len(s)+len(t)
for i in range(-1,-min(len(s),len(t))-1,-1):
    if s[i] == t[i]:
        totalLen-=2
    else:
        break
print(totalLen)