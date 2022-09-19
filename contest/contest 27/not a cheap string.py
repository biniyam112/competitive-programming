cases = int(input())
for _ in range(cases):
    s = input()
    max_ = int(input())
    tot = 0
    v = []
    for i in range(len(s)):
        val = ord(s[i])-96
        tot += val
        v.append((val, i))
    v.sort(reverse=True)
    i = 0
    removed = set()
    while i < len(v) and tot > max_:
        tot -= v[i][0]
        removed.add(v[i][1])
        i += 1
    ans = ''
    for i in range(len(s)):
        if i not in removed:
            ans += s[i]
    print(ans)
