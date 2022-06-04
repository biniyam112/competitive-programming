

inputs = int(input())

red = []
blue = []
for i in range(inputs):
    length = int(input())
    red = input()
    blue = input()
    red = [int(x) for x in red]
    blue = [int(x) for x in blue]
    red_ = 0
    blue_  = 0
    for i in range(len(red)):
        if red[i] > blue[i]:
            red_+=1
        elif red[i] < blue[i]:
            blue_+=1
    if red_ > blue_:
        print('RED')
    elif red_ < blue_:
        print('BLUE')
    else:
        print('EQUAL')