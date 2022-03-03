n,k=map(int,input().split())
remaining = 240 - k
counter = 0
def recursion(remaining:int,counter:int):
    if remaining - ((counter+1)*5) < 0 :
        if counter > n:
            print(n)
        else:
            print(counter)
    else:
        counter+=1
        remaining -= 5*counter
        recursion(remaining,counter)
recursion(remaining,counter)

    