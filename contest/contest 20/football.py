players = input()
counter = 1
prevItem = players[0]
for i in range(1,len(players)):
    if players[i] == prevItem:
        counter +=1
    else:
        prevItem = players[i]
        counter = 1
    if counter == 7:
        print('YES')
        break
if counter != 7:
    print('NO')
    