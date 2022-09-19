temp = input().split()
height = int(temp[1])
temp = input().split()
friends = [(int(x)) for x in temp]
minWidth = 0
for i in friends:
    if i > height:
        minWidth += 2
    else:
        minWidth += 1
print(minWidth)
