from collections import deque


size = [int(x) for x in input().split(' ')]
start = input()
coor = input().split(' ')

visited = set()

matrix = []
for i in range(size[0]):
    for j in range(size[1]):
        matrix.append([i,j])

queue = deque()
for i in range(0,len(coor)-1,2):
    row,col = int(coor[i])-1,int(coor[i+1])-1
    queue.append((row,col))
    visited.add((row,col))

lastVisit = []

def isValid(matrix,visited,row,col):
    return  (0 <= row < size[0]) and (0 <=  col < size[1]) and (row,col) not in visited

def bfs(matrix):
    directions = [(0,1),(1,0),(0,-1),(-1,0)]

    while queue:
        i,j = queue.popleft()
        for direc in directions:
            new_row,new_col = i+direc[0],j+direc[1]
            if  isValid(matrix,visited,new_row,new_col):
                queue.append((new_row,new_col))
                visited.add((new_row,new_col))
                lastVisit.append((new_row+1,new_col+1))


bfs(matrix)
print(lastVisit[-1][0],lastVisit[-1][1])