cases = int(input())
for _ in range(cases):
    part1 = 0
    part2 = 0
    s = input()
    for i in range(len(s)):
        if i < 3:
            part1+=int(s[i])
        else:
            part2+=int(s[i])

    if part1 == part2:
        print("YES")
    else:
        print('NO')