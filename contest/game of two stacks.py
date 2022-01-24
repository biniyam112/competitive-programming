def twoStacks(maxSum, a, b):
    # Write your code here
    a = list(map(int,a.split()))
    b = list(map(int,b.split()))
    print(a)
    print(b)
    # for only a
    counter1 = 0
    total = 0
    for i in a:
        total+=i
        if total > maxSum:
            break
        counter1+=1
    for i in b:
        total+=i
        if total > maxSum:
            break
        counter1 +=1
    
        
    # for only b        
    counter2 = 0
    total = 0
    for i in b:
        total+=i
        if total > maxSum:
            break
        counter2 +=1
    for i in a:
        total+=i
        if total > maxSum:
            break
    counter2 +=1
        
    # for both lists
    i = 0
    j = 0
    counter =0
    total = 0
    while True:
        if (a[i] < b[j] and i < len(a)-1) or j == len(b)-1:
            total += a[i]
            i +=1
        elif (a[i] > b[j] and j < len(b)-1) or i == len(a)-1 :
            total += b[j]
            j+=1
        if total > maxSum:
            break  
        counter+=1
    print(max(counter,counter1,counter2))

twoStacks(62,'7 15 12 0 5 18 17 2 10 15 4 2 9 15 13 12 16','12 16 6 8 16 15 18 3 11 0 17 7 6 11 14 13 15 6 18 6 16 12 16 11 16 11')
twoStacks(77,'11 4 1 11 10 6 5 1 1 19 9 7 1 16 14 2 14 19 0 4 10 1 1 11 2 11 5 7 0 13','16 4 17 9 15 19 16 0 0 9 11 10 17 4 18 3 6')
twoStacks(60,'17 5 0','10 8 2 1 13 1 14 18 9 18 16 19 5')
twoStacks(33,'4 11 9',
'0 15 6 6 9 8 1 11 10 8 3 11 9 9 18 17 3 5 10 12 9 14 15 6 14 7 7 4 3 10 5 15 6 11 1 7 12 14 10 2 2 14 13 4 3 3 13 18 0 3')