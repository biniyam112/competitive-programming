from collections import defaultdict, deque


count = int(input())
nodes = defaultdict(list)
root = input().split()
nodes[root[0]].append(root[1])
for _ in range(count-2):
    node = input().split()
    nodes[node[0]].append(node[1])

order = input().split()
new_order = defaultdict(list)
queue = deque()
queue.append((root[0], 0))
if order[0] != '1':
    print('NO')
else:
    while queue:
        node, level = queue.popleft()
        new_order[level].append(node)
        for i in nodes[node]:
            queue.append((i, level+1))
    start = 0
    prob = False
    for k, v in new_order.items():
        temp = order[start:start+len(v)]
        temp.sort()
        v.sort()
        start += len(v)
        if v != temp:
            prob = True
            break
    if prob:
        print('NO')
    elif len(order) == start:
        print('YES')
