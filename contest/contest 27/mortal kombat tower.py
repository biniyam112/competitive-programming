cases = int(input())
for _ in range(cases):
    input()
    bosses = input().split()
    bosses = [int(x) for x in bosses]
    # one is friends turn
    turn = True
    # consequetive kills
    kills = 0
    skips = bosses[0]
    i = 1
    while i+1 < len(bosses):
        if turn:
            if kills == 1:
                if bosses[i+1] == 0:
                    i += 1
                    kills += 1
        else:
            if i+1 < len(bosses):
                i += 1
            kills += 1
        if kills == 2:
            turn = not turn
