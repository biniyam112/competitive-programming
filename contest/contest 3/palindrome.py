m = str(input())
temp = list(m)
reverse = []
for i in range(len(temp)-1,-1,-1):
    reverse.append(temp[i])
print(int(''.join(temp+reverse)))