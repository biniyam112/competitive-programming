a,b,c = map(int,input().split())
def recursion(a):
    if a==1:
        return '1'
    value = recursion(a//2)
    if  a%2==0:
        return value+'0'+value
    else:
        return value+'1'+value
value = recursion(a)
counter = 0
for i in range(b-1,c):
    if value[i] == '1':
        counter+=1
print(counter)