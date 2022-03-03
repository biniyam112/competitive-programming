n,m,k=map(int,input().split())
# m = total times you can use imoticon
# k = times to use imoticon in a row
items = [int(x) for x in input().split()]
max_1 = 0
max_2 = 0
temp = 0
for i in range(len(items)):
    if items[i] > max_1:
        max_1 = items[i]
        temp = i
for i in range(len(items)): 
    if items[i] > max_2 and i != temp:
        max_2 = items[i]
output = 0
rep = m//(k+1)
output += (k * max_1 + max_2) * rep 
output += (m % (k+1))  * max_1
print(output)