def toys(w):
    # Write your code here
    w.sort(reverse=True)
    counter = 1
    maxweight = w[-1]+4
    while w:
        if w[-1] <= maxweight:
            w.pop()
        else:
            maxweight = w[-1]+4
            counter+=1
    return counter