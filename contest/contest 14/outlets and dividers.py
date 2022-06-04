cases = int(input())
for _ in range(cases):
    temp = input().split()
    students = int(temp[0])
    outlets = 2
    dividers = input().split()
    dividers = [int(x) for x in dividers]
    if outlets > students:
        print(0)
    else:
        dividers.sort(reverse=True)
        # print(dividers)
        counter = 0
        while counter < len(dividers) and students > outlets:
            outlets += dividers[counter]-1
            counter+=1
        if outlets >= students:
            print(counter)
        else:
            print(-1)