cases = int(input())
for _ in range(cases):
    input()
    baloons = input()
    s = set()
    counter = 0
    for b in baloons:
        if b not in s:
            counter += 2
            s.add(b)
        else:
            counter += 1
    print(counter)
