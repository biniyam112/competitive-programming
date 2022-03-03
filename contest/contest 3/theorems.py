total,k=map(int,input().split())
theorems = [int(x) for x in input().split()]
mood = [int(x) for x in input().split()]
start = 0
end = start+k-1
# k = window size
counter = 0
maxtheorem = 0
for i in range(total):
    if  mood[i] ==1:
        counter += theorems[i]
for i in range(k):
    if  mood[i] == 0 :
        maxtheorem+= theorems[i]
temp = maxtheorem
print(maxtheorem)
print('==================')
start+=1
while end < total:
    if mood[start] == 0:
        temp -= theorems[start]
    if mood[end] == 0 :
        temp += theorems[end]
    print(temp)
    maxtheorem = max(maxtheorem,temp)
    start+=1
    end+=1
print(counter+maxtheorem)