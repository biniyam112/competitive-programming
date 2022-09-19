n = int(input())
p = input().split()
p = [int(x) for x in p]
q = input().split()
q = [int(x) for x in q]
s = set()
for i in range(1, len(p)):
    s.add(p[i])
for i in range(1, len(q)):
    s.add(q[i])
can_pass = True
for i in range(1, n+1):
    if i not in s:
        print('Oh, my keyboard!')
        can_pass = False
        break
if can_pass:
    print('I become the guy.')
