
from git import List


def countNegatives(grid: List[List[int]]) -> int:
    counter = 0
    mid = 0
    j = len(grid[0])-1
    for item in grid:
        i = 0
        if len(item) == 1:
            if item[0] < 0:
                counter+=1
            else:
                continue
        while j >= i:
            mid = i + (j-i)//2
            if mid+1 >= len(item):
                break
            if item[mid] >= 0 and item[mid+1] >= 0:
                i = mid+1
            elif item[mid] < 0 and item[mid+1] < 0:
                if mid == 0:
                    counter+= len(item)
                    break
                j = mid-1
            elif item[mid] >= 0 and item[mid+1]< 0:
                counter+=len(item)-(mid+1)
                j = mid
                break
    print(counter)


countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]])