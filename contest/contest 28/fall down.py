cases = int(input())
for _ in range(cases):
    temp = input().split()
    rows, cols = int(temp[0]), int(temp[1])
    grid = []
    for _ in range(rows):
        grid.append([x for x in input()])
    for j in range(cols):
        for i in range(rows-2, -1, -1):
            k = i
            if grid[i][j] == '*':
                while k+1 < rows and grid[k+1][j] == '.':
                    grid[k][j], grid[k+1][j] = grid[k+1][j], grid[k][j]
                    k += 1
    s = ''
    for item in grid:
        for c in item:
            s += c
        s += '\n'
    print(s[:-1])
