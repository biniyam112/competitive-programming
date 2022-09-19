temp = input().split()
n,t = int(temp[0]),int(temp[1])
queue = input()
queue = [x for  x in queue]
for _ in range(t):
    index  = 0
    while index < len(queue)-1:
        if queue[index] == 'B' and queue[index+1] == 'G':
            queue[index],queue[index+1] = queue[index+1],queue[index]
            index+=2
        else:
            index+=1
print(''.join(queue))

