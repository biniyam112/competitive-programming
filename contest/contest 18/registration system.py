cases = int(input())
seen = {}
for _ in range(cases):
    username = input()
    if username not in seen:
        seen[username] =  0
        print('OK')
    else:
        seen[username] += 1
        print(username+str(seen[username]))

