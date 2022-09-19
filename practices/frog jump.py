cases = int(input())

for _ in range(cases):
    jumps = input()
    max_jump = 1
    prev_r = -1
    for i in range(len(jumps)):
        if jumps[i] == 'R':
            max_jump = max(i-prev_r, max_jump)
            prev_r = i
    max_jump = max(max_jump, len(jumps)-prev_r)
    print(max_jump)
