cases = int(input())
for _ in range(cases):
    items = input().split()
    math = int(items[0])
    prog = int(items[1])
    if math == 0 or prog == 0:
        print(0)
    else:
        if math > prog:
            ratio = math//prog
        else:
            ratio = prog//math
        if ratio < 3:
            print((math+prog)//4)
        else:
            print(min(prog, math))
