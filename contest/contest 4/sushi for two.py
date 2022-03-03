n = input()
m = input()
m = m.split(" ")
counter = 0
maxcounter = 2
i  = len(m) //2
j = len(m)//2
while i < j :
    if m[i] != m[j] :
        if  i == 0 or  m[i] == m[i-1]:
            counter+=2
            i+=1
            j-=1
        else:
            maxcounter = max(maxcounter,counter)
            counter=2
            i+=1
    else:
        maxcounter = max(maxcounter,counter)
        counter=0
        i+=1
maxcounter = max(maxcounter,counter)
counter = 0
i = 0 
j = len(m)-1
while i < j :
    if m[i] != m[j]:
        if j == len(m)-1 or  m[j] == m[j+1]:
            counter+=2
            i+=1
            j-=1
        else:
            maxcounter = max(maxcounter,counter)
            counter=2
            j-=1
    else:
        maxcounter = max(maxcounter,counter)
        counter=0
        j-=1
maxcounter = max(maxcounter,counter)
print(maxcounter)