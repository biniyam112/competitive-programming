temp = input().split()
k = int(temp[1])
n = int(temp[0])
left = input()
left = [x for x in left]
right = input()
right = [x for x in right]
ladders = [left, right]
visited = {}


def dfs(i, side, waterlevel):
    if ladders[side][i] == 'X':
        return False
    if i+k >= n:
        return True
    if (side, i) in visited:
        return visited[(side, i)]
    up = down = jump = False
    if ladders[side][i+1] != 'X':
        up = dfs(i+1, side, waterlevel+1)
        visited[(side, i)] = up
    if ladders[not side][i+k] != 'X':
        jump = dfs(i+k, not side, waterlevel+1)
        visited[(not side, i)] = jump
    if i-1 >= 0 and ladders[side][i-1] != 'X' and i-1 > waterlevel+1:
        down = dfs(i-1, side, waterlevel+1)
        visited[(side, i)] = down
    return up or down or jump


if dfs(0, 0, -1):
    print('YES')
else:
    print('NO')
