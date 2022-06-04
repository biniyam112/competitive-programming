import random
output  = []
rn = random.random()
for i in range(1000):
    temp = []
    for j in range(2):
        temp.append(random.randint(1,1000))
    output.append(temp)
with open('testcase helper/couple/file.txt','w') as file:
    file.write(str(output))