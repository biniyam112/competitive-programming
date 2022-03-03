count = int(input())
items = []
for i in range(count):
    item = input()
    items.append(item)
for item in items:
    output = []
    i = 0
    j = i+1
    if len(item) == 1:
        print(item)
    else:
        while j < len(item):
            if item[i] != item[j]:
                output.append(item[i])
                i+=1
                j+=1
            else:
                i+=2
                j+=2
            if j >= len(item) and i >= len(item):
                break
            if j >= len(item) and i < len(item):
                output.append(item[i])
        output = list(set(output))
        output.sort()
        print(''.join(output))