strairs = int(input())
strairHeight = input().split()
strairHeight = [int(x) for x in strairHeight]
boxes = int(input())
boxesDimention = []
for _ in range(boxes):
    temp = input().split()
    boxesDimention.append([int(temp[0]), int(temp[1])])
print(boxesDimention)
