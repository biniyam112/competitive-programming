input()
word = input()
word = word.lower()
s = set()
for c in word:
    s.add(c)
if len(s) == 26:
    print('YES')
else:
    print('NO')
