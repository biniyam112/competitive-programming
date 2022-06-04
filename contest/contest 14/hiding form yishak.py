cases = int(input())
for _ in range(cases):
    items = int(input())
    column = input().split()
    if len(column) == 0:
        print(0)
    else:
        column = [int(x) for x in column]
        #? decreasing mono stack
        monoStack = []
        i = 0
        counter = 0
        while i < len(column):
            if not monoStack or monoStack[-1] >= column[i]:
                monoStack.append(column[i])
            else:
                while monoStack and column[i] > monoStack[-1]:
                    monoStack.pop()
                    counter+=1
                monoStack.append(column[i])
            i+=1
        print(counter)
    
    