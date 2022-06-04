import string


length = int(input())
words = []
for _ in range(length):
    words.append(input())
visited = set()
order = []


def findOrder(words):
    for word in words:
        if not visited or word[0] not in visited or (word[0] in visited and word[0] == order[-1]):
            visited.add(word[0])
            order.append(word[0])
        else:
            return 'Impossible'

findOrder(words=words)
output = ''
counter  = 0
print(order)
for i in string.ascii_lowercase :
    print(output)
    if counter == 0 and i not in visited and i < order[0]:
        output+= i
        continue
    if counter == 0 and i == order[0]:
        output += order[0]
        counter +=1
    elif  i > order[counter]:
        output+=order[counter]
        counter += 1
    else :
        output += i
print(output)
    




