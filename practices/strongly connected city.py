size = input()
hor = input()
ver = input()
output = "Yes"
dirs = [hor[0]+ver[0],hor[0]+ver[-1],hor[-1]+ver[-1],hor[-1]+ver[0]]
wrong =['<^','>^','>v','<v']

for i in range(len(wrong)):
    # print(output)
    if dirs[i] ==  wrong[i]:
        output = "No"
        break
print(output)