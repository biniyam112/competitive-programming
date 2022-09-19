dim = int(input())
queen = input().split()
king = input().split()
goto = input().split()
queen = [int(x) for x in queen]
king = [int(x) for x in king]
goto = (int(goto[0]), int(goto[1]))
covered = set()
def inbound(col, row): return 1 <= col <= dim and 1 <= row <= dim


for i in range(1, dim+1):
    covered.add((queen[0], i))
for i in range(1, dim+1):
    covered.add((i, queen[1]))
i = queen[0]
j = queen[1]
while inbound(i, j):
    covered.add((i, j))
    i += 1
    j += 1
i = queen[0]
j = queen[1]
while inbound(i, j):
    covered.add((i, j))
    i -= 1
    j -= 1

dirs = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]


def dfs(col, row, found):
    if (col, row) == goto:
        found[0] = True
        return
    visited.add((col, row))
    for way in dirs:
        new_col, new_row = col+way[0], row+way[1]
        if not found[0] and inbound(new_col, new_row) and (new_col, new_row) not in covered and (new_col, new_row) not in visited:
            dfs(new_col, new_row, found)


visited = set()
found = [False]
if inbound(king[0], king[1]):
    dfs(king[0], king[1], found)
if found[0]:
    print('YES')
else:
    print('NO')
