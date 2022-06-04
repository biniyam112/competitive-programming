cases = int(input())
for i in range(cases):
    bounds = input().split()
    n = int(bounds[1])
    m = int(bounds[0])
    isInBound  = lambda row,col : 0 < row <= n and 0 < col <= m
    dirs = [0,1,0,-1,0]
    output = []
    visited = set()
    def dfs(row,col,prev,moves):
        visited.add((row,col))
        if  row == n and col == m:
            output.append(moves)
        for i in range(4):
            new_row,new_col = row + dirs[i] , col + dirs[i+1]
            if  isInBound(new_row,new_col) or (new_row,new_col) not in visited or i != prev:
                dfs(new_row,new_col,i,moves+1)
    dfs(1,1,5,0)
    if output:
        print(min(output))
    else:
        print('-1')

