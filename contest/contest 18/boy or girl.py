username = input()
seen = set()
counter = 0
for char in username:
    if char not in seen:
        seen.add(char)
        counter+=1
if counter % 2 == 0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')