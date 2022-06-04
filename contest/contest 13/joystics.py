val = input().split()
j1,j2 = int(val[0]),int(val[1])
time = 0
while (not (j1 <= 1 and j2 <= 1)) and j1 != 0 and j2 != 0:
    if j1 >= j2:
        j2 += 1
        j1 -= 2
    else:
        j1 += 1
        j2 -= 2
    time += 1
print(time)
