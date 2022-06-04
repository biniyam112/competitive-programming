def getWays(n, c):
    # Write your code here
    counter = 0
    items = set()
    for i in c:
        items.add(i)
    for i in c:
        if n % i == 0:
            counter+=1
        while i < n:
            i = i**2
            if n-i in items:
                counter+=1
    return counter