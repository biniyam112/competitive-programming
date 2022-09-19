cases = int(input())
for _ in range(cases):
    word = input()
    days = 0
    i = 0
    while i < len(word):
        visited = set()
        j = 0
        k = i
        while j < 3 and k < len(word):
            if word[k] not in visited:
                visited.add(word[k])
                j += 1
            k += 1
        i = k
        days += 1
        while i < len(word) and word[i] in visited:
            i += 1
    print(days)
